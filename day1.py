# variables and types
# Names, types, conversion, truthiness
# [  ] 1. Create variables for name (str), age (int), height (float), is_student (bool). Print each with its type().
# Check: Output shows str, int, float, bool.
name="nneamaka"
age=12
height=12.5
is_studenet=True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_studenet, type(is_studenet))


# [  ] 2. Swap two variables without a temp variable.
# Check: a=1, b=2 becomes a=2, b=1.
a, b = 1, 2
a, b = b, a
print(a, b)  # 2 1

# [  ] 3. Convert '42' to int, 42 to str, 3.9 to int, '3.14' to float.
# Check: int(3.9) == 3 (truncates, does not round).
print(int(3.9))    # 3
print(float('3.14')) # 3.14

# [  ] 4. Predict first, then run: type(5/2), type(5//2), type(True + 1).
# Check: float, int, int.
print(type(5/2))     # float
print(type(5//2))    # int
print(type(True + 1)) # int

# [  ] 5. Predict bool() of 0, '', [], None, '0', ' '.
# Check: False, False, False, False, True, True.
print(bool(0))
print(bool(''))
print(bool([]))
print(bool(None))
print(bool('0'))
print(bool(' '))