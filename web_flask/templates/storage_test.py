#!/usr/bin/python3

from models import storage
from models import State

a = storage.all(State).values()

for i in a:
    print(i.name)
    for j in i.cities:
        print(f"\t{j.name}")
