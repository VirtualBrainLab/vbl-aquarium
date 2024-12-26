from importlib import import_module
from pkgutil import iter_modules

for module in iter_modules(["models"]):
    print(module.name)
    import_module(f"vbl_aquarium.models.{module.name}")
