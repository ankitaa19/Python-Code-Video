class DivisibleBySevenGenerator:
    def __init__(self, n):
        self.n = n

    def generate_numbers(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num

# Example usage:
n = 100
generator = DivisibleBySevenGenerator(n)

for divisible_by_seven in generator.generate_numbers():
    print(divisible_by_seven)