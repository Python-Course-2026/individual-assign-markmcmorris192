
from fastapi import APIRouter, HTTPException
from datetime import date
from schemas import DateRange, BirthDate
from service import days_between, age_from_birthdate

router = APIRouter(prefix="/days", tags=["days"])


@router.post("/between")
def between(data: DateRange):
    return days_between(data.date1, data.date2)

@router.post("/age")
def age(data: BirthDate):
    if data.birth_date > date.today():
        raise HTTPException(status_code=400, detail="Дата рождения не может быть в будущем")
    return age_from_birthdate(data.birth_date)