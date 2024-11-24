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
        if i == x:
            return True
        elif i != x :
            return False


print(string_info('gg'))
print(is_contains('all', ['all','ill']))
print(is_contains('alll', ['all','ill']))
print(calls)