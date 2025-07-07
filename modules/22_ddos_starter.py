import sys
import subprocess

# --- Vérifie si 'requests' est installé, sinon installe-le ---
try:
    import requests
except ImportError:
    print("[!] 'requests' n'est pas installé. Installation en cours...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

from rich.prompt import Prompt
from rich.console import Console

console = Console()

def ddos_simulator(url, count):
    console.print(f"[cyan]Envoi de {count} requêtes GET vers {url}[/cyan]")
    for i in range(int(count)):
        try:
            response = requests.get(url)
            console.print(f"[green]✓ Requête {i+1} envoyée — Code: {response.status_code}[/green]")
        except Exception as e:
            console.print(f"[red]Erreur lors de la requête {i+1} : {e}[/red]")

if __name__ == "__main__":
    target = Prompt.ask("URL cible (https://...)")
    number = Prompt.ask("Nombre de requêtes à envoyer", default="10")
    ddos_simulator(target, number)
