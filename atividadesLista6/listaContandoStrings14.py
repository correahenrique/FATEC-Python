"""Crie uma lista com 5 strings e conte quantas começam com a letra 'A'."""
from turtledemo.penrose import start

listas = [
    "String 1",
    "String 2",
    "A String 3",
    "A String 4",
    "A string 5"
]
count1 = 0
for i in listas:
    if i.lower().startswith("a"):
        count1 += 1
print(f"Teve {count1} Strings que comaçaram com A")