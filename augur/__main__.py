import typer
from cli import console, icon, print
import resources
import random

app = typer.Typer()

@app.command()
def main(question: str):
    answers = resources.positive + resources.negative + resources.ambiguous
    resp = random.choice(answers)
    print(f'{icon}  {resp}')

if __name__ == '__main__':
    app()
