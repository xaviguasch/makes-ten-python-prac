
# Create a function that takes two arguments.
# Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.


def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False

# def makes10(a, b):
# 	return 10 in [a, b, a+b]


print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))