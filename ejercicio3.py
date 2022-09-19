from ejercicio2 import evaluate_condition


def cgi_decoded_instrumented(s: str):
    """Decode the CGI−encoded string ‘s‘:
    ∗ replace '+' by ''
    ∗ replace '%xx' by the character with hex number xx.
    Return the decoded string. Raise ‘ValueError‘ for invalid inputs.
    """
    # Mapping of hex digits to their integer values
    hex_values = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    hex_values = {ord(key): value for key, value in hex_values.items()}
    t = ""
    i = 0
    while evaluate_condition(1, "Lt", i, len(s)):  # c1
        c = ord(s[i])
        if evaluate_condition(2, "Eq", c, ord("+")):  # c2
            t += " "
        elif evaluate_condition(3, "Eq", c, ord("%")):  # c3
            digit_high, digit_low = ord(s[i + 1]), ord(s[i + 2])
            i += 2
            if evaluate_condition(
                4, "In", digit_high, hex_values
            ) and evaluate_condition(
                5, "In", digit_low, hex_values
            ):  # c4
                v = hex_values[digit_high] * 16 + hex_values[digit_low]
                t += chr(v)
            else:
                raise ValueError("Invalid encoding")
        else:
            t += chr(c)
        i += 1
    return t
