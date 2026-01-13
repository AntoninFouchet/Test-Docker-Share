import os
from mcp.server.fastmcp import FastMCP
from ollama import Client

mcp = FastMCP("serveur Stage")
MODELE_IA = "qwen2.5-coder:1.5b"

# Pointe vers hôte Windows
client = Client(host='http://host.docker.internal:11434')

# OUTIL 1 : Lister les fichiers
@mcp.tool()
def lister_fichiers(dossier: str = ".") -> str:
    """
    Liste tous les fichiers et dossiers dans le répertoire donné.
    Utilisé pour explorer la structure du projet.
    Args:
        dossier: Le chemin à explorer (par défaut le dossier courant)
    """
    try:
        fichiers = os.listdir(dossier)
        return "Fichiers trouvés :\n- " + "\n- ".join(fichiers)
    except Exception as e:
        return f"Erreur lors de la lecture du dossier : {str(e)}"

# OUTIL 2 : Lire un fichier
@mcp.tool()
def lire_fichier(nom_fichier: str) -> str:
    """Lit le contenu d'un fichier spécifique."""
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Impossible de lire le fichier {nom_fichier} : {str(e)}"
# OUTIL 3 : Analyser un fichier avec l'IA
@mcp.tool()
def analyser_fichier_ia(nom_fichier: str, question: str) -> str:
    contenu = lire_fichier(nom_fichier)

    prompt = f"""
    Voici le contenu du fichier '{nom_fichier}' :
    ```
    {contenu}
    ```
    Consigne de l'utilisateur : {question}
    """
    try:
        reponse = client.chat(model=MODELE_IA, messages=[
            {'role': 'user', 'content': prompt}
        ])
        return reponse['message']['content']
    except Exception as e:
        return f"Erreur de communication avec l'IA"


if __name__ == "__main__":
    mcp.run()