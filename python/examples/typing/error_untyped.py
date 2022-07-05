class SalesSummary:
    def __init__(self, sales, country, product_codes):
        self.sales = sales
        self.country = country
        self.product_codes = product_codes


summary_correct = SalesSummary(
    sales=10.12, country="USA", product_codes=[123, 12414, 124, 123123, 1231]
)

summary_wrong = SalesSummary(
    sales=10, country="USA", product_codes=[123, 124, {"a": "b"}, 1231, "12"]
)
