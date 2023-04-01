import typer
from formatting import console, icons, print
import random
from . import augur, remember

app = typer.Typer()

@app.command()
def main(question: str):
    answers = augur.positive + augur.negative + augur.ambiguous

    resp = random.choice(answers)
    hist = remember.History.from_json_file()
    print(f'{icons["8ball"]}  {resp}')

if __name__ == '__main__':
    app()
