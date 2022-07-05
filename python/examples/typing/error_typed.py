# python -m mypy .\error_typed.py
from dataclasses import dataclass


@dataclass
class SalesSummaryNG:
    sales: int
    country: str
    product_codes: list[int]


summaryng_correct = SalesSummaryNG(
    sales=10, country="USA", product_codes=[123, 12414, 124, 123123, 1231]
)

summaryng_wrong = SalesSummaryNG(
    sales=10, country="USA", product_codes=[123, 124, {"a": "b"}, 1231, "12"]
)
