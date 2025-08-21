# 1) https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python
def is_palindrome(s):
    s = s.lower()
    if s [::-1] == s:
        return True
    else:
        return False
# 2) https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/python
def between(a,b):
    result = []
    while a <= b:
        result.append(a)
        a += 1
    return result
# 3) https://www.codewars.com/kata/57a0885cbb9944e24c00008e/train/python
def remove_exclamation_marks(s):
    result = ''
    for i in s:
        if i != '!':
            result += i
    return result
# 4) https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python
# ?