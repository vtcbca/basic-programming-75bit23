row = int(input("Enter how many lines? "))
a = 64

for i in range(1, row + 1):

    spaces = ' ' * (row - i)
    
    first_half = ''.join(chr(a + j) for j in range(1, i + 1))
  
    second_half = ''.join(chr(a + j) for j in range(i - 1, 0, -1))
    
    print(spaces + first_half + second_half)
