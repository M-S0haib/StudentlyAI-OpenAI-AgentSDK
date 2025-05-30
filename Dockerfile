FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

ENV HOST=0.0.0.0
ENV PORT=8000

CMD ["chainlit", "run", "src/studently_ai/main.py", "--host", "0.0.0.0", "--port", "8000"]
