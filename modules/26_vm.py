import sys
import subprocess

# --- Auto-installation ---
try:
    import psutil
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    import psutil

try:
    import platform
    import socket
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table

console = Console()

def get_system_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    os_name = platform.system()
    os_version = platform.version()
    architecture = platform.machine()
    cpu_count = psutil.cpu_count(logical=True)
    ram = round(psutil.virtual_memory().total / (1024**3), 2)

    return {
        "OS": f"{os_name} {os_version}",
        "Nom d'hôte": hostname,
        "Adresse IP locale": ip_address,
        "Architecture": architecture,
        "CPU (threads)": str(cpu_count),
        "RAM": f"{ram} GB"
    }

def show_vm_info():
    info = get_system_info()
    console.print(Panel("[bold cyan]🖥️ VM Info / Environnement local[/bold cyan]", border_style="blue"))

    table = Table(title="Données système détectées")
    table.add_column("Clé", style="magenta", no_wrap=True)
    table.add_column("Valeur", style="green")

    for key, value in info.items():
        table.add_row(key, value)

    console.print(table)

if __name__ == "__main__":
    show_vm_info()
