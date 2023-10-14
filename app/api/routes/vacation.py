from typing import Optional
from uuid import UUID

from fastapi import (
    Depends,
    APIRouter,
)
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repository.vacation import VacationRepository
from app.schema import VacationBase, VacationUpdateCreate

router = APIRouter()


@router.get("/{vacation_id}", response_model=Optional[VacationBase])
def get_vacation(session: Session = Depends(get_db), *, vacation_id: UUID):
    return VacationRepository.get(session=session, id=vacation_id)

@router.post("/", response_model=VacationBase)
def create_vacation(vacation_in: VacationUpdateCreate, session: Session = Depends(get_db)):
    return VacationRepository.create_vacation(session=session, vacation_in=vacation_in)

@router.patch("/{vacation_id}")
def update_vacation(vacation_id: UUID, vacation_in: VacationUpdateCreate, session: Session = Depends(get_db)):
    return VacationRepository.update(session, vacation_id, vacation_in)

@router.delete("/{vacation_id}")
def delete_vacation(vacation_id: UUID, session: Session = Depends(get_db)):
    return VacationRepository.delete(session=session, id=vacation_id)
