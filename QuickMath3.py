class Calculator:
    def __init__(self):
        self.name = "calculator"

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def subtract(self, a, b):
        return a - b


calc = Calculator()

sum_result = calc.add(7, 3)
product_result = calc.multiply(4, 6)
quotient_result = calc.divide(20, 5)
difference_result = calc.subtract(15, 8)

print(sum_result)
print(product_result)
print(quotient_result)
print(difference_result)
