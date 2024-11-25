calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(x):

    y = (len(x), x.upper(),x.lower())

    count_calls()
    return y


def is_contains(x, y):
    count_calls()
    for i in y:
        if i.lower() == x.lower():
            return True
    for i in y:
        if i.lower() != x.lower():
            return False

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))

print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)
