def vowel_filter(function):
    def wrapper():
        result = function()
        filtered_result = [x for x in result if x.lower() in 'aeiou']
        return filtered_result

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())