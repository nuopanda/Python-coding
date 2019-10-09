from prime_generator import PrimeGenerator


def main():
    """call PrimeGeneartor constructor and generate_prime function"""
    generator = PrimeGenerator()
    generate_prime(generator)


def generate_prime(generator):
    """given PrimeGenerator object, print the prime list"""
    num_input = int(input("Enter a value: "))
    generator.primes_to_max(num_input)
    print(generator.prime_list)


main()
