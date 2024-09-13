def palindrome(s):
    s.replace(' ', '')
    sreverse = s[::-1]
    return sreverse == s

val = palindrome('helleh')

print(val)