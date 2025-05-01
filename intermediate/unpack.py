"""
`foo` expects two keyword arguments - `name` of type `str`, and `age` of type `int`.
"""

from typing import Unpack, TypedDict


class Person(TypedDict):
    name: str
    age: int


def foo(**kwargs: Unpack[Person]):
    pass


person: Person = {"name": "The Meaning of Life", "age": 1983}
foo(**person)
# foo(**{"name": "Brian", "age": 30})
# foo(**{"name": "Brian"})  # error
person2: dict[str, object] = {"name": "Brian", "age": 20}
# foo(**person2)  # error
# foo(**{"name": "Brian", "age": "1979"})  # error
