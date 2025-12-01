FROM python:3.11

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir ollama mcp


COPY app.py .
COPY agent_simple.py .
COPY mon_serveur_mcp.py .
COPY test_client.py .

CMD ["python", "mon_serveur_mcp.py"]