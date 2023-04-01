from pydantic import BaseModel
import datetime
from pathlib import Path
import json
from typing import ClassVar



test_input = {'date':datetime.date.today(), 'question': 'Am I pretty?', 'answer':'No!'}

class Query(BaseModel):
    date: datetime.date
    question: str
    answer: str


class History(BaseModel):
    questions: list[Query|None] = []
    year: ClassVar[int] = datetime.date.today().year
    folder: ClassVar[Path] = Path('/Users/evan/Development/Projects/augur/augur/_history')

    def to_json_file(self):
        file = History.folder / f"{History.year}.json"
        file.write_text(self.json(indent=4))

    @classmethod
    def from_json_file(cls):
        file = History.folder / f"{cls.year}.json"
        return cls.parse_file(file)
    
    def append(self, input):
        self.questions.append(input)



"""
from augur import remember
q = remember.Query(**remember.test_input)
hist = remember.History()
hist.questions.append(q)
"""