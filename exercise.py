"""
Practical exercise 3: Help Julia on her trip to New York

A friend of yours, Julia, goes to New York, US to visit her brother who is studying there.
As soon as she lands at the JFK airport, she notices that the US is another world.
The distance is measured in miles, mass is measured in pounds, and the temperature is measured in Fahrenheit.
She is having trouble converting these values into metric units.
Another prblem is that she cannot remember the conversion ratios. Luckily, she has you as a friend.
In this practical exercise, you will write a number of functions to help your friend in converting these values.
"""

import seaborn as sns
import math

def greetings(name):
    print(f"Hello, {name} I just came to US")

greetings("Sam")

def diffrence(number1, number2):
    return number1-number2

print(diffrence(50,20))

def personel_information(birthday, place_of_birth, current_city):
    print(f"I was born on {birthday} in {place_of_birth} and now I live in {current_city}")

birthday = "4 September 1996"
place_of_birth = "London"
current_city = "London"

personel_information(birthday=birthday,place_of_birth=place_of_birth,current_city=current_city)

"""
While introducing herself, she noticed that from now on she has to change her current city!
Can you help her by creating a function that takes a new city name as an argument and changes the current_city?
"""

def change_city(current_city, new_city):
    return new_city

new_city = "New York"
current_city = change_city(current_city,new_city)

personel_information(birthday, place_of_birth,current_city)

"""
Julia needs a weather forecast
"""
day = [1,2,3,4,5,6,7]
avg_temperature = [14,9,3,11,18,27,6]

sns.lineplot(x=day,y=avg_temperature)

# Now let's define some functions for conversion

"""
Mile - Kilometer
Julia looked at the road sign and she sees that city center is 12 miles away from the airport. 
First, we will write a function for converting miles to kilometers.
"""

# 1 mile 1.60934 km

def mile2km(mile): # mile to km
    return mile * 1.60934

def km2mile(km):
    return km / 1.60934

assert math.isclose(mile2km(132.2), 212.754748, abs_tol=1e-5), "Test failed for mile2km!"
assert math.isclose(km2mile(48.44), 30.099295, abs_tol=1e-5), "Test failed for km2mile!"
print("Test passed!")

print(mile2km(12))

#Pound - Kilogram
# 1 pound = 0.45359 kilograms
# assert koşul true ise devam et false ise çalışmayı durdur

def pound_kilogram(quantity, mode):
    assert mode == "pound2kg" or mode == "kg2pound", "Invalid argument!"

    if mode == "pound2kg":
        return quantity * 0.45359
    else:
        return quantity / 0.45359
# Testler
assert pound_kilogram(10, "pound2kg") == 4.5359, "Test failed for pound to kg!"
assert pound_kilogram(4.5359, "kg2pound") == 10, "Test failed for kg to pound!"
print("All tests passed!")



#Fahrenheit-Celsius
#Formula: °C = (°F − 32) × 5/9
#Formula: °F = (°C x 9/5) + 32

def fahrenheit_celcius(temperature, mode):
    assert mode == "f2c" or mode == "c2f", "Invalid argument!"

    if mode == "f2c":
        return (temperature - 32) * 5 / 9
    else:
        return (temperature * 9 / 5) + 32

assert math.isclose(fahrenheit_celcius(98.6, "f2c"), 37.0, abs_tol=1e-5), "Test failed for mode \"f2c\"!"
assert math.isclose(fahrenheit_celcius(42, "c2f"), 107.6, abs_tol=1e-5), "Test failed for mode \"c2f\"!"
print("Test passed!")

print(fahrenheit_celcius(88,"f2c"))