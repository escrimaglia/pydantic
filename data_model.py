# Pydantic classes whose diagram class is in the file Class_diagram.png
# By Ed Scrimaglia

from pydantic import BaseModel, Field, ConfigDict, EmailStr, IPvAnyAddress, AfterValidator
from typing import Annotated
from validation_functions import ValidateUniqueInList


# Class Interface
class Interface(BaseModel):
    model_config = ConfigDict(extra="forbid")
    number: int = Field(ge=0, lt=10)
    tipo: str | None  = "gigabit"
    slot: int = Field(gt=0, lt=2) 
    port: int = Field(gt=0, lt=3)

# Class Vlan
class Vlan(BaseModel):
    model_config = ConfigDict(extra="forbid")
    number: int = Field(ge=0, le=4096)
    name: str | None = Field(min_length=5, max_length=20)


# Class Device
class Device(BaseModel):
    model_config = ConfigDict(extra="forbid")
    nombre: str | None = Field(min_length=6, max_length=40)
    familia: str | None = Field(min_length=6, max_length=50)
    memoria: int = Field(gt=2000, lt=8000)
    ip_address: IPvAnyAddress | None = Field(serialization_alias="ipAddress")
    interface: Annotated[list[Interface], AfterValidator(ValidateUniqueInList.validate_unique_list_objects)] | None
    vlan: Annotated[list[Vlan], AfterValidator(ValidateUniqueInList.validate_unique_list_objects)] | None


# Class Metadata
class Metadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str | None
    author: str | None = "Ed Scrimaglia"
    email: EmailStr | None = "edscrimaglia@octupus.com"
    tags: str | None


# Class Environment
class Environment(BaseModel):
    model_config = ConfigDict(extra="forbid")
    repository: str | None
    ssh_config_file: str | None
    debug: bool | None = False
    ansible_command_timeout: int = Field(ge=100, le=180, default=180, serialization_alias="ansibleCommandTimeout")
    module_command_timeout: int = Field(ge=100, le=1800, default=1800, serialization_alias="moduleCommandTimeout")
    sleep_time: int | None = Field(ge=50, le=180, default=50, serialization_alias="sleepTime")


# Class Others
class Others(BaseModel):
    model_config = ConfigDict(extra="forbid")
    other: str | None = None


# Class Resource
class Resource(BaseModel):
    model_config = ConfigDict(extra="forbid")
    device: list[Device]
    others: list[Others]


# Class Specification
class Specification(BaseModel):
    model_config = ConfigDict(extra="forbid")
    environment: Environment
    resource: Resource


# Clase Modelo
class Modelo(BaseModel):
    model_config = ConfigDict(extra="forbid")
    version: str | None = "api/v1"
    metadata: Metadata
    specification: Specification


# Clase DataModel
class DataModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    modelo: Modelo
