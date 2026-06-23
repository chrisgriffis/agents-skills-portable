FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install --no-cache-dir .

COPY . .

EXPOSE 8000

# For remote hosting via SSE transport
CMD ["python", "server.py", "--transport", "sse", "--port", "8000"]
