from models_base import *
from models_generic import *
from models_urchin import *

from generate_cs import *

classes_list = [Vector3Data, ]

for cclass in classes_list:
    with open(f"./schemas/{cclass.__name__}.json", "w") as f:
        f.write(dumps(cclass.model_json_schema()))

    with open(f'./csharp/{cclass.__name__}.cs', 'w') as f:
        f.write(pydantic_to_csharp(cclass))