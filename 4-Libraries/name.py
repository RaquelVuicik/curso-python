import sys

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Poucos argumentos")

if len(sys.argv) < 2:
    print("Poucos argumentos")
elif len(sys.argv) > 2:
    print("Muitos argumentos")
else:
    print("Hello, my name is", sys.argv[1])