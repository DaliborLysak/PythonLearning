def palindrome(s):
    s.replace(' ', '')
    sreverse = s[::-1]
    return sreverse == s

# A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run".
print("Write a word for palindrom test:")
word = input()
result = palindrome(word)
print("It is palindrom" if result else "It is not palindrom")