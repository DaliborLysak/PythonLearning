from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title="Data")

table.add_column("Id", justify="right", style="cyan")
table.add_column("Name", style="green", no_wrap=True)
table.add_column("Note", justify="left", style="yellow", no_wrap=True)

table.add_row("1", "John Doe", "Hello World")
table.add_row("2", "Jane Smith", "Good Bye World")

console.print(table)