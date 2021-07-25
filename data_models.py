from pydantic import BaseModel


class NpmDependencies(BaseModel):
    name: str
    version: str
    dependencies: dict
