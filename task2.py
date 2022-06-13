def palindrome(s):
    return s[::-1] == s
while True:
    s = input("Введите палиндром: ")
    print(f"{s} является палиндромом!" if palindrome(s) else "не является палиндромом")