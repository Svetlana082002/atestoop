import logging

logging.basicConfig(level=logging.INFO)


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'({self.real}+{self.imaginary}i)' if self.imaginary >= 0 else f'({self.real}{self.imaginary}i)'

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        if denominator == 0:
            logging.error("Attempt to divide by zero complex number.")
            return "Cannot divide by zero"
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real, imaginary)


class OperationCommand:
    def __init__(self, operation):
        self.operation = operation

    def execute(self, a, b):
        result = self.operation(a, b)
        operation_name = self.operation.__name__.strip('__')
        logging.info(f'{operation_name.capitalize()}: {a} {operation_name} {b} = {result}')
        return result


class CalculatorFacade:
    def __init__(self):
        self.commands = {
            'add': OperationCommand(ComplexNumber.__add__),
            'multiply': OperationCommand(ComplexNumber.__mul__),
            'divide': OperationCommand(ComplexNumber.__truediv__)
        }

    def perform_operation(self, operation, a, b):
        return self.commands[operation].execute(a, b)


def main():
    calculator = CalculatorFacade()
    complex_numbers = []

    for i in range(2):
        while True:
            try:
                real = int(input(f"Input complex number {i + 1} real part: "))
                imaginary = int(input(f"Input complex number {i + 1} imaginary part: "))
                complex_numbers.append(ComplexNumber(real, imaginary))
                break
            except ValueError:
                logging.error('Input numbers should be integers!')
                print("Please enter valid integers.")

    if len(complex_numbers) == 2:
        num1, num2 = complex_numbers
        print(f'{num1} + {num2} = {calculator.perform_operation("add", num1, num2)}')
        print(f'{num1} * {num2} = {calculator.perform_operation("multiply", num1, num2)}')
        print(f'{num1} / {num2} = {calculator.perform_operation("divide", num1, num2)}')


if __name__ == "__main__":
    main()
