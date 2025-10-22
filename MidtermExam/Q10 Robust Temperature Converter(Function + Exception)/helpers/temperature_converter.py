#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def cel_to_far(c: float) -> float:
    """
    Convert Celsius to Fahrenheit.

    Args:
        c (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (c * 9 / 5) + 32


def far_to_cel(f: float) -> float:
    """
    Convert Fahrenheit to Celsius.

    Args:
        f (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    return (f - 32) * 5 / 9


def run_cli():
    print("Temperature Converter")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")

    choice = input("Choose conversion (1 or 2): ").strip()
    if choice not in {"1", "2"}:
        print("Invalid choice. Please enter 1 or 2.")
        return

    temp_input = input("Enter temperature: ").strip()
    try:
        temp = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    if choice == "1":
        result = cel_to_far(temp)
        print(f"{temp}°C is {result:.2f}°F")
    else:
        result = far_to_cel(temp)
        print(f"{temp}°F is {result:.2f}°C")


if __name__ == "__main__":
    run_cli()


# In[ ]:




