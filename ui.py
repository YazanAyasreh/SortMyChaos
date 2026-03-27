from rich.table import Table
from rich.panel import Panel
from rich.console import Console

console = Console()

def create_summary_table(files_info):
    table = Table(title="File Organization Summary")
    table.add_column("Category", style="cyan", no_wrap=True)
    table.add_column("Count", style="magenta", justify="right")
    table.add_column("Total Size (MB)", style="green", justify="right")
    for cat, info in files_info.items():
        table.add_row(cat, str(info['count']), f"{info['size']:.2f}")
    return table

def create_status_panel(status):
    return Panel(status, title="System Status", border_style="blue")