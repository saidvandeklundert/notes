from typing import TypedDict


class SalesSummary(TypedDict):
    sales: int
    country: str
    product_codes: list[str]


def get_sales_summary() -> SalesSummary:
    """Return summary for yesterday's sales."""
    return {
        "sales": 1_000,
        "country": "UK",
        "product_codes": ["SUYDT"],
    }


sales_summary = get_sales_summary()
try:
    sales = sales_summary["saldes"]  # <- the typechecker will catch this!
except KeyError as e:
    print(e, "as we expected")
sales = sales_summary["sales"]
print(type(sales_summary))  # this is still 'just' a dict