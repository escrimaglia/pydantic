from pydantic import BaseModel, Field

class Interfaces(BaseModel):
    number: int = Field(ge=0, lt=10)
    tipo: str | None  = "gigabit"
    slot: int = Field(gt=0, lt=2) 
    port: int = Field(gt=0, lt=3)

class Device(BaseModel):
    nombre: str
    familia: str
    memoria: int = Field(gt=2000, lt=8000) 
    interfaces: list[Interfaces]

class Metadata(BaseModel):
    name: str | None
    author: str | None = "Ed Scrimaglia"
    tags: str | None

class Environment(BaseModel):
    repository: str | None
    ssh_config_file: str | None
    debug: bool | None = False
    ansible_command_timeout: int = Field(ge=100, le=180, default=180)
    module_command_timeout: int = Field(ge=100, le=1800, default=1800)
    sleep_time: int = Field(ge=100, le=180, default=0)

class Others(BaseModel):
    other: str | None = None

class Resources(BaseModel):
    devices: list[Device]
    others: list[Others]

class Specifications(BaseModel):
    environment: Environment
    resources: Resources

class Modelo(BaseModel):
    version: str | None = "api/v1"
    metadata: Metadata
    specifications: Specifications

class DataModel(BaseModel):
    modelo: Modelo