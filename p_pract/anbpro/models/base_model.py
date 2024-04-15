#!/usr/bin/python3

import models
from uuid import uuid4
from datetime import datetime


class Basemodel:
    def __init__(self, idx=0, created_at=0, updated_at=0):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        return_dict = self.__dict__.copy()
        return_dict["created_at"] = self.created_at.isoformat()
        return_dict["updated_at"] = self.updated_at.isoformat()
        return_dict["__class__"] = self.__class__.__name__
        return return_dict

    def __str__(self):
        class_name = self.__class__.__name__
        return (f"[{class_name} ({self.id}) {self.__dict__}")
        