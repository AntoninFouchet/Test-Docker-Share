#!/bin/sh

# À l'intérieur du conteneur Linux.
echo "Démarrage du conteneur (.sh)"

echo "vérifie les fichiers"
ls -l mon_serveur_mcp.py

# On lance le test des volumes
echo "Lancement du test des volumes"
python app.py

# On lance le test_client.py
echo "Lancement du test_client.py"
python test_client.py

echo "Conteneur terminé"





