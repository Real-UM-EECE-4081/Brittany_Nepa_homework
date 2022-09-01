from datetime import datetime

current = datetime.now()
print("The current date and time is: ", current)

time_string = current.strftime("%d/%m/%Y %H:%M:%S")
print("current date and time is: ", time_string)