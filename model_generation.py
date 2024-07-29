from pydantic import ValidationError, TypeAdapter
import json
from ruamel.yaml import YAML
from datos_instancia_modelo import datos_instancia
from clases_modelo import *

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

# Validacion del modelo y creacion del modelo de datos
try:
    modelo = DataModel.model_validate(datos_instancia)
    json_file = modelo.model_dump_json(indent=2)
    file_json(json_file)
    file_yaml(json_file)
except ValidationError as err:
    print (err)

# Creacion del json schema 
type_adapter = TypeAdapter(DataModel)
with open("json_schema.json", "w") as file:
    file.write(json.dumps(type_adapter.json_schema(), indent=2))
