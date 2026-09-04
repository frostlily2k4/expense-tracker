from datetime import date


class Expense:
    """Represent a single expense."""

    def __init__(self, amount, category, description):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.amount = amount
        self.category = category
        self.description = description
        self.date = date.today()

    def __str__(self):
        return (
            f"₹{self.amount:.2f} | "
            f"{self.category} | "
            f"{self.description} | "
            f"{self.date}"
        )


if __name__ == "__main__":
    expense = Expense(250, "Food", "Lunch")

    print(expense)