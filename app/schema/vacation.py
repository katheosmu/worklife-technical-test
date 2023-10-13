from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pydantic import root_validator

import datetime

from app.model.vacation import VacationModel

class VacationBase(sqlalchemy_to_pydantic(VacationModel)):
    ...
    
class VacationUpdateCreate(sqlalchemy_to_pydantic(VacationModel)):
    @root_validator
    def validate(cls, values):
        date_format = '%Y-%m-%d'
        start_date = values.get("start_date")
        end_date =  values.get("end_date")
        try:
            obj_start_date = datetime.datetime.strptime(start_date, date_format)
        except ValueError:
            raise ValueError("Start date must be in the format YYYY-mm-dd")
        
        try:
            datetime.datetime.strptime(end_date, date_format)
        except ValueError:
            raise ValueError("End date must be in the format YYYY-mm-dd")
 
        if obj_start_date < datetime.datetime.today():
            raise ValueError("It is not possible to create vacations in the past")
        
        if start_date >= end_date:
            raise ValueError("End date must be later than start date")

        return values
