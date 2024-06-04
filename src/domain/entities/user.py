from dataclasses import dataclass, asdict
from typing import Dict

from src.domain.value_objects import UserId


@dataclass
class User:
    id: UserId
    first_name: str
    last_name: str
    email: str
    phone: str

    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        return cls(**data)

    def to_dict(self) -> Dict:
        return asdict(self)
