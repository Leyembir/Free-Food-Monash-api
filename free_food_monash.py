
from PIL import Image
from pytesseract import pytesseract
import requests

import cv2


import re
import json
    #Define path to image
PATH_TO_IMAGE = r'C:\Users\amir0\Documents\Python project amir\\backend\\images\\free_food1.jpg'


preprocess_type = "thresh"  # Replace with the desired preprocessing type
# Get the current directory (project_folder in this case)
# print(PATH_TO_IMAGE)
image = cv2.imread(PATH_TO_IMAGE)

 


# gray = cv2.medianBlur(blackAndWhiteImage, 3)



def ocr_core(PATH_TO_IMAGE = r'C:\Users\amir0\Documents\Python project amir\\backend\\images\\free_food1.jpg'
):
    # Define path to tessaract.exe
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    # Open image with PIL
    img = Image.open(PATH_TO_IMAGE)

    # Extract text from image
    text = pytesseract.image_to_string(image) 

    new_text = text.splitlines()
    new_text = [x for x in new_text if x != '']
    print(new_text)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_indices = {}

    for i, line in enumerate(new_text):
        for day in days:
            # Check if day is in the line, with or without a dash and additional characters
            if re.search(f"{day}(-\w+)?", line):
                day_indices[day] = i

    monday_list = new_text[day_indices["Monday"]-1:day_indices["Tuesday"]]
    tuesday_list = new_text[day_indices["Tuesday"]:day_indices["Wednesday"]]
    wednesday_list = new_text[day_indices["Wednesday"]:day_indices["Thursday"]]
    thursday_list = new_text[day_indices["Thursday"]:day_indices["Friday"]]
    friday_list = new_text[day_indices["Friday"]:]

    return monday_list, tuesday_list, wednesday_list, thursday_list, friday_list





def locations(weekDay_list: list):
    location = []
    j = 2
    while j < len(weekDay_list):
        #find index of all the numbers
        if any(i.isdigit() for i in weekDay_list[j]):
            location.append(weekDay_list[j-1])
        if j == len(weekDay_list) - 1:
            location.append(weekDay_list[-1])

        j += 1
    return location

def days(days_list: list):
    days_list = [item for item in days_list if item not in locations(days_list)]


    return days_list[1:]






# splits the list into time and eventname
def split_time_and_events(input_list):
    time_list = []
    event_list = []
    current_time = None
    current_event = ""

    for item in input_list:
        # Check and replace 'S' if preceded by a digit and followed by 'pm:'/'am:'
        item = re.sub(r'(?<=\d)S(?=pm:|am:)', '5', item, flags=re.IGNORECASE)
        # Check and replace 'S' standalone or connected with 'pm'/'am' preceded by a hyphen ('-')
        item = re.sub(r'(\b|-)S(?=pm:|am:)', r'\g<1>5', item, flags=re.IGNORECASE)

        # Use regular expression to find the time pattern in the string
        time_match = re.search(r'\b\d{1,2}(?::\d{2})?(?:[ap]m)?(?:\s*-\s*\d{1,2}(?::\d{2})?(?:[ap]m)?)?\b', item, re.IGNORECASE)

        if time_match:
            # If a new time is found, save the current event under the previous time (if any)
            if current_time is not None:
                time_list.append(current_time)
                event_list.append(current_event.strip())

            # Reset the current event and update the current time
            current_time = time_match.group()
            current_event = item.replace(current_time, "").strip(": ").strip()
        else:
            # Concatenate the item to the current event (if any)
            current_event += " " + item

    # Save the last event under the last time (if any)
    if current_time is not None:
        time_list.append(current_time)
        event_list.append(current_event.strip())

    return time_list, event_list

#everything into a list


def creating_json_object():
    # You can use the function as defined in the previous code.
    monday_list, tuesday_list, wednesday_list, thursday_list, friday_list = ocr_core()
    json_object = {}
    print(monday_list)
    all_events = [monday_list, tuesday_list, wednesday_list, thursday_list, friday_list]
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]

    for j, events_list in enumerate(all_events):
        locations_list = locations(events_list)
        days_of_week = days(events_list)
        times, events = split_time_and_events(days_of_week)

        if weekdays[j] in json_object:
            json_object[weekdays[j]]["time"].extend(times)
            json_object[weekdays[j]]["event_name"].extend(events)
            json_object[weekdays[j]]["location"].extend(locations_list)
        else:
            json_object[weekdays[j]] = {
                "time": times,
                "event_name": events,
                "location": locations_list
            }

    json_string = json.dumps(json_object, indent=2)
    print(json_string)
    return json_object





creating_json_object()




def google_maps(req): 

    req.replace(' ','+')
    uri = 'https://www.google.com/maps/search/?api=1&query=monash+'
    url = uri+req
    ret = requests.get(url)

    print(ret.url)

# google_maps(tuesday_location[0])


