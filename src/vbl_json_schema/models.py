from json import loads, dumps

from jsonschema import validate
from pydantic import BaseModel
from requests import get


class Vector3(BaseModel):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


class Vector3Data(BaseModel):
    id: int
    value: Vector3


with open("./schemas/vector3.json", "w") as f:
    f.write(dumps(Vector3.model_json_schema()))

online_schema = get(
    "https://raw.githubusercontent.com/VirtualBrainLab/vbl-json-schema/pydantic/src/vbl_json_schema/schemas/vector3.json")
print(online_schema.text)
as_dict = loads(online_schema.text)

print(validate(instance={"id": 1, "value": {"x": 1.0, "y": 2.0, "z": 3.0}},
               schema=as_dict))
