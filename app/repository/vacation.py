from app.model import VacationModel
from app.repository.base import BaseRepository
from fastapi.encoders import jsonable_encoder
from sqlalchemy import and_, or_
from datetime import timedelta, datetime


class _VacationRepository(BaseRepository):
    def get_by_id(self, session, vacation_id):
        return self.query(session).filter(self.model.id == vacation_id)
    
    def create_vacation(self, session, vacation_in):
        obj_in_data = jsonable_encoder(vacation_in)
        return self.overlap_dates(session, obj_in_data)

    
    def overlap_dates(self, session, vacation_in, vacation_id=None):
        new_start_date = vacation_in["start_date"]
        new_end_date = vacation_in["end_date"]
        employee_id = vacation_in["employee_id"]
        vacation_type = vacation_in["type"]
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
            vacation_in["start_date"] = min(*start_dates, new_start_date)
            vacation_in["end_date"] = max(*end_dates, new_end_date)
        
        # Calculate duration
        vacation_in["duration"] = self.calculate_duration(vacation_in["start_date"], vacation_in["end_date"])

        if not vacation_id is None and vacations.count() == 1 and vacations[0].id == vacation_id:
            # In case of an update where no merge is needed
            return self.update(session, vacation_id, vacation_in)
        else:
            db_item = self.model(**vacation_in)
            new_vacation = self.create_obj(session, db_item)
            for v in vacations:
                self.delete_obj(session, v)
            if vacation_id:
                self.delete(session, id)
            return new_vacation


    def update_vacation(self, session, vacation_id, vacation_in):
        obj_in_data = jsonable_encoder(vacation_in)
        return self.overlap_dates(session, obj_in_data, vacation_id)
    
    def calculate_duration(self, start_date, end_date):
        date_format = '%Y-%m-%d'
        start_date = datetime.strptime(start_date, date_format)
        end_date =  datetime.strptime(end_date, date_format)
        daygenerator = (start_date + timedelta(x + 1) for x in range((end_date - start_date).days))
        return sum(1 for day in daygenerator if day.weekday() < 5)
        

VacationRepository = _VacationRepository(model=VacationModel)
