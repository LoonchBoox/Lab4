from pydantic import BaseModel

class FullSpell(BaseModel):
    name: str

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