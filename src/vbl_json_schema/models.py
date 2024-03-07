from pydantic import BaseModel


class Vector3(BaseModel):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


class Vector3Data(BaseModel):
    id: int
    value: Vector3


with open("./schemas/vector3.json", "w") as f:
    f.write(str(Vector3.model_json_schema()))
