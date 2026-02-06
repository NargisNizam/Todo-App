# Quick Start Guide - Todo Application Phase I

## Installation

No installation required! The application uses only Python standard library.

## Requirements

- Python 3.10 or higher

## Running the Application

### Option 1: Run from command line

```bash
cd todo-app
python -m todo_app.main
```

### Option 2: Run demo test

To see the application in action without manual input:

```bash
cd todo-app
python demo_test.py
```

## Running Tests

### All tests
```bash
python -m unittest discover tests
```

### With verbose output
```bash
python -m unittest discover tests -v
```

### Individual test files
```bash
python -m unittest tests.test_task
python -m unittest tests.test_task_manager
python -m unittest tests.test_integration
```

## Quick Tutorial

When you run the application, you'll see this menu:

```
========================================
      Todo Application - Phase I
========================================

Main Menu:
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

Enter your choice (1-6):
```

### Try These Steps:

1. **Add a task**: Select option 1, enter "Buy groceries"
2. **View tasks**: Select option 2 to see your task list
3. **Mark complete**: Select option 5, enter task ID 1
4. **View again**: Select option 2 to see the status changed
5. **Exit**: Select option 6 to close the application

## Features

- ✓ Add tasks with descriptions (1-500 characters)
- ✓ View all tasks in a formatted table
- ✓ Update task descriptions
- ✓ Delete tasks (with confirmation)
- ✓ Toggle task completion status
- ✓ Error handling for invalid input

## Important Notes

- **No Persistence**: All data is stored in memory only
- **Data is Lost**: When you close the application, all tasks are deleted
- **Single User**: This is a local, single-user application

## Troubleshooting

### "Module not found" error
Make sure you're in the `todo-app` directory and running with `python -m todo_app.main`

### Python version
Check your Python version:
```bash
python --version
```
Must be 3.10 or higher

### Tests failing
Ensure you're in the `todo-app` directory when running tests

## File Locations

```
todo-app/
├── todo_app/          # Application source code
│   ├── main.py        # Run this to start the app
│   ├── task.py        # Task data model
│   ├── task_manager.py # Business logic
│   └── cli.py         # User interface
├── tests/             # Test files
├── README.md          # Full documentation
├── demo_test.py       # Automated demo
└── QUICKSTART.md      # This file
```

## Next Steps

- Read `README.md` for complete documentation
- Read `PHASE_I_SPECIFICATION.md` for detailed feature specifications
- Read `PHASE_I_VERIFICATION.md` for test results and verification

## Support

This is Phase I of a 5-phase project. For questions about features or behavior, refer to the specification documents in the project root.
