calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    len1 = len(string)
    upper_1 = string.upper()
    lower_1 = string.lower()
    return (len1, upper_1, lower_1)

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    return string_lower in (item.lower() for item in list_to_search)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)