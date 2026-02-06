"""Unit tests for Task data model."""

import unittest
from todo_app.task import Task


class TestTask(unittest.TestCase):
    """Test cases for Task class."""

    def test_task_creation_valid(self):
        """Test Task creation with valid data."""
        task = Task(id=1, description="Buy groceries", is_complete=False)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Buy groceries")
        self.assertFalse(task.is_complete)

    def test_task_creation_empty_description(self):
        """Test ValueError raised for empty description."""
        with self.assertRaises(ValueError) as context:
            Task(id=1, description="")
        self.assertEqual(
            str(context.exception),
            "Task description cannot be empty"
        )

    def test_task_creation_whitespace_only(self):
        """Test ValueError raised for whitespace-only description."""
        with self.assertRaises(ValueError) as context:
            Task(id=1, description="   ")
        self.assertEqual(
            str(context.exception),
            "Task description cannot be empty"
        )

    def test_task_creation_too_long(self):
        """Test ValueError raised for description exceeding 500 characters."""
        long_description = "a" * 501
        with self.assertRaises(ValueError) as context:
            Task(id=1, description=long_description)
        self.assertEqual(
            str(context.exception),
            "Task description cannot exceed 500 characters"
        )

    def test_task_description_trimmed(self):
        """Test whitespace trimming in description."""
        task = Task(id=1, description="  Buy groceries  ")
        self.assertEqual(task.description, "Buy groceries")

    def test_task_default_incomplete(self):
        """Test is_complete defaults to False."""
        task = Task(id=1, description="Buy groceries")
        self.assertFalse(task.is_complete)

    def test_task_creation_explicit_complete(self):
        """Test Task creation with explicit is_complete=True."""
        task = Task(id=1, description="Buy groceries", is_complete=True)
        self.assertTrue(task.is_complete)

    def test_task_description_exactly_500_chars(self):
        """Test description with exactly 500 characters is valid."""
        description_500 = "a" * 500
        task = Task(id=1, description=description_500)
        self.assertEqual(len(task.description), 500)


if __name__ == "__main__":
    unittest.main()
