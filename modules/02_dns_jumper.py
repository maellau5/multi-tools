import os
import platform
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def change_dns_windows():
    os.system('netsh interface ip set dns "Wi-Fi" static 8.8.8.8')
    os.system('netsh interface ip add dns "Wi-Fi" 8.8.4.4 index=2')
    console.print("[green]DNS modifié avec succès (Google DNS)[/green]")

def change_dns_linux():
    resolv_path = "/etc/resolv.conf"
    try:
        with open(resolv_path, "w") as file:
            file.write("nameserver 8.8.8.8\nnameserver 8.8.4.4\n")
        console.print(f"[green]DNS modifié dans {resolv_path}[/green]")
    except PermissionError:
        console.print("[red]Permission refusée. Lancez en tant que super utilisateur (sudo).[/red]")

def main():
    console.print("[bold cyan]Changer de DNS vers Google (8.8.8.8, 8.8.4.4)[/bold cyan]")
    confirm = Prompt.ask("Voulez-vous continuer ?", choices=["y", "n"], default="y")
    if confirm == "y":
        if platform.system() == "Windows":
            change_dns_windows()
        elif platform.system() == "Linux":
            change_dns_linux()
        else:
            console.print("[red]OS non supporté[/red]")

if __name__ == "__main__":
    main()
