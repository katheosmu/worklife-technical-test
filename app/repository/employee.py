from app.model import EmployeeModel, VacationModel
from app.repository.base import BaseRepository
from typing import List
import time
import sqlalchemy as sa
import pdb

class _EmployeeRepository(BaseRepository):
    # def get_by_id(self, session, employee_id):
    #     return self.query(session).filter(self.model.id == employee_id)
    
    # def get_vacations(self, session, date):
    #     return self.query(session).filter()

    def get_employees_on_vacation(self, session, start_date, end_date):
        # option 1:
        # filters = [VacationModel.start_date == start_date, VacationModel.end_date == end_date]
        # vacations = session.query(VacationModel).filter(*filters)
        # employees = list()
        # for vac in vacations:
        #     employees.append(vac.employee)
        # return employees
    
        # option 2:
        # filters = [self.model.vacations.any(start_date=start_date), self.model.vacations.any(end_date=end_date)]
        # return session.query(self.model).filter(*filters).all()

        # option 3:
        filters = [VacationModel.start_date <= start_date, VacationModel.end_date >= end_date]
        return session.query(self.model).join(VacationModel).filter(*filters).all()
        

EmployeeRepository = _EmployeeRepository(model=EmployeeModel)
