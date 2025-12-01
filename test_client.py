import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run():
    print("Connexion")

    server_params = StdioServerParameters(
        command="python",
        args=["mon_serveur_mcp.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # Test 1 : Lister les fichiers
            print("\n COMMANDE 1 : Lister les fichiers du projet")
            resultat = await session.call_tool("lister_fichiers", arguments={"dossier": "."})
            print(f"Réponse :\n{resultat.content[0].text}")

            # Test 2 : Lire un fichier existant
            fichier_a_lire = "mon_serveur_mcp.py"
            print(f"\n COMMANDE 2 : Lire le contenu de {fichier_a_lire}")
            
            lecture = await session.call_tool("lire_fichier", arguments={"nom_fichier": fichier_a_lire})
              
            apercu = lecture.content[0].text[:100]
            print(f"Aperçu du fichier :\n{apercu}...")

if __name__ == "__main__":
    asyncio.run(run())
