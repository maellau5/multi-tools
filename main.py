import os
import subprocess
import sys

# --- Vérifie et installe 'rich' si nécessaire ---
try:
    from rich.console import Console
    from rich.prompt import Prompt
    from rich.panel import Panel
    from rich.columns import Columns
    from rich.table import Table
    from rich.text import Text
except ImportError:
    print("[!] 'rich' non trouvé. Installation en cours...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    # Recharge après installation
    from rich.console import Console
    from rich.prompt import Prompt
    from rich.panel import Panel
    from rich.columns import Columns
    from rich.table import Table
    from rich.text import Text

# --- Interface et menus ---
console = Console()

logo = Text()
logo.append("Maellau Tool\n", style="bold blue")
logo.append("Bonjour Invité\n", style="italic cyan")
console.print(Panel(logo, border_style="blue"))

menus = [
    ["[01] Searcher", "[02] DNS Jumper", "[03] Anti DDOS", "[04] Grabber Builder", "[05] Web Builder", "[06] USB Grabber Builder"],
    ["[07] QR Grabber", "[08] EXE Builder", "[09] SSH Brute Forcing", "[10] WiFi Brute Forcing", "[11] Port Scanner", "[12] IP Scanner"],
    ["[13] ID Scanner", "[14] Token Scanner", "[15] HTML Scanner", "[16] Port Generator", "[17] IP Generator", "[18] Password Generator"],
    ["[19] ID Generator", "[20] Nitro Generator", "[21] VM", "[22] DDOS Starter", "[23] Cam Grabber", "[24] Destock Message"],
    ["[25] Hard Doxing", "[26] Raid Discord", "[27] HTML Injection", "[28] DOX Channel", "[29] License", "[30] Exit"]
]

columns = []
for idx, menu in enumerate(menus, start=1):
    table = Table(show_header=False, expand=True, box=None)
    for item in menu:
        table.add_row(f"[cyan]{item}[/cyan]")
    columns.append(Panel(table, title=f"[bold magenta]Menu {idx}[/bold magenta]", border_style="magenta"))

console.print(Columns(columns, equal=True))

info = Table(show_header=False, box=None)
info.add_row("[bold green]Author[/bold green]: Maellau")
info.add_row("[bold green]Version[/bold green]: 3.0")
info.add_row("[bold green]Langage[/bold green]: Python")
info.add_row("[bold green]Type[/bold green]: Privé")
info.add_row("[bold green]Copyright[/bold green]: No")
info.add_row("[bold green]Lignes de code[/bold green]: ???")
console.print(Panel(info, title="[bold yellow]Informations[/bold yellow]", border_style="yellow"), justify="center")

# --- Interaction ---
while True:
    choice = Prompt.ask("\n[bold blue]@root[/bold blue] [Lettre + Score] — [bold cyan]V3[/bold cyan]\n[bold magenta]» Choix du numéro[/bold magenta]")

    if not choice.isdigit():
        console.print("[red]Erreur : Veuillez entrer un numéro valide.[/red]")
        continue

    if choice == "30":
        console.print("[green]Fermeture de l'outil...[/green]")
        break

    folder = "modules"
    if not os.path.isdir(folder):
        console.print(f"[red]Dossier '{folder}' introuvable. Créez-le et placez-y les modules.[/red]")
        break

    files = os.listdir(folder)
    match = next((f for f in files if f.startswith(f"{choice.zfill(2)}_") and f.endswith(".py")), None)

    if match:
        file_path = os.path.join(folder, match)
        console.print(f"[yellow]Exécution de {match}...[/yellow]")
        subprocess.run([sys.executable, file_path])
    else:
        console.print(f"[red]Aucun module trouvé pour l'option {choice}.[/red]")
