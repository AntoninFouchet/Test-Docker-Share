import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ServeurStage_Git")

# OUTIL 1 : Lister les fichiers (Simulation Git)
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

if __name__ == "__main__":
    mcp.run()

    