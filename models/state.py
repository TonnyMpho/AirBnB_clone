#!/usr/bin/python3
"""Definition of the State Class."""
from models.base_model import BaseModel


class State(BaseModel):
    """This represents a state.

    Attributes:
        name (str): the name of the state.
    """

    name = ""
