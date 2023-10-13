from app.model import VacationModel
from app.repository.base import BaseRepository
from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, or_

class _VacationRepository(BaseRepository):
    def get_by_id(self, session, vacation_id):
        return self.query(session).filter(self.model.id == vacation_id)
    
    def create_vacation(self, session, vacation_in):
        obj_in_data = jsonable_encoder(vacation_in)
        
        # Overlap
        new_start_date = obj_in_data["start_date"]
        new_end_date = obj_in_data["end_date"]
        employee_id = obj_in_data["employee_id"]
        vacation_type = obj_in_data["type"]
        filters = [
            or_(
                and_(self.model.start_date <= new_start_date, self.model.end_date >= new_start_date, self.model.employee_id == employee_id, self.model.type == vacation_type),
                and_(self.model.start_date <= new_end_date, self.model.end_date >= new_end_date, self.model.employee_id == employee_id, self.model.type == vacation_type),
                and_(self.model.start_date >= new_start_date, self.model.end_date <=  new_end_date, self.model.employee_id == employee_id, self.model.type == vacation_type)
            )
        ]
        vacations = session.query(self.model).filter(*filters).all()
        if vacations:
            start_dates = [v.start_date.isoformat() for v in vacations]
            end_dates = [v.end_date.isoformat() for v in vacations]
            obj_in_data["start_date"] = min(*start_dates, new_start_date)
            obj_in_data["end_date"] = max(*end_dates, new_end_date)

        #     TODO: Calculate duration
        #     db_item.duration = 0
        
        db_item = self.model(**obj_in_data)
        new_vacation = self.create_obj(session, db_item)
        for v in vacations:
            self.delete_obj(session, v)
        return new_vacation
    



VacationRepository = _VacationRepository(model=VacationModel)
