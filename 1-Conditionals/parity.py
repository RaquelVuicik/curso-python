# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Par")
# else:
#     print("Impar")

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Par")
    else:
        print("Impar")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

def is_even(n):
    return n % 2 == 0

main()