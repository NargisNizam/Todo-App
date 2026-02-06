"""Command-line interface for Todo Application.

This module handles all user interaction, input validation, and output formatting.
"""

from todo_app.task import Task
from todo_app import task_manager


def display_menu() -> None:
    """Display the main menu."""
    print("\n========================================")
    print("      Todo Application - Phase I")
    print("========================================")
    print("\nMain Menu:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete/Incomplete")
    print("6. Exit")
    print()


def get_menu_choice() -> int | None:
    """Get and validate menu choice from user.

    Returns:
        int | None: Valid menu choice (1-6) or None if invalid
    """
    try:
        choice = int(input("Enter your choice (1-6): "))
        if 1 <= choice <= 6:
            return choice
        else:
            print("✗ Error: Invalid choice. Please enter a number between 1 and 6.")
            return None
    except ValueError:
        print("✗ Error: Invalid input. Please enter a number.")
        return None


def get_task_id() -> int | None:
    """Get and validate task ID from user.

    Returns:
        int | None: Valid task ID or None if invalid input
    """
    try:
        return int(input("Enter task ID: "))
    except ValueError:
        print("✗ Error: Invalid input. Please enter a numeric task ID.")
        return None


def get_task_description() -> str | None:
    """Get and validate task description from user.

    Returns:
        str | None: Valid description or None if invalid
    """
    description = input("Enter task description: ")
    description = description.strip()

    if not description:
        print("✗ Error: Task description cannot be empty.")
        return None

    if len(description) > 500:
        print("✗ Error: Task description cannot exceed 500 characters.")
        return None

    return description


def get_confirmation() -> bool:
    """Get yes/no confirmation from user.

    Returns:
        bool: True for yes, False for no
    """
    while True:
        response = input("Are you sure you want to delete this task? (y/n): ").lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("✗ Error: Invalid input. Please enter 'y' for yes or 'n' for no.")


def format_task_table(tasks: list[Task]) -> None:
    """Display tasks in table format.

    Args:
        tasks: List of tasks to display
    """
    print("\n=== Task List ===")

    if not tasks:
        print("No tasks found.")
        return

    print("ID  | Description              | Status")
    print("----|--------------------------|------------")

    for task in tasks:
        # Truncate description if too long for display
        description = task.description[:24] if len(task.description) > 24 else task.description
        status = "Complete" if task.is_complete else "Incomplete"
        print(f"{task.id:<3} | {description:<24} | {status}")

    print(f"\nTotal: {len(tasks)} tasks")


def display_task_details(task: Task) -> None:
    """Display detailed information about a task.

    Args:
        task: Task to display
    """
    print(f"  ID: {task.id}")
    print(f"  Description: {task.description}")
    status = "Complete" if task.is_complete else "Incomplete"
    print(f"  Status: {status}")


def display_success(message: str) -> None:
    """Display success message.

    Args:
        message: Success message to display
    """
    print(f"\n✓ {message}")


def display_error(message: str) -> None:
    """Display error message.

    Args:
        message: Error message to display
    """
    print(f"✗ Error: {message}")


def display_exit_message() -> None:
    """Display goodbye message when exiting."""
    print("\nThank you for using Todo Application!")
    print("Goodbye!")


def wait_for_enter() -> None:
    """Wait for user to press Enter."""
    print()
    input("Press Enter to continue...")


def handle_add_task(manager=task_manager) -> None:
    """Handle add task user flow.

    Args:
        manager: Task manager module (injected for testability)
    """
    print("\n=== Add New Task ===")
    description = get_task_description()

    if description is None:
        wait_for_enter()
        return

    try:
        task = manager.add_task(description)
        display_success("Task added successfully!")
        display_task_details(task)
    except ValueError as e:
        display_error(str(e))

    wait_for_enter()


def handle_view_tasks(manager=task_manager) -> None:
    """Handle view tasks user flow.

    Args:
        manager: Task manager module (injected for testability)
    """
    tasks = manager.get_all_tasks()
    format_task_table(tasks)
    wait_for_enter()


def handle_update_task(manager=task_manager) -> None:
    """Handle update task user flow.

    Args:
        manager: Task manager module (injected for testability)
    """
    print("\n=== Update Task ===")
    task_id = get_task_id()

    if task_id is None:
        wait_for_enter()
        return

    task = manager.get_task_by_id(task_id)
    if task is None:
        display_error("Task not found. Please enter a valid task ID.")
        wait_for_enter()
        return

    print(f"Current description: {task.description}")
    new_description = get_task_description()

    if new_description is None:
        wait_for_enter()
        return

    try:
        updated_task = manager.update_task(task_id, new_description)
        if updated_task is None:
            display_error("Task not found. Please enter a valid task ID.")
        else:
            display_success("Task updated successfully!")
            display_task_details(updated_task)
    except ValueError as e:
        display_error(str(e))

    wait_for_enter()


def handle_delete_task(manager=task_manager) -> None:
    """Handle delete task user flow.

    Args:
        manager: Task manager module (injected for testability)
    """
    print("\n=== Delete Task ===")
    task_id = get_task_id()

    if task_id is None:
        wait_for_enter()
        return

    task = manager.get_task_by_id(task_id)
    if task is None:
        display_error("Task not found. Please enter a valid task ID.")
        wait_for_enter()
        return

    print(f"Task: {task.description}")
    print()

    if not get_confirmation():
        print("Deletion cancelled.")
        wait_for_enter()
        return

    manager.delete_task(task_id)
    display_success("Task deleted successfully!")
    wait_for_enter()


def handle_toggle_complete(manager=task_manager) -> None:
    """Handle toggle complete user flow.

    Args:
        manager: Task manager module (injected for testability)
    """
    print("\n=== Mark Task Complete/Incomplete ===")
    task_id = get_task_id()

    if task_id is None:
        wait_for_enter()
        return

    task = manager.get_task_by_id(task_id)
    if task is None:
        display_error("Task not found. Please enter a valid task ID.")
        wait_for_enter()
        return

    current_status = "Complete" if task.is_complete else "Incomplete"
    print(f"Current status: {current_status}")

    updated_task = manager.toggle_complete(task_id)
    if updated_task is None:
        display_error("Task not found. Please enter a valid task ID.")
    else:
        new_status = "Complete" if updated_task.is_complete else "Incomplete"
        display_success(f"Task marked as {new_status}!")

    wait_for_enter()
