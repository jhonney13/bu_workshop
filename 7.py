days = int(input("Enter the number of days: "))

years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

print(days, "days is approximately", years, "years,", weeks, "weeks, and", remaining_days, "days.")
