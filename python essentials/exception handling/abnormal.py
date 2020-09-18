import math

from past.builtins import raw_input

while True:
    try:
        text = raw_input('> ')
        if text[0] == 'q':
            break
        x = float(text)
        y = 1 / math.log10(x)
        print("1 / log10({0}) = {1}".format(x, y))
    except ValueError:
        print("the value must be greater than 0")
    except ZeroDivisionError:
        print("the value must not be 1")
    except Exception:
        print("unexpected error")