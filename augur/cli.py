from rich.console import Console
from rich.theme import Theme

colors = {
    'burning_fireflies' : '#ff166c'
}


augur_theme = Theme({
    'icon': f'bold {colors["burning_fireflies"]} reverse'
})

console = Console(theme=augur_theme)

icon = "[icon] augur :[/icon]"

print = console.print
