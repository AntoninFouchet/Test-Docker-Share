#!/bin/sh

# À l'intérieur du conteneur Linux.
echo Démarrage du conteneur (.sh)

echo vérifie les fichiers
ls -l mon_serveur_mcp.py

echo Lancement du Serveur MCP
# On lance le vrai programme
python mon_serveur_mcp.py

echo Conteneur lancé







