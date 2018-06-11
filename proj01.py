# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.



# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


# If you complete extensions, describe your extensions here!
name = raw_input("Name")
birth_month = int(raw_input(Birth_month))
birth_day = int(raw_input(Birth_day))
current_month = 6
current_day = 11
if birth_month > current_month:
    months = birth_month - current_month
else:
    months = 12 - (current_month - birth_month)
if birth_day > current_day:
    days =  birth_day -  current_day
else:
    days = 30 - (current_day - birth_day)
    months = months - 1
print name + ", you will have your birthday in " + months + "months and" + days + "days."




