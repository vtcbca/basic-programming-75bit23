string = input("Write string: ")
is_palindrome = True
for i in range(len(string) // 2):
    if string[i] != string[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
