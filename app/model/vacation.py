import sqlalchemy as sa
from sqlalchemy.orm import relationship
from enum import Enum

from .base import BaseModel, CustomUUID

class VacationType(str, Enum):
    paid = "paid"
    unpaid = "unpaid"

class VacationModel(BaseModel):
    __tablename__ = "vacation"
    type = sa.Column(sa.Enum(VacationType), nullable=False)
    duration = sa.Column(sa.Integer)
    start_date = sa.Column(sa.Date, nullable=False)
    end_date = sa.Column(sa.Date, nullable=False)
    employee_id = sa.Column(CustomUUID, sa.ForeignKey("employee.id"), nullable=False)
    employee = relationship("EmployeeModel")
