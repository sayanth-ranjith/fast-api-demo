from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v2.v2_path_constant import V2_PATH_CONSTANT
from app.core.database import get_db
from app.models.customer_details_response import CustomerDetailsResponse
from app.service.customer_details_service import CustomerDetailsService

router = APIRouter(prefix=V2_PATH_CONSTANT, tags=["v2_customer_details"])


service = CustomerDetailsService()


@router.get("/fetchCustomer/{id}", response_model=CustomerDetailsResponse)
def get_customer_details(id: int, db: Session = Depends(get_db)):
    return service.get_customer_by_id(id, db)

