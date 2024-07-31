from pydantic import BaseModel, ValidationError, Field
import json
from pprint import pprint
import yaml
from clases_modelo import *

# Lectura modelo yaml
with open("config.yaml", "r") as file:
    data = yaml.safe_load(file.read())

# data_json = json.dumps(data, indent=2)

print ("A validar:")
print (data)

# Validación from Json
try:
    dev = DataModel.model_validate(data)
    print ("Validacion:")
    print (dev)
except ValidationError as err:
    print (err)
