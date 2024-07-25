from pydantic import BaseModel, ValidationError, Field
from datetime import date
from pprint import pprint
from dict_ejemplo import data, data_expected_serialization
from json_ejemplo import data_json, data_json_expected_serialization

class Automobil(BaseModel):
    manufacturer: str
    series_name: str
    type: str
    is_electric: bool = False
    manufactured_date: date
    base_msrp_usd: float = Field(gt=0, lt=10)
    vin: str
    numbers_of_doors: int = 4
    registration_country: str | None = None
    license_plate: str | None = None

# Serialización: confierte Clase pydantic (instancia) a formatos Dict o Json
# Serializacion a Dict
try:
    car = Automobil.model_validate(data)
    print ("instancia:\n",car)
    print ("serialization a Dic:\n",car.model_dump())
    print ("data:\n", data_expected_serialization)
    print ("Test contra data:\n",car.model_dump() == data_expected_serialization)
    print ("Fields inicializados\n",car.model_fields_set)
    print ("Fields default\n", car.model_fields.keys() - car.model_fields_set)
except ValidationError as err:
    print (err)
print ("--"*30)

# Serializacion a Json
try:
    car = Automobil.model_validate_json(data_json)
    print ("instancia:\n",car)
    print ("serialization a Json:\n",car.model_dump_json())
    print ("data_Json:\n", data_json)
    print ("Test contra data_json:\n",car.model_dump_json() == data_json_expected_serialization)
    print ("Fields inicializados\n",car.model_fields_set)
    print ("Fields default\n", car.model_fields.keys() - car.model_fields_set)
except ValidationError as err:
    print (err)

print ("--"*30)

# Json Schema de la clase Automobil
pprint (car.model_json_schema())
