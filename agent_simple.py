import ollama

MODELE = "qwen2.5-coder:1.5b"

code_a_verifier = """
def calculer_moyenne(notes):
    somme = 0
    for note in notes:
        somme += note
    # Bug ici : si la liste est vide, on divise par 0 !
    return somme / len(notes)
"""

print(f"L'agent analyse le code avec {MODELE}...")

try:
    reponse = ollama.chat(model=MODELE, messages=[
    {
        'role': 'system',
        'content': 'Tu es un expert Senior en Python. Ta mission est de trouver les bugs de sécurité ou de logique.'
    },
    {
        'role': 'user',
        'content': f"Analyse ce code et explique le problème brièvement :\n{code_a_verifier}",
    },
    ])

    print("\n Analyse de l'IA")
    print(reponse['message']['content'])

except Exception as e:
    print(f"Erreur : Assure-toi que Ollama tourne bien en arrière-plan.\nDétail: {e}")



    