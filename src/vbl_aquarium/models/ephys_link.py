from pydantic import BaseModel

from vbl_aquarium.models_unity import Vector4


class GotoPositionRequest(BaseModel):
    """Data format for requesting a manipulator to move to a position.
    
    :param manipulator_id: ID of the manipulator to move.
    :type manipulator_id: str
    :param position: Position to move to in mm (X, Y, Z, W).
    :type position: Vector4
    :param speed: Speed to move at in mm/s.
    :type speed: float
    """
    manipulator_id: str
    position: Vector4
    speed: float
