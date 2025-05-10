FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --index-url https://pypi.org/simple

COPY . .

ENV PORT=8000
EXPOSE $PORT

CMD ["chainlit", "run", "StudentlyAI.py", "--port", "$PORT"]