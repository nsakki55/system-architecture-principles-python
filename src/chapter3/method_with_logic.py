from dataclasses import dataclass


@dataclass(frozen=True)
class PersonName:
    first_name: str
    last_name: str

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


if __name__ == "__main__":
    person_name = PersonName("Yamada", "Taro")
    print(person_name.full_name)
