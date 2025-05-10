# StudentlyAI

StudentlyAI is an AI-powered study assistant designed to help students with their academic queries. Built using Python, Chainlit, and the LiteLLM framework, it provides a conversational interface with robust features like input guardrails, streaming responses, and context-aware memory. The assistant ensures that conversations remain focused on study-related topics, making it a reliable tool for educational support.

## Features

- **Conversational Study Assistant**: StudentlyAI engages with users to answer study-related questions, leveraging the Gemini 2.0 Flash model for accurate and contextually relevant responses.
- **Input Guardrails**: A custom guardrail system filters out off-topic or inappropriate queries, ensuring the assistant remains focused on academic content. It allows context-related questions (e.g., "What’s my name?") while blocking unrelated topics after multiple off-topic turns.
- **Streaming Responses**: Responses are streamed in real-time, providing a smooth and interactive user experience.
- **Context Memory**: Maintains conversation history to provide context-aware responses, allowing for coherent and relevant interactions over multiple turns.
- **Chainlit Integration**: Uses Chainlit for a user-friendly chat interface, making it easy to interact with the assistant.

## Prerequisites

- Python 3.8 or higher
- A Gemini API key (set as the `GEMINI_API_KEY` environment variable)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/studently-ai.git
   cd studently-ai
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set the Gemini API Key**:
   Export your Gemini API key as an environment variable:
   

## Usage

1. **Run the Application**:
   ```bash
   chainlit run StudentlyAI.py
   ```

2. **Interact with StudentlyAI**:
   - Open the provided URL (typically `http://localhost:8000`) in your browser to access the Chainlit chat interface.
   - Start asking study-related questions, and StudentlyAI will respond with context-aware, streamed answers.
   - The guardrail ensures that only study-related queries are processed, maintaining focus on academic topics.

## Project Structure

- `StudentlyAI.py`: The main application file containing the agent logic, guardrail implementation, and Chainlit event handlers.
- `requirements.txt`: Lists the required Python dependencies for the project.

## Example Interaction

**User**: "Can you explain the Pythagorean theorem?"  
**StudentlyAI**: The Pythagorean theorem states that in a right-angled triangle, the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides. Mathematically, it’s expressed as:  
\[ a^2 + b^2 = c^2 \]  
where \( c \) is the hypotenuse, and \( a \) and \( b \) are the other two sides. Would you like an example?  

**User**: "What’s your favorite movie?"  
**StudentlyAI**: Sorry! You are asking something other than study-related questions. Please ask a study-related question.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code follows the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please open an issue on the GitHub repository.

---

Happy studying with StudentlyAI! 🎓
