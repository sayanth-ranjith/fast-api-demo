from pydantic import BaseModel


class CustomerDetailsRequest(BaseModel):
    id: int
    firstname: str
    lastname: str
    address: str
    country: str
    state: str
    pincode: int
    gender: str
    accountnumber: int

