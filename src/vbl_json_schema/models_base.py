from pydantic import BaseModel, Field, confloat

class Color(BaseModel):
    r: confloat(ge=0, le=255)
    g: confloat(ge=0, le=255)
    b: confloat(ge=0, le=255)
    a: confloat(ge=0, le=255) = 255

class Vector3(BaseModel):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
