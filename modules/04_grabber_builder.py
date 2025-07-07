from rich.console import Console
import time

console = Console()

def fake_grabber():
    console.print("[yellow]Création d'un grabber (simulé)...[/yellow]")
    time.sleep(1)
    console.print("[green]Configuration sauvegardée[/green]")
    time.sleep(1)
    console.print("[cyan]Fichier prêt : fake_grabber.exe[/cyan]")

if __name__ == "__main__":
    fake_grabber()
