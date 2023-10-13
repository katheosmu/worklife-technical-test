import sqlalchemy as sa
from sqlalchemy.orm import relationship
from .base import BaseModel

TOTAL_VACATIONS = 25 # Days

class EmployeeModel(BaseModel):
    __tablename__ = "employee"
    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    balance = sa.Column(sa.Integer, default=TOTAL_VACATIONS)
    vacations = relationship("VacationModel", back_populates="employee")
