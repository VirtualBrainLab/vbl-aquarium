from pydantic import BaseModel
from vbl_json_schema.models_unity import *

class IDData(BaseModel):
    id: str

class Vector3Data(BaseModel):
    id: str
    value: Vector3

class ColorData(BaseModel):
    id: str
    value: Color

class StringData(BaseModel):
    id: str
    value: str

class FloatData(BaseModel):
    id: str
    value: float

class IntData(BaseModel):
    id: str
    value: int

class BoolData(BaseModel):
    id: str
    value: bool