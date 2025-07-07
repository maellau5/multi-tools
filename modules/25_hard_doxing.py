import sys
import subprocess

# --- Installation auto des dépendances ---
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.prompt import Prompt
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.prompt import Prompt

console = Console()

def get_email_info(email):
    url = f"https://emailrep.io/{email}"
    headers = {
        "User-Agent": "BatmanToolV3-HardDoxing/1.0",
        # "Key": "VOTRE_CLÉ_API"  # facultatif pour usage pro, sinon limité à 15 req/j
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data
    except Exception as e:
        console.print(f"[red]Erreur : {e}[/red]")
        return None

def display_info(data, email):
    console.print(Panel(f"[bold cyan]Résultats OSINT pour :[/bold cyan] {email}", title="📧 EmailRep.io", border_style="blue"))

    table = Table(title="Analyse de réputation")
    table.add_column("Champ", style="magenta", no_wrap=True)
    table.add_column("Valeur", style="green")

    table.add_row("Reputation", data.get("reputation", "N/A"))
    table.add_row("Suspicious", str(data.get("suspicious", "N/A")))
    table.add_row("Blacklisted", str(data.get("blacklisted", "N/A")))
    table.add_row("Domain", data.get("details", {}).get("domain_exists", "N/A"))
    table.add_row("Deliverable", str(data.get("details", {}).get("deliverable", "N/A")))
    table.add_row("Valid MX", str(data.get("details", {}).get("valid_mx", "N/A")))
    table.add_row("Seen On Breach", str(data.get("details", {}).get("credentials_leaked", "N/A")))

    console.print(table)

    socials = data.get("profiles", [])
    if socials:
        social_str = "\n".join(f"- {site}" for site in socials)
        console.print(Panel(social_str, title="🔗 Profils détectés", border_style="green"))
    else:
        console.print(Panel("Aucun profil social détecté.", border_style="grey37"))

def main():
    console.print(Panel("[bold red]MODULE HARD DOXING (ÉTHIQUE)[/bold red]\nAnalyse publique d'une adresse e-mail via EmailRep.io", title="🛡️ OSINT API", border_style="red"))
    email = Prompt.ask("Entrez une adresse email à analyser")
    result = get_email_info(email)

    if result and "error" not in result:
        display_info(result, email)
    else:
        console.print("[bold red]❌ Aucune donnée trouvée ou erreur avec l'email.[/bold red]")

if __name__ == "__main__":
    main()
