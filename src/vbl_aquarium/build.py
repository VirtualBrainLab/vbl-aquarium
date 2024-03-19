import vbl_aquarium.unity as unity
from vbl_aquarium.models import generic
from vbl_aquarium.models import urchin
from vbl_aquarium.models import logging
from vbl_aquarium.models import pinpoint
from vbl_aquarium.models import ephys_link
from vbl_aquarium.models import dock

from vbl_aquarium.models.vbl_base_model import VBLBaseModel

from generate_cs import *

import json
import os

def get_classes(module):
    # Get a list of all attributes in the module
    attributes = dir(module)
    # Filter out classes
    classes = [getattr(module, attr) for attr in attributes if isinstance(getattr(module, attr), type)]
    return classes

def remove_ignored_classes(module):
    return [c for c in get_classes(module) if c not in ignored_classes]

ignored_classes = get_classes(unity)
ignored_classes.append(VBLBaseModel)
unity_class_names = [x.__name__ for x in get_classes(unity)]

module_list = [generic, urchin, logging, pinpoint, ephys_link, dock]
folder_prefix = ['generic', 'urchin', 'logging', 'pinpoint', 'ephys_link', 'dock']


cdir = os.path.dirname(os.path.abspath(__file__))

for i, (module, cfolder) in enumerate(zip(module_list, folder_prefix)):
    classes = remove_ignored_classes(module)
    
    for cclass in classes:
        
        if not cclass.__name__ in unity_class_names:

            path = f"{cdir}/../../models/schemas/{cfolder}"
            if not os.path.exists(path):
                    os.makedirs(path)

            with open(f"{path}/{cclass.__name__}.json", "w") as f:
                f.write(json.dumps(cclass.model_json_schema()))

            path = f"{cdir}/../../models/csharp/{cfolder}"
            if not os.path.exists(path):
                    os.makedirs(path)

            with open(f'{path}/{cclass.__name__}.cs', 'w') as f:
                f.write(pydantic_to_csharp(cclass, cclass.model_json_schema()))