from sqlalchemy.orm import Session

from app.models.customer_details_request import CustomerDetailsRequest
from app.models.customer_details_response import CustomerDetailsResponse
from app.repositories.customer_details_repo import CustomerDetailsRepo


class CustomerDetailsService:

    def __init__(self):
        self.repo = CustomerDetailsRepo()

    def get_customer_details_by_id(self, request: CustomerDetailsRequest, db: Session):
        print("[CustomerDetailsService.get_customer_details_by_id]")
        entity = self.repo.get_customer_details_by_id(request, db)
        if not entity:
            return None
        else:
            return CustomerDetailsResponse.model_validate(entity.__dict__)


    def get_customer_by_id(self, id: int, db: Session):
        entity = self.repo.get_customer_by_id(id, db)
        if not entity:
            return None
        else:
            return CustomerDetailsResponse.model_validate(entity.__dict__)

