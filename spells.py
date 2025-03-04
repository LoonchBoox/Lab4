from pydantic import BaseModel
from typing import Optional

class FullSpell(BaseModel):
    index: str
    name: str
    desc: list[str]
    higher_level: list[str]
    range: str
    concentration: bool
    casting_time: str
    level: int

    def __repr__(self):
        return f"{self.name}\n{self.desc}\n{self.higher_level}\nrange:{self.range}\nconcentration:{self.concentration}\ncasting time:{self.casting_time}"
    
    def printBasic(self):
        return f"{self.name} - {self.level}"

class SmallSpell(BaseModel):
    index: str
    name: str
    level: int
    url: str

    def __repr__(self):
        return f"{self.name} - level {self.level}"
    
class AllSpells(BaseModel):
    count: int
    results: list[SmallSpell]