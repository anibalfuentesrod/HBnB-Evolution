#!/usr/bin/python3
import uuid

class Country:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
