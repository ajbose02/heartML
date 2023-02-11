from django.db import models

# Create your models here.
class Person(): 
    def __init__(self, values):
        self.values = values
        self.array = values[0]

    def getArray(self):
        return self.values