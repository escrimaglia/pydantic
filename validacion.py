from pydantic import BaseModel, ValidationError, Field
import json
from pprint import pprint
import yaml

class Interfaces(BaseModel):
    nombre: str
    tipo: str | None = "gigabit"
    slot: int = Field(gt=0, lt=2)
    port: int = Field(gt=0, lt=3)

class Device(BaseModel):
    nombre: str
    familia: str
    memoria: int = Field(gt=2000, lt=8000)
    interfaces: list[Interfaces]

# Lectura modelo yaml
with open("modelo.yaml", "r") as file:
    data = yaml.safe_load(file.read())

data_json = json.dumps(data, indent=2)

print ("A validar:")
print (data_json)

# Validación from Json
try:
    dev = Device.model_validate_json(data_json)
    print ("Validacion:")
    print (dev)
except ValidationError as err:
    print (err)

# Json Schema clase Device
json_schema = Device.model_json_schema()
pprint (json_schema)