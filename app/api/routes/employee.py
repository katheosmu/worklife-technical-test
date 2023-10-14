from typing import Optional, List
from uuid import UUID

from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
)
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repository.employee import EmployeeRepository
from app.schema import EmployeeBase, EmployeeWithVacation

router = APIRouter()

@router.get("/on_vacation", response_model=Optional[List[EmployeeBase]])
def get_employees_on_vacation(start_date , end_date, session: Session = Depends(get_db)):
    return EmployeeRepository.get_employees_on_vacation(session=session, start_date=start_date, end_date=end_date)

@router.get("", response_model=Optional[List[EmployeeWithVacation]])
def get_employees(session: Session = Depends(get_db), *, id: UUID = None, first_name: str = None, last_name: str = None):
    query_params = {}
    if not id is None: query_params["id"] = id
    if not first_name is None: query_params["first_name"] = first_name
    if not last_name is None: query_params["last_name"] = last_name
    return EmployeeRepository.get_many(session=session, **query_params)

@router.get("/{employee_id}", response_model=Optional[EmployeeBase])
def get_employee(session: Session = Depends(get_db), *, employee_id: UUID):
    return EmployeeRepository.get(session=session, id=employee_id)

@router.post("/", response_model=EmployeeBase)
def create_employee(employee_in: EmployeeBase, session: Session = Depends(get_db)):
    db_employee = EmployeeRepository.get(
        session=session,
        first_name=employee_in.first_name,
        last_name=employee_in.last_name
    )
    if db_employee:
        raise HTTPException(status_code=400, detail="Employee already registered")
    return EmployeeRepository.create(session=session, obj_in=employee_in)
