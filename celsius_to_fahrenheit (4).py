#celsius_to_fahrenheit.py
#Celsius to Fahrenheit program for CSCI 111-900
#Last edited 9/15/19 by Pat Doyle


city_name =(input("Enter city name: "))
#prompts for name of city
temp_celsius = float(input("Enter the temperature in degrees celsius: "))
#prompts for temperature in degrees celsius
temp_fahrenheit = ((9 / 5) * temp_celsius) + 32
#defines variable for degrees fahrenheit
print("The current temperature in", city_name , "is" , temp_celsius , u"\u00B0" , "celsius or" , temp_fahrenheit , u"\u00b0","fahrenheit.")
#outputs city name and temperature in celsius and fahrenheit 
