import os
import sys
import time
from datetime import datetime
import torch
from diffusers import DiffusionPipeline
from PIL import Image

os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

# Funktion zur Bildgenerierung
def generate_image(prompt):
    # Verwendet CPU wenn GPU nicht vorhanden
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Lade das Stable Diffusion Modell
    print("\nLade das Stable Diffusion Modell...")
    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1-base").to(device)

    # Bild generieren
    print("Generiere das Bild...")
    image = pipe(prompt).images[0]

    # Eindeutigen Dateinamen erstellen
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_image_{timestamp}.png"
    
    image.save(filename)  # Speichern als PNG
    print(f"\nBild erfolgreich gespeichert: {filename}")

    # Versuche, das Bild mit dem Standardbildbetrachter zu öffnen
    try:
        image.show()
    except Exception as e:
        print(f"Fehler beim Öffnen des Bildes: {e}")
        print("Versuche, das Bild im Terminal anzuzeigen...")

        # Versuche w3m oder cacaview zu verwenden
        if os.system("command -v w3m > /dev/null") == 0:
            os.system(f"w3m {filename}")
        elif os.system("command -v cacaview > /dev/null") == 0:
            os.system(f"cacaview {filename}")
        else:
            print("Kein unterstützter Bildbetrachter gefunden!")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == "__main__":
    
    while True:
        clear_screen()
        print("Willkommen zum Bildgenerierungsprogramm mit Stable Diffusion!\n")
        prompt = input("Bitte geben Sie Ihren Prompt ein (oder 'exit' zum Beenden): ")  # Eingabeaufforderung für den Benutzer

        if prompt.strip().lower() == 'exit':
            print("Programm wird beendet...")
            breakf

        if prompt.strip():
            generate_image(prompt)
        else:
            print("Fehler: Der Prompt darf nicht leer sein!")

        input("\nDrücke Enter, um fortzufahren...")