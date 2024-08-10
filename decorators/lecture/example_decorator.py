def uppercase(function):  # decorator
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper

@uppercase
def say_hi():
    return 'say hi'


print(say_hi())
