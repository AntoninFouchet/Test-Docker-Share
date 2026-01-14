# Test Docker - Serveur MCP & IA

Ce projet est un environnement de test utilisant Docker pour faire fonctionner un serveur **MCP (Model Context Protocol)** et des agents IA interagissant avec **Ollama**.

## Configuration de l'accès Internet

Vous pouvez autoriser ou bloquer l'accès à l'internet extérieur pour le conteneur via le fichier `.env`.

1. Ouvrez le fichier `.env`.
2. Modifiez la variable `DOCKER_NETWORK` :
   - `DOCKER_NETWORK=public_net` : Accès à Internet **autorisé** (par défaut).
   - `DOCKER_NETWORK=internal_net`  : Accès à Internet **bloqué** (réseau interne uniquement).
3. Redémarrez le conteneur pour appliquer les changements :
   ```bash
   docker-compose up --build
   ```

## Structure du projet

*   `mon_serveur_mcp.py` : Serveur MCP basé sur `FastMCP` offrant des outils pour lister, lire et analyser des fichiers via l'IA.
*   `test_client.py` : Client de test pour interagir avec le serveur MCP.
*   `agent_simple.py` : Un exemple d'agent IA simple utilisant la bibliothèque `ollama` pour analyser du code Python.
*   `app.py` : Script de test pour vérifier le bon fonctionnement des volumes Docker (écrit dans `data/test_volume.txt`).
*   `Dockerfile` & `docker-compose.yml` : Configuration pour conteneuriser l'application.
*   `.sh` : Script d'entrée du conteneur qui orchestre le lancement des différents tests.

## Prérequis

*   **Docker** et **Docker Compose** installés sur votre machine.
*   **Ollama** installé et en cours d'exécution sur votre machine hôte.
*   Le modèle `qwen2.5-coder:1.5b` doit être téléchargé dans Ollama (`ollama pull qwen2.5-coder:1.5b`).

## Installation et Utilisation

1.  **Cloner le dépôt** (ou copier les fichiers).
2.  **Lancer le conteneur** avec Docker Compose :
    ```bash
    docker-compose up --build
    ```
3.  **Vérifier les résultats** :
    *   Le conteneur va s'exécuter et afficher les logs de `app.py` et `test_client.py`.
    *   Un fichier `data/test_volume.txt` sera créé/incrémenté sur votre machine hôte pour confirmer le montage du volume.

## Configuration Docker

Le conteneur est configuré pour communiquer avec Ollama sur l'hôte via l'adresse :
`http://host.docker.internal:11434`

## Outils du Serveur MCP

Le serveur expose trois outils principaux :
1.  `lister_fichiers` : Liste les fichiers d'un répertoire.
2.  `lire_fichier` : Lit le contenu d'un fichier.
3.  `analyser_fichier_ia` : Analyse le contenu d'un fichier en utilisant un prompt et le modèle IA via Ollama.
