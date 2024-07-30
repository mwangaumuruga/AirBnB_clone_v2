#!/usr/bin/python3
"""This is the state class"""
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
    else:
        @property
        def cities(self):
            """

            """
            import models
            from models.city import City
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
                  return city_list   
                   
                
