# (For Individual)

import pywhatkit
import time

phone_number = "+92 3401219216"
message = "This message from Python Developer Waleed"
schedule_hour = 1 
schedule_minute = 43 
schedule_period = "AM"
num_messages = 5 #Enter a number for message do you want to send.

# Convert 12-hour format to 24-hour format
if schedule_period == "PM":
    schedule_hour = (schedule_hour % 12) + 12

for i in range(num_messages):
    pywhatkit.sendwhatmsg(phone_number, message, schedule_hour, schedule_minute)
    time.sleep(5)  # Adding a delay between messages to avoid rate-limiting


# # =============================================================
# (For Group)
    
import pywhatkit
import time

group_name = "Your WhatsApp Group Name"  # Replace with your group name
message = "This message from Python Developer Waleed"
schedule_hour = 1
schedule_minute = 34
schedule_period = "PM"
num_messages = 5

# Convert 12-hour format to 24-hour format
if schedule_period == "PM":
    schedule_hour = (schedule_hour % 12) + 12

for i in range(num_messages):
    pywhatkit.sendwhatmsg_to_group(group_name, message, schedule_hour, schedule_minute)
    time.sleep(5)  # Adding a delay between messages to avoid rate-limiting
