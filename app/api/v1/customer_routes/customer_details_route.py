from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.constants.v1_path_constant import V1_PATH_CONSTANT
from app.core.database import get_db
from app.models.customer_details_request import CustomerDetailsRequest
from app.models.customer_details_response import CustomerDetailsResponse
from app.service.customer_details_service import CustomerDetailsService

router = APIRouter(prefix=V1_PATH_CONSTANT, tags=["v1_customer_details"])

service = CustomerDetailsService()

@router.post("/fetchCustomerDetails", response_model=CustomerDetailsResponse)
def fetch_customer_details(request: CustomerDetailsRequest, db: Session = Depends(get_db)):
    return service.get_customer_details_by_id(request, db)
