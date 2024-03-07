from typing import List
from vbl_json_schema import *
from vbl_json_schema.models import *

def generate_csharp_struct(class_name: str, fields: List[str]) -> str:
    field_declarations = "\n".join(f"    public {field};" for field in fields)
    constructor_parameters = ", ".join(f"{field} {field.lower()}" for field in fields)
    assignments = "\n".join(f"        this.{field} = {field.lower()};" for field in fields)
    
    return f"""
using UnityEngine;
    
public struct {class_name}
{{
{field_declarations}
}}
"""

def pydantic_to_csharp(pydantic_class):
    class_name = pydantic_class.__name__

    fields = []
    for name, data in pydantic_class.model_fields.items():

        field_data = f'{data.annotation.__name__} {name}'

        fields.append(field_data)

    return generate_csharp_struct(class_name, fields)

if __name__ == "__main__":
    with open(f'./src/vbl_json_schema/csharp/{Vector3Data.__name__}.cs', 'w') as f:
        f.write(pydantic_to_csharp(Vector3Data))