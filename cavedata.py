from typing import List
from dataclasses import dataclass
import json
from random import choices


@dataclass
class Reward:
    cash: int
    item: str


@dataclass
class Cave:
    gifLink: str
    weight: int
    reward: Reward


@dataclass
class Caves:
    list: List[Cave]

    def random(self) -> Cave:
        weights = map(lambda c: c.weight, list)
        choices(list, weights=weights)
        return choices[0]


def load_cave_data():
    data = open('data.json')
    jsonData = json.load(data)
    return Caves(**jsonData)
