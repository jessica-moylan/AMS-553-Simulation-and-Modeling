import math

# Inspired by the numpy Generator class
class RandomVariateGenerator:
    def __init__(self, seed: int):
        self.m = 2**32       # m
        self.a = 1664525     # a
        self.c = 1013904223  # c
        self.seed = seed     # z_0

    def next_integer(self) -> int:
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def random(self) -> float:
        """Generate a uniform variate in [0, 1)."""
        return self.next_integer() / self.m

    def uniform(self, low: float=0.0, high: float=1.0) -> float:
        """Generate a uniform variate in [low, high)."""
        if low > high:
            raise ValueError("low must be less than or equal to high")
        return low + (high - low) * self.random()

    def standard_normal(self) -> list[float, float]:
        """Generate a standard normal variate using the polar method."""
        while True:
            u1 = self.uniform(-1, 1)
            u2 = self.uniform(-1, 1)
            s = u1**2 + u2**2

            if s <= 1:
                factor = math.sqrt(-2.0 * math.log(s) / s)
                return [u1 * factor, u2 * factor]

    def normal(self, mean: float = 0.0, stddev: float = 1.0) -> float:
        """Generate a normal variate with the given mean and standard deviation."""
        if stddev < 0:
            raise ValueError("stddev must be non-negative")
        return mean + stddev * self.standard_normal()[0]