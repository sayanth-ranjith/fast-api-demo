from pydantic import BaseModel


class CustomerDetailsResponse(BaseModel):
    id: int
    firstname: str
    lastname: str
    address: str
    country: str
    state: str
    pincode: int
    gender: str
    accountnumber: int
