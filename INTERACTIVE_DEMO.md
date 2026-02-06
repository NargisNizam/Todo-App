# Interactive Application Demo

## What You'll See When You Run the Application

### Step 1: Launch the Application

Run this command:
```bash
python -m todo_app.main
```

### Step 2: Main Menu Appears

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

Enter your choice (1-6): _
```

---

## Example Session Walkthrough

### Adding Your First Task

```
Enter your choice (1-6): 1

=== Add New Task ===
Enter task description: Buy groceries

✓ Task added successfully!
  ID: 1
  Description: Buy groceries
  Status: Incomplete

Press Enter to continue...
```

*Press Enter to return to menu*

---

### Viewing Your Tasks

```
Enter your choice (1-6): 2

=== Task List ===
ID  | Description              | Status
----|--------------------------|------------
1   | Buy groceries            | Incomplete

Total: 1 tasks

Press Enter to continue...
```

---

### Adding More Tasks

```
Enter your choice (1-6): 1

=== Add New Task ===
Enter task description: Finish project report

✓ Task added successfully!
  ID: 2
  Description: Finish project report
  Status: Incomplete

Press Enter to continue...
```

Add another:

```
Enter your choice (1-6): 1

=== Add New Task ===
Enter task description: Call dentist

✓ Task added successfully!
  ID: 3
  Description: Call dentist
  Status: Incomplete

Press Enter to continue...
```

---

### View All Tasks

```
Enter your choice (1-6): 2

=== Task List ===
ID  | Description              | Status
----|--------------------------|------------
1   | Buy groceries            | Incomplete
2   | Finish project report    | Incomplete
3   | Call dentist             | Incomplete

Total: 3 tasks

Press Enter to continue...
```

---

### Mark a Task Complete

```
Enter your choice (1-6): 5

=== Mark Task Complete/Incomplete ===
Enter task ID: 2
Current status: Incomplete

✓ Task marked as Complete!

Press Enter to continue...
```

Now view the list again:

```
Enter your choice (1-6): 2

=== Task List ===
ID  | Description              | Status
----|--------------------------|------------
1   | Buy groceries            | Incomplete
2   | Finish project report    | Complete
3   | Call dentist             | Incomplete

Total: 3 tasks

Press Enter to continue...
```

---

### Update a Task

```
Enter your choice (1-6): 3

=== Update Task ===
Enter task ID: 1
Current description: Buy groceries
Enter task description: Buy groceries and cook dinner

✓ Task updated successfully!
  ID: 1
  Description: Buy groceries and cook dinner

Press Enter to continue...
```

---

### Delete a Task

```
Enter your choice (1-6): 4

=== Delete Task ===
Enter task ID: 3
Task: Call dentist

Are you sure you want to delete this task? (y/n): y

✓ Task deleted successfully!

Press Enter to continue...
```

View final list:

```
Enter your choice (1-6): 2

=== Task List ===
ID  | Description              | Status
----|--------------------------|------------
1   | Buy groceries and cook... | Incomplete
2   | Finish project report    | Complete

Total: 2 tasks

Press Enter to continue...
```

---

### Error Handling Examples

**Empty Description:**
```
Enter your choice (1-6): 1

=== Add New Task ===
Enter task description:

✗ Error: Task description cannot be empty.

Press Enter to continue...
```

**Invalid Task ID:**
```
Enter your choice (1-6): 3

=== Update Task ===
Enter task ID: 999

✗ Error: Task not found. Please enter a valid task ID.

Press Enter to continue...
```

**Invalid Menu Choice:**
```
Enter your choice (1-6): 9

✗ Error: Invalid choice. Please enter a number between 1 and 6.

Enter your choice (1-6): _
```

**Non-Numeric Input:**
```
Enter your choice (1-6): abc

✗ Error: Invalid input. Please enter a number.

Enter your choice (1-6): _
```

---

### Exiting the Application

```
Enter your choice (1-6): 6

Thank you for using Todo Application!
Goodbye!
```

Application closes and returns to terminal.

---

## Key Features Demonstrated

✓ **Add Task** - Creates new tasks with unique IDs
✓ **View Tasks** - Displays all tasks in formatted table
✓ **Update Task** - Modifies task descriptions
✓ **Delete Task** - Removes tasks with confirmation
✓ **Toggle Complete** - Changes task completion status
✓ **Error Handling** - Graceful handling of invalid input
✓ **User-Friendly** - Clear messages and prompts

---

## Notes

- All data is **in-memory only** - lost when application closes
- Task IDs are **never reused** even after deletion
- Descriptions limited to **500 characters**
- Application runs in an **infinite loop** until you choose Exit
- Every operation returns you to the **main menu**

---

## To Start Your Session

```bash
cd C:\Users\HP\Desktop\TODO-APP\todo-app
python -m todo_app.main
```

Enjoy managing your tasks!
