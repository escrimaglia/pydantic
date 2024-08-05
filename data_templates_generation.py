# By Ed Scrimaglia

from pydantic import ValidationError, TypeAdapter
import json
from ruamel.yaml import YAML
from data_test_modelo import datos_instancia
from data_model import *

# Json file generation
def file_json(_json: json) -> None:
    with open("config.json", "w") as file:
        file.write(_json)

# Yaml file generation
def file_yaml(_yaml: json) -> None:
    yaml = YAML(typ="safe", pure=True)
    yaml.default_flow_style = False
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.sort_base_mapping_type_on_output = False
    with open("config.yaml", "w") as file:
        yaml.dump(yaml.load(_yaml), file)


# Model Validation from data_test
try:
    modelo = DataModel.model_validate(datos_instancia)
    json_file = modelo.model_dump_json(by_alias=True, indent=2)
    yaml_file = modelo.model_dump_json(indent=2)
except ValidationError as err:
    print (f"{err=}")

# Json and Yaml templates generation
try:
    file_json(json_file)
    file_yaml(yaml_file)
except Exception as err:
    print (f"{err=}")

# Json schema generation 
type_adapter = TypeAdapter(DataModel)
with open("json_schema.json", "w") as file:
    file.write(json.dumps(type_adapter.json_schema(by_alias=True), indent=2))
