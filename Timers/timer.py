import time
from datetime import datetime, timedelta

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))

total_seconds = (hours * 3600) + (minutes * 60)
end_time = datetime.now() + timedelta(seconds=total_seconds)

print(f"Alarm will go off at {end_time.strftime('%H:%M:%S')}")

time.sleep(total_seconds)

print("WAKE UP!")