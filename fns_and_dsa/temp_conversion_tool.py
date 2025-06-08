FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def FAHRENHEIT_TO_CELSIUS():
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    temperature = (user_temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return f"{user_temp}°F is {temperature}°C"

def CELSIUS_TO_FAHRENHEIT():
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    temperature = user_temp * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return f"{user_temp}°C is {temperature}°F" 

if __name__ == "__main__":
    
    user_temp = float(input("Enter the temperature to convert: "))
    temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if temperature_type == "C":
        print(CELSIUS_TO_FAHRENHEIT())
    elif temperature_type == "F":
        print(FAHRENHEIT_TO_CELSIUS())
    else:
        print("Invalid temperature type. Please try again.")
        
    
    


    
