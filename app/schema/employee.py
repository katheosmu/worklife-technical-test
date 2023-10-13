from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from typing import List

from app.model.employee import EmployeeModel
from app.model.vacation import VacationModel


class EmployeeBase(sqlalchemy_to_pydantic(EmployeeModel)):
    ...

class EmployeeWithVacation(sqlalchemy_to_pydantic(EmployeeModel)):
    vacations : List[sqlalchemy_to_pydantic(VacationModel)] = []
