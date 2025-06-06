# Conversion factors are defined globally, accessible by functions.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_ADJUSTMENT = 32 # Constant for the offset in Fahrenheit scale

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using a global conversion factor.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Use the global FAHRENHEIT_TO_CELSIUS_FACTOR to perform the conversion.
    celsius = (fahrenheit - FREEZING_POINT_ADJUSTMENT) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using a global conversion factor.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Use the global CELSIUS_TO_FAHRENHEIT_FACTOR to perform the conversion.
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_ADJUSTMENT
    return fahrenheit

def main():
    """
    Handles user interaction, prompts for temperature input, calls the
    appropriate conversion function, and displays the result.
    """
    try:
        # Prompt the user to enter a temperature.
        temp_input_str = input("Enter the temperature to convert: ")
        # Attempt to convert the input string to a float.
        # This will raise a ValueError if the input is not numeric.
        temperature_value = float(temp_input_str)

        # Prompt the user to specify whether it's in Celsius or Fahrenheit.
        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Based on the user's input, call the appropriate conversion function.
        if unit_input == 'F':
            converted_temperature = convert_to_celsius(temperature_value)
            # Display the converted temperature.
            print(f"{temperature_value}°F is {converted_temperature}°C")
        elif unit_input == 'C':
            converted_temperature = convert_to_fahrenheit(temperature_value)
            # Display the converted temperature.
            print(f"{temperature_value}°C is {converted_temperature}°F")
        else:
            # Handle invalid unit input.
            print("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError:
        # Catch ValueError if float conversion fails and print the specified error message.
        print("Invalid temperature. Please enter a numeric value.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")
