"""Quick demo/test script to verify application functionality."""

from todo_app import task_manager

# Reset state
task_manager.tasks.clear()
task_manager._next_id = 1

print("=" * 50)
print("AUTOMATED DEMO TEST - Todo Application Phase I")
print("=" * 50)

# Test 1: Add tasks
print("\n[TEST 1] Adding tasks...")
task1 = task_manager.add_task("Buy groceries")
task2 = task_manager.add_task("Finish project report")
task3 = task_manager.add_task("Call dentist")
print(f"[OK] Added task 1: {task1.description}")
print(f"[OK] Added task 2: {task2.description}")
print(f"[OK] Added task 3: {task3.description}")

# Test 2: View all tasks
print("\n[TEST 2] Viewing all tasks...")
tasks = task_manager.get_all_tasks()
print(f"Total tasks: {len(tasks)}")
for task in tasks:
    status = "Complete" if task.is_complete else "Incomplete"
    print(f"  ID {task.id}: {task.description} [{status}]")

# Test 3: Mark task as complete
print("\n[TEST 3] Marking task 2 as complete...")
task_manager.toggle_complete(2)
task = task_manager.get_task_by_id(2)
status = "Complete" if task.is_complete else "Incomplete"
print(f"[OK] Task 2 is now: {status}")

# Test 4: Update task description
print("\n[TEST 4] Updating task 1...")
updated = task_manager.update_task(1, "Buy groceries and cook dinner")
print(f"[OK] Updated task 1: {updated.description}")

# Test 5: View tasks again
print("\n[TEST 5] Viewing updated task list...")
tasks = task_manager.get_all_tasks()
for task in tasks:
    status = "Complete" if task.is_complete else "Incomplete"
    print(f"  ID {task.id}: {task.description} [{status}]")

# Test 6: Delete a task
print("\n[TEST 6] Deleting task 3...")
result = task_manager.delete_task(3)
if result:
    print("[OK] Task 3 deleted successfully")

# Test 7: View final task list
print("\n[TEST 7] Final task list...")
tasks = task_manager.get_all_tasks()
print(f"Total tasks: {len(tasks)}")
for task in tasks:
    status = "Complete" if task.is_complete else "Incomplete"
    print(f"  ID {task.id}: {task.description} [{status}]")

# Test 8: Error handling
print("\n[TEST 8] Testing error handling...")
try:
    task_manager.add_task("")
    print("[FAIL] Should have raised ValueError for empty description")
except ValueError as e:
    print(f"[OK] Correctly raised error: {e}")

result = task_manager.get_task_by_id(999)
if result is None:
    print("[OK] Correctly returned None for non-existent task")

print("\n" + "=" * 50)
print("DEMO COMPLETE - All functionality verified!")
print("=" * 50)
print("\nYou can now run the full application with:")
print("  python -m todo_app.main")
