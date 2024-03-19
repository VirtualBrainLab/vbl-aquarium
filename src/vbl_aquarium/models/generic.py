from vbl_aquarium.models.vbl_base_model import VBLBaseModel
from typing import List
from vbl_aquarium.unity import *

# Standard types and lists
class IDData(VBLBaseModel):
    id: str = Field(..., alias='ID')

class Vector3Data(VBLBaseModel):
    id: str = Field(..., alias='ID')
    value: Vector3

class Vector3List(VBLBaseModel):
    id: str = Field(..., alias='ID')
    values: List[Vector3]

class ColorData(VBLBaseModel):
    id: str = Field(..., alias='ID')
    value: Color

class ColorList(VBLBaseModel):
    id: str = Field(..., alias='ID')
    values: List[Color]

class StringData(VBLBaseModel):
    id: str = Field(..., alias='ID')
    value: str

class StringList(VBLBaseModel):
    id: str = Field(..., alias='ID')
    values: List[str]

class FloatData(VBLBaseModel):
    id: str = Field(..., alias='ID')
    value: float

class FloatList(VBLBaseModel):
    id: str = Field(..., alias='ID')
    values: List[float]

class IntData(VBLBaseModel):
    id: str = Field(..., alias='ID')
    value: int

class IntList(VBLBaseModel):
    id: str = Field(..., alias='ID')
    values: List[int]

class BoolData(VBLBaseModel):
    id: str = Field(..., alias='ID')
    value: bool

class BoolList(VBLBaseModel):
    id: str = Field(..., alias='ID')
    values: List[bool]

# ID lists 
    
class IDList(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')

class IDListVector3Data(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')
    value: Vector3

class IDListVector3List(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')
    values: List[Vector3]

class IDListColorData(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')
    value: Color

class IDListColorList(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')
    values: List[Color]

class IDListStringData(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')
    value: str

class IDListStringList(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')
    values: List[str]

class IDListFloatData(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')
    value: float

class IDListFloatList(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')
    values: List[float]

class IDListIntData(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')
    value: int

class IDListIntList(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')
    values: List[int]

class IDListBoolData(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')
    value: bool

class IDListBoolList(VBLBaseModel):
    ids: List[str] = Field(..., alias='IDs')
    values: List[bool]