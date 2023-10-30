#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib  # Import hashlib to perform MD5 hashing


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

        # Check if 'password' is provided in kwargs
        if "password" in kwargs:
            # Hash the password to an MD5 value
            self.password = hashlib.md5(kwargs["password"].encode()) \
                            .hexdigest()

    def to_dict(self, exclude=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()

        # List of keys to exclude by default
        default_exclude = ["password"]

        # If 'exclude' is provided, append it to the default exclusion list
        if exclude:
            default_exclude.extend(exclude)

        # Remove the specified keys from the dictionary
        for key in default_exclude:
            if key in new_dict:
                del new_dict[key]

        return new_dict
