from datetime import datetime

def get_days_from_today(date):
    current_dt = datetime.today().date()
    try:
        input_dt = datetime.strptime(date, '%Y-%m-%d').date()

        print((input_dt - current_dt).days)
    except ValueError:
        print(f'Input data incorrect. Please use correct date format \'year-month-day\', like {current_dt}')
    
date = input('Enter you date: ')
get_days_from_today(date)