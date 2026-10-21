import math

class LinearCongruentialGenerator:
    def __init__(self, seed: int):
        self.m = 2**32      # m
        self.a = 1664525    # a
        self.c = 1013904223 # c
        self.seed = seed   # z_0

    def next_integer(self) -> int:
        """Generates the next random integer."""
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed


class UniformRandomVariableGenerator(LinearCongruentialGenerator):
    def next_uniform(self, low: float = 0.0, high: float = 1.0) -> float:
        """Generate a uniform variate in [low, high)."""
        if low > high:
            raise ValueError("low must be less than or equal to high")

        unit_value = self.next_integer() / self.m
        return low + (high - low) * unit_value

class StandardNormalRandomVariableGenerator(UniformRandomVariableGenerator):
    def next_normal(self) -> float:
        """Generate a standard normal variate using the Acceptance/Rejection Polar method."""
        while True:
            u1 = self.next_uniform(low=-1, high=1)
            u2 = self.next_uniform(low=-1, high=1)
            s = u1**2 + u2**2

            if s <= 1:
                break

        w = math.sqrt(-2.0 * math.log(s) / s)
        return u1 * w

class NormalRandomVariableGenerator(StandardNormalRandomVariableGenerator):
    def __init__(self, seed: int, mean: float = 0.0, stddev: float = 1.0):
        super().__init__(seed)
        self.mean = mean
        self.stddev = stddev

    def next_normal(self) -> float:
        """Generate a normal variate with specified mean and standard deviation."""
        return self.mean + self.stddev * super().next_normal()

