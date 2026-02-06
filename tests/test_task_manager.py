"""Unit tests for TaskManager business logic."""

import unittest
from todo_app import task_manager
from todo_app.task import Task


class TestTaskManager(unittest.TestCase):
    """Test cases for task_manager module."""

    def setUp(self):
        """Reset task manager state before each test."""
        task_manager.tasks.clear()
        task_manager._next_id = 1

    def test_add_task_success(self):
        """Test adding a valid task."""
        task = task_manager.add_task("Buy groceries")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Buy groceries")
        self.assertFalse(task.is_complete)
        self.assertEqual(len(task_manager.tasks), 1)

    def test_add_task_generates_sequential_ids(self):
        """Test ID generation is sequential."""
        task1 = task_manager.add_task("Task 1")
        task2 = task_manager.add_task("Task 2")
        task3 = task_manager.add_task("Task 3")
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)

    def test_add_task_invalid_description(self):
        """Test ValueError propagated for invalid description."""
        with self.assertRaises(ValueError):
            task_manager.add_task("")

    def test_get_all_tasks_empty(self):
        """Test getting tasks from empty list."""
        tasks = task_manager.get_all_tasks()
        self.assertEqual(tasks, [])

    def test_get_all_tasks_multiple(self):
        """Test getting multiple tasks."""
        task_manager.add_task("Task 1")
        task_manager.add_task("Task 2")
        tasks = task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].description, "Task 1")
        self.assertEqual(tasks[1].description, "Task 2")

    def test_get_task_by_id_found(self):
        """Test successful task lookup by ID."""
        task_manager.add_task("Task 1")
        task = task_manager.get_task_by_id(1)
        self.assertIsNotNone(task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Task 1")

    def test_get_task_by_id_not_found(self):
        """Test None returned for non-existent ID."""
        task = task_manager.get_task_by_id(999)
        self.assertIsNone(task)

    def test_update_task_success(self):
        """Test successful task update."""
        task_manager.add_task("Old description")
        updated = task_manager.update_task(1, "New description")
        self.assertIsNotNone(updated)
        self.assertEqual(updated.id, 1)
        self.assertEqual(updated.description, "New description")
        self.assertFalse(updated.is_complete)

    def test_update_task_not_found(self):
        """Test None returned when updating non-existent task."""
        result = task_manager.update_task(999, "New description")
        self.assertIsNone(result)

    def test_update_task_invalid_description(self):
        """Test ValueError propagated for invalid description."""
        task_manager.add_task("Old description")
        with self.assertRaises(ValueError):
            task_manager.update_task(1, "")

    def test_update_task_preserves_completion_status(self):
        """Test update preserves completion status."""
        task_manager.add_task("Task")
        task_manager.toggle_complete(1)
        updated = task_manager.update_task(1, "Updated task")
        self.assertTrue(updated.is_complete)

    def test_delete_task_success(self):
        """Test successful task deletion."""
        task_manager.add_task("Task to delete")
        result = task_manager.delete_task(1)
        self.assertTrue(result)
        self.assertEqual(len(task_manager.tasks), 0)

    def test_delete_task_not_found(self):
        """Test False returned when deleting non-existent task."""
        result = task_manager.delete_task(999)
        self.assertFalse(result)

    def test_delete_task_id_not_reused(self):
        """Test IDs are not reused after deletion."""
        task_manager.add_task("Task 1")
        task_manager.delete_task(1)
        task2 = task_manager.add_task("Task 2")
        self.assertEqual(task2.id, 2)

    def test_toggle_complete_to_complete(self):
        """Test toggling task from incomplete to complete."""
        task_manager.add_task("Task")
        result = task_manager.toggle_complete(1)
        self.assertIsNotNone(result)
        self.assertTrue(result.is_complete)

    def test_toggle_complete_to_incomplete(self):
        """Test toggling task from complete to incomplete."""
        task_manager.add_task("Task")
        task_manager.toggle_complete(1)
        result = task_manager.toggle_complete(1)
        self.assertIsNotNone(result)
        self.assertFalse(result.is_complete)

    def test_toggle_complete_not_found(self):
        """Test None returned when toggling non-existent task."""
        result = task_manager.toggle_complete(999)
        self.assertIsNone(result)

    def test_tasks_maintain_order(self):
        """Test tasks maintain insertion order."""
        task_manager.add_task("First")
        task_manager.add_task("Second")
        task_manager.add_task("Third")
        tasks = task_manager.get_all_tasks()
        self.assertEqual(tasks[0].description, "First")
        self.assertEqual(tasks[1].description, "Second")
        self.assertEqual(tasks[2].description, "Third")


if __name__ == "__main__":
    unittest.main()
