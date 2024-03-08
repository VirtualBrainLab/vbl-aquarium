from pydantic import BaseModel
from typing import List
from vbl_json_schema.models_unity import *

class IDData(BaseModel):
    id: str

class Vector3Data(BaseModel):
    id: str
    value: Vector3

class Vector3List(BaseModel):
    id: str
    value: List[Vector3]

class ColorData(BaseModel):
    id: str
    value: Color

class ColorList(BaseModel):
    id: str
    value: List[Color]

class StringData(BaseModel):
    id: str
    value: str

class StringList(BaseModel):
    id: str
    value: List[str]

class FloatData(BaseModel):
    id: str
    value: float

class FloatList(BaseModel):
    id: str
    value: List[float]

class IntData(BaseModel):
    id: str
    value: int

class IntList(BaseModel):
    id: str
    value: List[int]

class BoolData(BaseModel):
    id: str
    value: bool

class BoolList(BaseModel):
    id: str
    value: List[bool]