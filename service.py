from datetime import date
from decorator import timer
import time

@timer
def days_between(date1, date2)->dict:
    time.sleep(2)
    delta_date = abs((date1 - date2).days)
    return {"date1": str(date1), "date2": str(date2), "days": delta_date}
@timer
def age_from_birthdate(birth_date: date) -> dict:
    time.sleep(2)
    today = date.today()
    years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        years -= 1

    total_days = (today - birth_date).days
    return {"birth_date": str(birth_date), "age_years": years, "total_days": total_days}



