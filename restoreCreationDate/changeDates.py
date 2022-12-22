import os
import datetime
import re

# Declare the last_date variable as global
global last_date

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

last_date = ""
# Loop through all files in the current directory
for file in sorted_alphanumeric(os.listdir()):
    # If the file is a jpeg
    print(file)
    if file.endswith(".jpeg"):
        last_date = os.popen(f'sh getCreationDate.sh "{file}"').read()
        os.popen(f'touch -t {last_date.strip()} "{file}"')
    elif file.endswith(".mov"):
        # Change the date of the file to the previously stored last_date value
        last_date = str(int(last_date) + 1)
        os.popen(f'touch -t {last_date.strip()} "{file}"')
