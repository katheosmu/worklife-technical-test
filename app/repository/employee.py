from app.model import EmployeeModel, VacationModel
from app.repository.base import BaseRepository

class _EmployeeRepository(BaseRepository):
    def get_employees_on_vacation(self, session, start_date, end_date):
        filters = [VacationModel.start_date <= start_date, VacationModel.end_date >= end_date]
        return session.query(self.model).join(VacationModel).filter(*filters).all()
        

EmployeeRepository = _EmployeeRepository(model=EmployeeModel)
