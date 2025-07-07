from rich.console import Console

console = Console()

def show_tips():
    tips = [
        "- Activez un pare-feu avec règles strictes",
        "- Utilisez Cloudflare ou un reverse proxy",
        "- Bloquez les IPs suspectes (fail2ban, iptables)",
        "- Surveillez le trafic avec netstat ou Wireshark",
        "- Désactivez les ports inutiles"
    ]
    console.print("[bold blue]Anti-DDOS - Conseils[/bold blue]")
    for tip in tips:
        console.print(f"[green]✓ {tip}[/green]")

if __name__ == "__main__":
    show_tips()
