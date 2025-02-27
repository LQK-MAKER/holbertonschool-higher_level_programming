#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    azer = []
    for i in range(0, list_length):
        try:
            azer.append(my_list_1[i] / my_list_2[i])
        except (TypeError):
            print("wrong type")
            azer.append(0)
        except (ZeroDivisionError):
            print("division by 0")
            azer.append(0)
        except (IndexError):
            print("out of range")
            azer.append(0)
        finally:
            pass
    return azer
