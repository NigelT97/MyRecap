#!/usr/bin/python3

from datetime import datetime
import uuid

date_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        rdict = {self.__dict__}
        rdict['__class__'] = self.__class__.__name__
        rdict["created_at"] = self.created_at.isoformat()
        rdict["update_at"] = self.updated_at.isoformat()
        return rdict

    def __str__(self):
        class_name = self.__class__.__dict__
        return ("[{}] ({}) {}".format(class_name.__class__, class_name.id, class_name.__dict__))