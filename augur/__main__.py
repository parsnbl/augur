import typer
from cli import console, icon, print
import augur
import random

app = typer.Typer()

@app.command()
def main(question: str):
    answers = augur.positive + augur.negative + augur.ambiguous
    resp = random.choice(answers)
    print(f'{icon}  {resp}')

if __name__ == '__main__':
    app()
