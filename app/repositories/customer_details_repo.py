from sqlalchemy.orm import Session

from app.entity.customer_details_entity import CustomerDetails
from app.models.customer_details_request import CustomerDetailsRequest


class CustomerDetailsRepo:
    def get_customer_details_by_id(self, request: CustomerDetailsRequest, db: Session) -> type[CustomerDetails] | None:
        return db.query(CustomerDetails).filter(CustomerDetails.id == request.id).first()