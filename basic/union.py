"""
foo should accept a argument that's either a string or integer.
"""


def foo(x: int | str):
    pass


foo("foo")
foo(1)
# foo([]) # error
