# @ALLOWED_VERSIONS: 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12

import warnings
from typing import Tuple

import numpy as np

warnings.filterwarnings("ignore")


class Mandelbrot:
    def __init__(
        self,
        size: Tuple[float, ...] = (-1.5, 1.5, -1.5, 1.5),
        edges=2,
        maxiter=25,
        color: bool = True,
    ) -> None:
        self.size = size
        self.edges = edges
        self.maxiter = maxiter
        self.color = color
        # np.log(2): 0.693147

    def _initiate(self) -> Tuple[np.ndarray, ...]:
        N = 512
        x1, x2, y1, y2 = self.size
        x, y = np.meshgrid(np.linspace(x1, x2, N), np.linspace(y1, y2, N))
        c = x + (1j * y)

        z = c.copy()
        fractal = np.zeros(z.shape, dtype=np.uint8)
        return c, z, fractal

    def _normalize(self, z: np.ndarray, fractal: np.ndarray) -> np.ndarray:
        if self.color:
            return (fractal**0.3).astype(np.float64)
        return np.abs(z)

    def calculate(self) -> np.ndarray:
        c, z, fractal = self._initiate()
        for n in range(self.maxiter):
            z = z**self.edges + c
            if self.color:
                fractal[(np.abs(z) > self.maxiter)] = n - (np.log(n) / 0.693147) * 0.1
        return self._normalize(z, fractal)


class TrigonometricMandelbrot(Mandelbrot):
    def __init__(
        self,
        size: Tuple[float, ...] = (-1.5, 1.5, -1.5, 1.5),
        maxiter=100,
        color: bool = True,
    ) -> None:
        super().__init__(size=size, maxiter=maxiter, color=color)


class Tricorn(Mandelbrot):
    def calculate(self) -> np.ndarray:
        c, z, fractal = self._initiate()
        for n in range(self.maxiter):
            z = z.conj()
            z = z**self.edges + c
            if self.color:
                fractal[(np.abs(z) > self.maxiter)] = n - (np.log(n) / 0.693147) * 0.1
        return self._normalize(z, fractal)


class TrigonometricSineMandelbrot(TrigonometricMandelbrot):
    def calculate(self) -> np.ndarray:
        c, z, fractal = self._initiate()
        for n in range(self.maxiter):
            z = np.sin(z / c)
            if self.color:
                fractal[(np.abs(z) > self.maxiter)] = n - (np.log(n) / 0.693147) * 0.1
        return self._normalize(z, fractal)


class TrigonometricCosineMandelbrot(TrigonometricMandelbrot):
    def calculate(self) -> np.ndarray:
        c, z, fractal = self._initiate()
        for n in range(self.maxiter):
            z = np.cos(z / c)
            if self.color:
                fractal[(np.abs(z) > self.maxiter)] = n - (np.log(n) / 0.693147) * 0.1
        return self._normalize(z, fractal)


def main():
    # Default Mandelbrot
    _ = Mandelbrot().calculate()
    # Tricorn
    _ = Tricorn().calculate()
    # Trigonometric Mandelbrot
    _ = TrigonometricSineMandelbrot().calculate()  # sine
    _ = TrigonometricCosineMandelbrot().calculate()  # cosine
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
