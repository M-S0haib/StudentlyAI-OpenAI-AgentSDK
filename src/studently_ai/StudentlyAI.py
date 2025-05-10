from __future__ import annotations
from pydantic import BaseModel
from openai.types.responses import ResponseTextDeltaEvent
from agents import (
    Agent,
    set_tracing_disabled,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
)
import chainlit as cl
import os



gemini_api_key = os.getenv("GEMINI_API_KEY")

if os.getenv("GEMINI_API_KEY") is None:
    raise ValueError("GEMINI_API_KEY is not set. Please set it and try again.")

set_tracing_disabled(disabled=True)

conversation_history = []

class NotStudyQuery(BaseModel):
    is_not_study_query: bool
    reasoning: str

guardrail_agent = Agent(
    name="Guardrail check",
    model="litellm/gemini/gemini-2.0-flash",
    instructions="""  
You are a filter that checks whether the user's latest message is truly off-topic and unrelated to their study goals.

DO NOT mark the query as off-topic just because it isn’t about a subject like math or science. It's normal for students to ask things like:

- How do you know my name?
- What did I say earlier?
- Who am I?
- What’s your name?

These are **valid** context questions and are allowed.

Only return `is_not_study_query: true` if:
- The user has clearly changed the subject to completely unrelated things (e.g., dating, movies, random facts) **for multiple turns**.
- They are being inappropriate, spammy, or disruptive.

Otherwise, return `is_not_study_query: false` and let the assistant continue.

Be lenient, and prioritize maintaining a helpful, conversational flow.

""",
    output_type=NotStudyQuery,
)

@input_guardrail
async def study_checker_guardrail(
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_not_study_query,
    )

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant named Studently AI which helps students with their studies. Use conversation history for context.",
    model="litellm/gemini/gemini-2.0-flash",
    input_guardrails=[study_checker_guardrail],
)

@cl.on_chat_start
async def start():
    await cl.Message(
        content="🎓 Hey! Welcome to **Studently AI**. I'm here to help you with your studies. Ask me anything!"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    try:
        user_input = message.content
        conversation_history.append({"role": "user", "content": user_input})

        history_prompt = "\n".join(
            f"{msg['role'].capitalize()}: {msg['content']}" for msg in conversation_history
        )
        combined_input = f"Conversation history:\n{history_prompt}\n\nCurrent input: {user_input}"

        guardrail_result = await Runner.run(guardrail_agent, combined_input)
        
        if guardrail_result.final_output.is_not_study_query:
            await cl.Message(
                content="Sorry! You are asking something other than study-related questions. Please ask a study-related question."
            ).send()
            return

        result = Runner.run_streamed(agent, combined_input)
        response = cl.Message(content="")
        await response.send()

        async for event in result.stream_events():
            if event.type == "raw_response_event" and hasattr(event.data, "delta"):
                token = event.data.delta
                await response.stream_token(token)

        conversation_history.append({"role": "assistant", "content": response.content})

    except InputGuardrailTripwireTriggered as e:
        await cl.Message(
            content="Sorry! You are asking something other than study-related questions. Please ask a study-related question."
        ).send()
