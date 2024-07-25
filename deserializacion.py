from pydantic import BaseModel, ValidationError, Field
from datetime import date
from dict_ejemplo import data
from json_ejemplo import data_json

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


# Deserialización: Convierte Dict o Json a formato Clase pydantic (instancia).
# Deserializacion from Dict.
try:
    car = Automobil.model_validate(data)
    print ("instancia:\n",car)
except ValidationError as err:
    print (err)

# Deserializacion from Json
try:
    car = Automobil.model_validate_json(data_json)
    print ("Instancia:\n", car)
except ValidationError as err:
    print (err)