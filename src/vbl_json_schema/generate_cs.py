from vbl_json_schema import *
from vbl_json_schema.models_urchin import *

import typing
import inspect

p2c_types = {
    'str': 'string',
}

def generate_csharp_struct(class_name: str, fields: List[str], enums = None):
    field_declarations = "\n".join(f"    public {field};" for field in fields)

    enum_str = ""
    if enums is not None:
        enum_array = ["\n".join(f"    {v[0]} = {v[1]}," for v in enums[1])]
        enum_str = f"""
\n\npublic Enum {enums[0]}
{enum_array}
"""

    return f"""
using UnityEngine;
    
public struct {class_name}
{{
{field_declarations}
}}{enum_str}
"""

def pydantic_to_csharp(pydantic_class):
    class_name = pydantic_class.__name__

    fields = []
    for name, data in pydantic_class.model_fields.items():
        field_data = ''
        enums = None # when enums are active this should be a tuple (ClassName, [(Option1, Value1), (Option2, Value2)])

        # first, catch enums
        if 'enum' in str(data.annotation):
            print(pydantic_class.field_definitions)

        # next, deal with base classes
        elif hasattr(data.annotation, "__name__"):
            # convert str -> string properly
            type_name = data.annotation.__name__

            if type_name in p2c_types.keys():
                type_name = p2c_types[type_name]

            field_data = f'{type_name} {name}'

        # finally, deal with arrays
        elif typing.get_origin(data.annotation) == list:
            arg_class = typing.get_args(data.annotation)
            if hasattr(arg_class[0], "__name__"):
                field_data = f'{arg_class[0].__name__}[] {name}'
            else:
                print(arg_class[0])

        else:
            raise Exception("need to write a new parser for a missing type")

        fields.append(field_data)

    return generate_csharp_struct(class_name, fields, enums)