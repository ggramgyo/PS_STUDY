import sys

def isPalindrome(a, b):
    while a < b:
        if word[a] == word[b]:
            a += 1
            b -= 1
        else:
            return False
    return True

word = list(sys.stdin.readline().rstrip())
if len(set(word)) ==  1:
    print(-1)
else:
    if isPalindrome(0, len(word) - 1):
        print(len(word) - 1)
    else:
        print(len(word))