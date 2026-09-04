import unittest

from src.expense import Expense


class TestExpense(unittest.TestCase):

    def test_expense_creation(self):
        expense = Expense(250, "Food", "Lunch")

        self.assertEqual(expense.amount, 250)
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.description, "Lunch")

    def test_expense_amount_must_be_positive(self):
        with self.assertRaises(ValueError):
            Expense(0, "Food", "Lunch")

        with self.assertRaises(ValueError):
            Expense(-100, "Food", "Lunch")


if __name__ == "__main__":
    unittest.main()