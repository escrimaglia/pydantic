from pydantic import BaseModel, Field
import pprint

class Reservacion(BaseModel):
    id: int
    nombre: str
    fecha: str
    cant_personas: int = Field(gt=0, lt=4)

pprint.pprint (Reservacion.model_json_schema())