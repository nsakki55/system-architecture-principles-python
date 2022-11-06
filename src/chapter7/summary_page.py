from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Title:
    value: str


@dataclass(frozen=True)
class Price:
    value: int


@dataclass(frozen=True)
class LocalDate:
    value: datetime


@dataclass(frozen=True)
class Author:
    value: str


@dataclass(frozen=True)
class BookType:
    value: str


@dataclass(frozen=True)
class BookSummary:
    title: Title
    unit_price: Price
    published: LocalDate

    author: Author
    type: BookType
