from datetime import datetime, timedelta

now = datetime.now()
today = datetime.today().date()
future_date = now + timedelta(days=7)
past_date = now - timedelta(days=30)
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

weekday_name = now.strftime("%A")
#%a for short name like dec,web
#%A ---> December, Wednesday 
month_name = now.strftime("%B")
year_full = now.strftime("%Y")
week_number = now.strftime("%W") 
am_pm = now.strftime("%p")
hour_12 = now.strftime("%I")
hour_24 = now.strftime("%H")

print("Current datetime:", now)
print("Today's date:", today)
print("Future date (7 days later):", future_date)
print("Past date (30 days ago):", past_date)
print("Formatted datetime:", formatted_date)
print("Weekday name (%A):", weekday_name)
print("Month name (%B):", month_name)
print("Year (%Y):", year_full)
print("Week number of the year (%W):", week_number)
print("AM/PM (%p):", am_pm)
print("Hour (12-hour clock, %I):", hour_12)
print("Hour (24-hour clock, %H):", hour_24)
