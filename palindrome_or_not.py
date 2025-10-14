#program to check if palindrome or not

num=int(input("Enter a number to check whether palindrome or not"))
if num==num[::-1]:
    print("palindrome")
else:
    print("not palindrome")
