from pydantic import BaseModel, ValidationError, Field
import json
from ruamel.yaml import YAML

class Interfaces(BaseModel):
    nombre: str
    tipo: str | None  = "gigabit"
    slot: int = Field(gt=0, lt=2) 
    port: int = Field(gt=0, lt=3)

class Device(BaseModel):
    nombre: str
    familia: str
    memoria: int = Field(gt=2000, lt=8000) 
    interfaces: list[Interfaces]

# Funciones para generar archivos json y yaml
def file_json(_json):
    with open("config.json", "w") as file:
        file.write(_json)

def file_yaml(_json):
    yaml = YAML(typ="safe", pure=True)
    yaml.default_flow_style = False
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.sort_base_mapping_type_on_output = False
    with open("config.yaml", "w") as file:
        yaml.dump(yaml.load(_json), file)

# Generación del modelo de datos from instancia
datos_instancia = {
    'nombre': 'None',
    'familia': 'None',
    'memoria': 2024,
    'interfaces': [
        {
            'nombre': 'None',
            'slot': 1,
            'port': 1
        },
        {
            'nombre': 'None',
            'slot': 1,
            'port': 2
        }
    ]
}
try:
    dev = Device.model_validate(datos_instancia)
    json = dev.model_dump_json(indent=2)
    file_json(json)
    file_yaml(json)
except ValidationError as err:
    print (err)

