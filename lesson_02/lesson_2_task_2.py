def is_year_leap(year):
    return year % 4 == 0


year_input = int(input("Укажите год: "))
result = is_year_leap(year_input)


print(f"год {year_input}: {result}")
