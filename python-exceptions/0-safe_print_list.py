#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of a list and return the real number printed."""
    count = 0
    i = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except Exception:
            break
        i += 1
    print()
    return count

