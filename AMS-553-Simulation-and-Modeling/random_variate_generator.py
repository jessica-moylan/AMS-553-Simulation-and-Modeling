import math

# Inspired by the numpy Generator class
class RandomVariateGenerator:
    def __init__(self, seed: int):
        self.m = 2**32       # m
        self.a = 1664525     # a
        self.c = 1013904223  # c
        self.seed = seed     # z_0

    def _next_integer(self) -> int:
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def _random(self) -> float:
        """Generate a uniform variate in [0, 1)."""
        return self._next_integer() / self.m

    def bernoulli(self, p: float = 0.5) -> int:
        """Generate a Bernoulli variate with success probability p."""
        if not 0 <= p <= 1:
            raise ValueError("p must be in [0, 1]")
        return 1 if self._random() < p else 0

    def uniform(self, low: float=0.0, high: float=1.0, size: int = 1) -> float:
        """Generate a uniform variate in [low, high)."""
        if low > high:
            raise ValueError("low must be less than or equal to high")
        if size == 1:
            return low + (high - low) * self._random()
        return [low + (high - low) * self._random() for _ in range(size)]

    def uniform_int(self, low: int = 0, high: int = 2, size: int = 1) -> int | list[int]:
        """Generate integers in [low, high) by scaling a uniform draw."""
        if size == 1:
            return low + int((high - low) * self._random())
        return [low + int((high - low) * self._random()) for _ in range(size)]

    def exponential(self, rate: float = 1.0) -> float:
        """Generate an exponential variate."""
        if rate <= 0:
            raise ValueError("rate must be positive")
        u = self._random()
        return -math.log(u) / rate

    def _standard_normal(self) -> list[float, float]:
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
        return mean + stddev * self._standard_normal()[0]

    def log_normal(self, mean: float = 0.0, stddev: float = 1.0) -> float:
        """Generate a log-normal variate using the transformation of mean and sd so it makes more sense with money."""
        if stddev < 0:
            raise ValueError("stddev must be non-negative")
        modified_mean = math.log(mean**2 / math.sqrt(stddev**2 + mean**2))
        modified_stddev = math.sqrt(math.log(1 + (stddev**2 / mean**2)))
        return math.exp(self.normal(modified_mean, modified_stddev))
