from pydantic import BaseModel
from models_base import *

class Vector3Data(BaseModel):
    id: int
    value: Vector3