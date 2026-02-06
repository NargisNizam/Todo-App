"""Main entry point for Todo Application.

This module contains the main application loop and orchestrates
CLI and task manager interactions.
"""

from todo_app import cli
from todo_app import task_manager


def main() -> None:
    """Main application loop.

    Displays menu, gets user choice, and dispatches to appropriate handler.
    Continues until user selects Exit option.
    """
    while True:
        cli.display_menu()
        choice = cli.get_menu_choice()

        if choice is None:
            continue

        if choice == 1:
            cli.handle_add_task(task_manager)
        elif choice == 2:
            cli.handle_view_tasks(task_manager)
        elif choice == 3:
            cli.handle_update_task(task_manager)
        elif choice == 4:
            cli.handle_delete_task(task_manager)
        elif choice == 5:
            cli.handle_toggle_complete(task_manager)
        elif choice == 6:
            cli.display_exit_message()
            break


if __name__ == "__main__":
    main()
