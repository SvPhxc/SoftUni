def even_numbers(function):
    def wrapper(numbers):
        nums = numbers
        result = [x for x in nums if x % 2 == 0]
        return function(result)
    return wrapper

@even_numbers
def get_numbers(numbers):
    return numbers

print(get_numbers([1, 2, 3, 4, 5]))