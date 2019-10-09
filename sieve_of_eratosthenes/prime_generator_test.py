from prime_generator import PrimeGenerator


def test_primes_to_max():
    """test the output prime list with a given argument value"""
    generator = PrimeGenerator()
    prime_list_10 = [2, 3, 5, 7]
    assert generator.primes_to_max(10) == prime_list_10
    prime_list_20 = [2, 3, 5, 7, 11, 13, 17, 19]
    generator_2 = PrimeGenerator()
    assert generator_2.primes_to_max(20) == prime_list_20
