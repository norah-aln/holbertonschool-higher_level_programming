#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide 2 integers and print the result in the finally block.
    Returns the result or None if division failed.
    """
    result = None
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result

