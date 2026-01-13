FROM python:3.11

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir ollama mcp


# On donne accès à ces fichiers à Docker
COPY agent_simple.py .
COPY mon_serveur_mcp.py .
COPY test_client.py .
COPY app.py .
COPY .sh .

# On le rend exécutable
RUN chmod +x .sh

ENV OLLAMA_HOST=http://host.docker.internal:11434

CMD ["./.sh"]