def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

string = input("Write string: ")
rev = reverse_string(string)
print(rev)
