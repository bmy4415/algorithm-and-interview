# string reverse function without loop

def reverse(string):
    if len(string) == 0:
        return ''

    return string[len(string)-1:] + reverse(string[:len(string)-1])

tests = [
    'abc',
    '12345'
]

for test in tests:
    print(test, '->', reverse(test))