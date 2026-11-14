import datetime

print("Personal Diary")

user_input = input("What would you like to write in your diary today? ")

file_name = "diary.txt"
file = open(file_name, "a")
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
file.write(f"{current_time} - {user_input}\n")
file.close()