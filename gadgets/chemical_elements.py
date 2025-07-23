from chempy.util import periodic
from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title="Chemical Elements")

table.add_column("Nam", justify="right", style="cyan")
table.add_column("Symbol", style="green", no_wrap=True)
table.add_column("Relative Atomic Mass", justify="left", style="yellow", no_wrap=True)

for i in range(len(periodic.names)):
    table.add_row(periodic.names[i],
                  periodic.symbols[i],
                  str(periodic.relative_atomic_masses[i]))

console.print(table)