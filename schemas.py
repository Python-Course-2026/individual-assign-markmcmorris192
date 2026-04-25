from pydantic import BaseModel, Field
from datetime import date

class DateRange(BaseModel):
    date1: date = Field(..., description="Дата рождения (ГГГГ-MM-ДД)")
    date2: date = Field(..., description="Дата рождения (ГГГГ-MM-ДД)")

class BirthDate(BaseModel):
    birth_date: date = Field(..., description="Дата рождения (ГГГГ-MM-ДД)")



