from dataclasses import dataclass
import uuid


@dataclass
class Student:
    id: uuid.UUID
    name: str
    surname: str
    specialization: str

    def __iter__(self):
        prop_list = list()
        prop_list.append(("id", self.id))
        prop_list.append(("name", self.name))
        prop_list.append(("surname", self.surname))
        prop_list.append(("specialization", self.specialization))
        return iter(prop_list)
