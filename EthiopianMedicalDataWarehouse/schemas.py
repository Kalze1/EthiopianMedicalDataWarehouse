from pydantic import BaseModel

class MedicalBusinessBase(BaseModel):
    name: str
    category: str
    location: str

class MedicalBusinessCreate(MedicalBusinessBase):
    pass

class MedicalBusiness(MedicalBusinessBase):
    id: int

    class Config:
        orm_mode = True
