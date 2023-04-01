from rich.console import Console
from rich.theme import Theme

colors = {
    'burning_fireflies' : '#ff166c'
}

emojis = {
    '8ball': '🎱',
    'crystal': '🔮',
}

augur_theme = Theme({
    'icon': f'bold {colors["burning_fireflies"]} reverse',
    'header': f'bold {colors["burning_fireflies"]}'
})

console = Console(theme=augur_theme)

icons = { 
    'text': "[icon] augur :[/icon]",
    '8ball': f"{emojis['8ball']}[header] : [/header]",
    'crystal': f"{emojis['crystal']}[header] : [/header]",
}


print = console.print
