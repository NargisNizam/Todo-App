"""Integration tests for complete user flows."""

import unittest
from unittest.mock import patch
from todo_app import task_manager


class TestIntegration(unittest.TestCase):
    """Test cases for complete user flows."""

    def setUp(self):
        """Reset task manager state before each test."""
        task_manager.tasks.clear()
        task_manager._next_id = 1

    def test_add_and_view_task(self):
        """Test adding a task and viewing it in the list."""
        task = task_manager.add_task("Buy groceries")
        tasks = task_manager.get_all_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, 1)
        self.assertEqual(tasks[0].description, "Buy groceries")
        self.assertFalse(tasks[0].is_complete)

    def test_add_update_view_task(self):
        """Test adding, updating, and viewing a task."""
        task = task_manager.add_task("Old description")
        updated = task_manager.update_task(1, "New description")
        tasks = task_manager.get_all_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].description, "New description")
        self.assertEqual(updated.description, "New description")

    def test_add_delete_verify_gone(self):
        """Test adding and deleting a task."""
        task_manager.add_task("Task to delete")
        result = task_manager.delete_task(1)
        tasks = task_manager.get_all_tasks()

        self.assertTrue(result)
        self.assertEqual(len(tasks), 0)

    def test_add_toggle_verify_complete(self):
        """Test adding a task and toggling its completion status."""
        task = task_manager.add_task("Task to complete")
        toggled = task_manager.toggle_complete(1)
        tasks = task_manager.get_all_tasks()

        self.assertTrue(toggled.is_complete)
        self.assertTrue(tasks[0].is_complete)

    def test_multiple_tasks_maintain_order(self):
        """Test that multiple tasks maintain insertion order."""
        task_manager.add_task("First task")
        task_manager.add_task("Second task")
        task_manager.add_task("Third task")
        tasks = task_manager.get_all_tasks()

        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0].description, "First task")
        self.assertEqual(tasks[1].description, "Second task")
        self.assertEqual(tasks[2].description, "Third task")

    def test_id_never_reused(self):
        """Test that IDs are never reused after deletion."""
        task_manager.add_task("First task")
        task_manager.delete_task(1)
        task2 = task_manager.add_task("Second task")
        task3 = task_manager.add_task("Third task")

        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)

        tasks = task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)

    def test_update_nonexistent_task(self):
        """Test updating a task that doesn't exist."""
        result = task_manager.update_task(999, "New description")
        self.assertIsNone(result)

    def test_delete_nonexistent_task(self):
        """Test deleting a task that doesn't exist."""
        result = task_manager.delete_task(999)
        self.assertFalse(result)

    def test_toggle_nonexistent_task(self):
        """Test toggling a task that doesn't exist."""
        result = task_manager.toggle_complete(999)
        self.assertIsNone(result)

    def test_complex_workflow(self):
        """Test a complex workflow with multiple operations."""
        # Add three tasks
        task1 = task_manager.add_task("Task 1")
        task2 = task_manager.add_task("Task 2")
        task3 = task_manager.add_task("Task 3")

        # Mark task 2 as complete
        task_manager.toggle_complete(2)

        # Update task 1
        task_manager.update_task(1, "Updated Task 1")

        # Delete task 3
        task_manager.delete_task(3)

        # Verify final state
        tasks = task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].description, "Updated Task 1")
        self.assertFalse(tasks[0].is_complete)
        self.assertEqual(tasks[1].description, "Task 2")
        self.assertTrue(tasks[1].is_complete)

    def test_toggle_twice_returns_to_original(self):
        """Test toggling status twice returns to original state."""
        task = task_manager.add_task("Toggle test")

        # First toggle: incomplete -> complete
        task_manager.toggle_complete(1)
        task1 = task_manager.get_task_by_id(1)
        self.assertTrue(task1.is_complete)

        # Second toggle: complete -> incomplete
        task_manager.toggle_complete(1)
        task2 = task_manager.get_task_by_id(1)
        self.assertFalse(task2.is_complete)

    def test_update_preserves_completion_status(self):
        """Test that updating description preserves completion status."""
        task_manager.add_task("Original task")
        task_manager.toggle_complete(1)

        updated = task_manager.update_task(1, "Updated task")

        self.assertEqual(updated.description, "Updated task")
        self.assertTrue(updated.is_complete)


if __name__ == "__main__":
    unittest.main()
