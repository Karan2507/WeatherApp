import requests  #USING NETWORK YOU CAN FETCH THINGS.
import os        #ROBO.
import json      #CREATING DICTIONARY.



city = input("Enter the name of the city : \n")   #THE NAME OF THE CITY FOR WHICH YOU WANT TO CHECK THE WEATHER.
url = f"https://api.weatherapi.com/v1/current.json?key=c60ebd1ed8784054990111329232806&q={city}"
#PICK A KEY FROM ANY WEATHER API WHICH CAN TELL YOU THE EXACT WEATHER. KEY'S WILL BE DIFFERENT FOR ALL.

r = requests.get(url)      # IT WILL FETCH YOUR URL.
# print(r.text)            # IT WILL PRINT THE WEATHER FOR YOU.
wdic = json.loads(r.text)         # METHOD IN JSON WHICH WILL CREATE A DICTIONARY FOR YOU.
t=wdic["current"] ["temp_c"]      # FROM THE WEATHER, THESE ARE THE FEW PARAMETERS WHICH YOU WANT TO CALL OUT.
w=wdic["current"] ["condition"] ["text"]          # LITTLE MORE INFORMATION


os.system(f"say 'The current weather in {city} is {t} degrees and the climate feels like there is a {w}'")
#THIS FUNCTION WILL SPEAK RESULTS. WE USED F-STRINGS METHOD HERE. FOR MAC USUALLY THE COMMAND IS SAY "STRING".


