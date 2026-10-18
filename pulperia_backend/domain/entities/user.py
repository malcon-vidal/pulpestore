from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int] = None
    name: str
    email: str
    password_hash: str
    role: str # "admin", "pulpero", "cliente"


    def is_admin(self) -> bool:
        return self.role == "admin"
    def is_pulpero(self) -> bool:
        return self.role == "pulpero"
    def is_cliente(self) -> bool:
        return self.role == "cliente"