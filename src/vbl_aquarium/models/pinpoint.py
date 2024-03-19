from vbl_aquarium.models.vbl_base_model import VBLBaseModel
from typing import List
from vbl_aquarium.unity import *

# CRANIOTOMY

class CraniotomyModel(VBLBaseModel):
    index: int
    size: Vector2
    position: Vector3
    rectangle: bool = False

class CraniotomyGroup(VBLBaseModel):
    atlas: str
    data: List[CraniotomyModel]