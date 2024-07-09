from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "2024.07.16"},
    {"name": "Jane Smith", "birthday": "2024.07.13"},
    {"name": "Rick Smith", "birthday": "2024.06.10"}
]


def get_upcoming_birthdays(users):
    current_dt = datetime.today().date()
    arr = []
    for user in users:
        date = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        if date < current_dt:
            arr.append({'name': user['name'], 'congratulation_date': (date + timedelta(365)).strftime('%Y.%m.%d')})
        elif (date - current_dt) <= timedelta(7):
            if date.weekday() > 4:
                if date.weekday() == 5:
                    arr.append({'name': user['name'], 'congratulation_date': (date + timedelta(2)).strftime('%Y.%m.%d')})
                else:
                    arr.append({'name': user['name'], 'congratulation_date': (date + timedelta(1)).strftime('%Y.%m.%d')})
            else:
                arr.append({'name': user['name'], 'congratulation_date': date.strftime('%Y.%m.%d')})
            
    print(arr)
    
            


get_upcoming_birthdays(users)

# current_dt = datetime.today().date() + timedelta(1)

# yesr = current_dt.strftime('%Y.%m.%d')

# print(type(yesr))


    

