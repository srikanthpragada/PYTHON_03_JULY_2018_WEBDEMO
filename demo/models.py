from django.db import models


# Create your models here.

class Info:
    def __init__(self):
        self.title = "Demo Application"
        self.version = "2.1"
        self.topics = ["Views", "Templates", "Forms" ,"ORM","Ajax","Rest API"]
