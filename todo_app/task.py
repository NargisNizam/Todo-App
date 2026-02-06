"""Task data model for Todo Application.

This module defines the Task class with field validation.
"""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a single todo task.

    Attributes:
        id: Unique task identifier (positive integer)
        description: Task description text (1-500 characters after trimming)
        is_complete: Completion status (True for complete, False for incomplete)
    """

    id: int
    description: str
    is_complete: bool = False

    def __post_init__(self) -> None:
        """Validate task fields after initialization.

        Raises:
            ValueError: If description is empty or exceeds 500 characters
        """
        # Validate description is not empty or whitespace-only
        if not self.description or not self.description.strip():
            raise ValueError("Task description cannot be empty")

        # Validate description length after trimming
        if len(self.description) > 500:
            raise ValueError("Task description cannot exceed 500 characters")

        # Trim whitespace from description
        self.description = self.description.strip()
