FROM python:3.11

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir ollama mcp


COPY agent_simple.py .
COPY mon_serveur_mcp.py .
COPY test_client.py .
COPY app.py .

# Copie du script Linux
COPY .sh .
# On le rend exécutable et on s'assure que les fins de ligne sont au format Unix
RUN sed -i 's/\r$//' .sh && chmod +x .sh

ENV OLLAMA_HOST=http://host.docker.internal:11434

CMD ["./.sh"]