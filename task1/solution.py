from datetime import datetime

def days_between_dates(date1, date2, date_format="%d.%m.%Y"):
    try:
        d1 = datetime.strptime(date1, date_format)
        d2 = datetime.strptime(date2, date_format)
        return abs((d2 - d1).days)
    except ValueError as e:
        raise ValueError(f"Ошибка преобразования даты: {e}")
