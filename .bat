@echo off

echo .bat donne la consigne de démarrer le conteneur au .sh

echo Construction de l'image Docker
docker build -t test-docker-share .

echo Lancement du conteneur
docker run test-docker-share
echo .sh éxecuté

pause



