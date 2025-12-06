#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element two lists up to list_length.
    On error insert 0 and print the appropriate message.
    """
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            res = a / b
        except IndexError:
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except Exception:
            # TypeError or others (wrong type)
            print("wrong type")
            result.append(0)
        else:
            result.append(res)
        finally:
            continue
    return result

