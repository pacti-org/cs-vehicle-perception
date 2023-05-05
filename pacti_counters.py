from functools import wraps
from pacti.terms.polyhedra import PolyhedralContract

def counter_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return fn(*args, **kwargs)

    wrapper.counter = 0
    return wrapper

PolyhedralContract.compose = counter_decorator(PolyhedralContract.compose)
PolyhedralContract.quotient = counter_decorator(PolyhedralContract.quotient)
PolyhedralContract.merge = counter_decorator(PolyhedralContract.merge)

import dataclasses
@dataclasses.dataclass
class PolyhedralContractCounts:
    compose: int = 0
    quotient: int = 0
    merge: int = 0

    def update_counts(self) -> "PolyhedralContractCounts":
        self.compose = PolyhedralContract.compose.counter
        self.quotient = PolyhedralContract.quotient.counter
        self.merge = PolyhedralContract.merge.counter
        return self

    def __add__(self, other: "PolyhedralContractCounts") -> "PolyhedralContractCounts":
        result = PolyhedralContractCounts()
        result.compose = self.compose + other.compose
        result.quotient = self.quotient + other.quotient
        result.merge = self.merge + other.merge
        return result

    def __str__(self) -> str:
        return f"PolyhedralContract operation counts: compose={self.compose}, quotient={self.quotient}, merge={self.merge}."
    