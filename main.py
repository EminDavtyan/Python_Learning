date = input('Date(10.10.2023): ').split('.')

day, month, year = int(date[0]), int(date[1]), int(date[2])


def check_year():
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0


def check_month():
    if month % 2 == 0:
        if month == 2:
            if check_year():
                return 29
            else:
                return 28
        else:
            return 30
    else:
        return 31


if day + 1 > check_month():
    day = 1
    if month + 1 > 12:
        month = 1
        year += 1
    else:
        month += 1

else:
    day += 1

print(f'next day is {day}.{month}.{year}')
