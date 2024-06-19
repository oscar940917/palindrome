def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
input_str = input().strip()
if is_palindrome(input_str):
    print("yes")
else:
    print("no")
