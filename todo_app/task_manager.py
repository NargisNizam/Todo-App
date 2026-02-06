"""Task manager for business logic and in-memory storage.

This module handles CRUD operations, ID generation, and task storage.
"""

from todo_app.task import Task

# In-memory task storage (cleared on application exit)
tasks: list[Task] = []

# ID generation counter (never decreases, ensures unique IDs)
_next_id: int = 1


def _generate_id() -> int:
    """Generate next unique task ID.

    Uses a simple auto-increment counter starting at 1.
    IDs are never reused, even after task deletion.

    Returns:
        int: Next available task ID
    """
    global _next_id
    task_id = _next_id
    _next_id += 1
    return task_id


def add_task(description: str) -> Task:
    """Add a new task to the task list.

    Args:
        description: Task description text

    Returns:
        Task: The newly created task

    Raises:
        ValueError: If description is invalid (propagated from Task)
    """
    task_id = _generate_id()
    task = Task(id=task_id, description=description)
    tasks.append(task)
    return task


def get_all_tasks() -> list[Task]:
    """Get all tasks in order of creation.

    Returns:
        list[Task]: Copy of all tasks (oldest first)
    """
    return tasks.copy()


def get_task_by_id(task_id: int) -> Task | None:
    """Find a task by its ID.

    Uses linear search through the task list.

    Args:
        task_id: Task ID to search for

    Returns:
        Task | None: Task if found, None otherwise
    """
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def update_task(task_id: int, new_description: str) -> Task | None:
    """Update a task's description.

    Args:
        task_id: ID of task to update
        new_description: New description text

    Returns:
        Task | None: Updated task if found, None otherwise

    Raises:
        ValueError: If new_description is invalid (propagated from Task)
    """
    for i, task in enumerate(tasks):
        if task.id == task_id:
            # Create new task with same ID and completion status
            updated_task = Task(
                id=task_id,
                description=new_description,
                is_complete=task.is_complete
            )
            tasks[i] = updated_task
            return updated_task
    return None


def delete_task(task_id: int) -> bool:
    """Delete a task from the task list.

    Args:
        task_id: ID of task to delete

    Returns:
        bool: True if task was deleted, False if not found
    """
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return True
    return False


def toggle_complete(task_id: int) -> Task | None:
    """Toggle a task's completion status.

    Args:
        task_id: ID of task to toggle

    Returns:
        Task | None: Updated task if found, None otherwise
    """
    task = get_task_by_id(task_id)
    if task is None:
        return None

    # Toggle the completion status
    task.is_complete = not task.is_complete
    return task
