def adjust(variable, option='set', parameter=1):
    """ Adjust the variable of the current music
        Attributes:

            option:
                option about how to ajust, can be:
                    'set' to set a raw value
                    'raise' to increase the actual value
                    'lower' to decrease the actual value
                    'half' to half the actual value
                    'double' to double the actual value

            parameter:
                parameter about how to adjust,
                    'set' will set the actual to that parameter
                    'raise' will increase that parameter
                    'lower' will decrease that parameter
                    'half' will half parameter times
                    'double' will double the parameter times
                    """
    operation = {
        'set': parameter,
        'raise': variable + parameter,
        'lower': variable - parameter,
        'half': variable / 2**parameter,
        'double': variable * 2**parameter,
    }
    result = operation[option]
    return result
