def judge(year):
    if year % 400 == 0:
        return "the year is a leap year"
    elif year % 4 == 0 and year % 100 != 0:
        return "the year is a leap year"
    else:
        return "the year isn't a leap year"
year = raw_input("which year do u want to judge? ")
print judge(int(year))
def days(day):
    year = day / 10000
    month = day % 10000 / 100
    day = day % 100
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if judge(year) == "the year is a leap year":
        month_days[1] = 29
    return day + sum(month_days[0:month - 1])
day = raw_input("pls input the entire date u want to judge(example: 20180818) ")
print days(int(day))   