"""
This module implements specialized container datatypes, providing alternatives to Python's general
purpose built-in
"""

from collections import namedtuple

FullName = namedtuple("FullName", ("first", "middle", "last"))

my_name = FullName("Barney", "The", "Dinosour")

print(my_name[0])
print(my_name.first)