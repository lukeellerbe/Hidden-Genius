A = range(90, 100)
B = range(80, 90)
C = range(70, 80)
D = range(60, 70)
F = range(0, 60)
grade = int(input(f"Enter your grade: "))
if grade in A:
    print("You got an A!")
if grade in B:
    print("You got a B!")
if grade in C:
    print("You got a C!")
if grade in D:
    print("You got a D!")
if grade in F:
    print("You got an F!")