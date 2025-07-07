import os
import sys
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
import webbrowser

console = Console()

def search_google(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    console.print(f"[cyan]🔎 Ouverture de Google avec la recherche :[/cyan] [bold green]{query}[/bold green]")
    webbrowser.open(url)

def search_duckduckgo(query):
    url = f"https://duckduckgo.com/?q={query.replace(' ', '+')}"
    console.print(f"[cyan]🔎 Ouverture de DuckDuckGo avec la recherche :[/cyan] [bold green]{query}[/bold green]")
    webbrowser.open(url)

def main():
    console.print(Panel("[bold blue]MODULE SEARCHER[/bold blue]\nEffectuez une recherche rapide sur Google ou DuckDuckGo", title="🔍 Searcher", border_style="blue"))
    
    query = Prompt.ask("[yellow]Entrez le terme à rechercher[/yellow]")
    
    engine = Prompt.ask("[green]Choisissez le moteur de recherche[/green] (g = Google / d = DuckDuckGo)", choices=["g", "d"], default="g")

    if engine == "g":
        search_google(query)
    else:
        search_duckduckgo(query)

    console.print("\n[bold green]✅ Recherche terminée. Le navigateur a été ouvert.[/bold green]\n")

if __name__ == "__main__":
    main()
