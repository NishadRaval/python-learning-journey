# def function_name():
     # some work
# function_name()   # calls itself

def print_numbers(n):
    if n > 5:      # Base case
        return

    print(n)
    print_numbers(n + 1)

print_numbers(1)

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)