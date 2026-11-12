from dataclasses import dataclass

#Models : This represents our todo data structure.

@dataclass
class Todo:
    id: int
    title: str
    description: str