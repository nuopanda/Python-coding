class PrimeGenerator:
    def __init__(self):
        """initialize the constructor, return empty list and set"""
        self.prime_list = []
        self.composite_set = set()

    def primes_to_max(self, N):
        """given a argument value N, return a list of prime"""
        for num in range(2, N+1):
            composite = 2*num
            while composite <= N:
                self.composite_set.add(composite)
                composite += num
        for num in range(2, N+1):
            if num in self.composite_set:
                continue
            else:
                self.prime_list.append(num)
        return self.prime_list
