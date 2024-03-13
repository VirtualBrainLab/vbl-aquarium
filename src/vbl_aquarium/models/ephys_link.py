from pydantic import BaseModel

from vbl_aquarium.models_unity import Vector4


class GotoPositionRequest(BaseModel):
    manipulator_id: str
    position: Vector4
    speed: float
