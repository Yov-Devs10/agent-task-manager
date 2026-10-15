tasks = []

PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def view_tasks():
    if not tasks:
        print("\nNo tasks yet. The agency is quiet... for now.")
        return
    print("\n--- MISSION TASKS ---")
    for number, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{number}. {status} {task['title']} (priority: {task['priority']})")


def ask_for_index(prompt):
    """Ask for a task number (counting from 1). Return the list index, or None if invalid."""
    if not tasks:
        print("\nThere are no tasks yet.")
        return None
    try:
        number = int(input(prompt))
    except ValueError:
        print("Please enter a number.")
        return None
    if 1 <= number <= len(tasks):
        return number - 1
    print("No task with that number.")
    return None


def add_task():
    title = input("Task title: ").strip()
    if title == "":
        print("A task needs a title.")
        return
    priority = input("Priority (high/medium/low) [medium]: ").strip().lower()
    if priority not in PRIORITY_ORDER:
        priority = "medium"
    tasks.append({"title": title, "done": False, "priority": priority})
    print(f"Added: {title}")


def complete_task():
    view_tasks()
    index = ask_for_index("Number of the task to mark completed: ")
    if index is not None:
        tasks[index]["done"] = True
        print(f"Completed: {tasks[index]['title']}")


def remove_task():
    view_tasks()
    index = ask_for_index("Number of the task to remove: ")
    if index is not None:
        removed = tasks.pop(index)
        print(f"Removed: {removed['title']}")


def sort_by_priority():
    tasks.sort(key=lambda task: PRIORITY_ORDER[task["priority"]])
    print("Tasks sorted by priority.")


def main():
    print("Welcome, Agent. Your task list awaits.")
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Mark task completed")
        print("4. Remove task")
        print("5. Sort by priority")
        print("6. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            sort_by_priority()
        elif choice == "6":
            print("Mission accomplished. Goodbye, Agent.")
            break
        else:
            print("Invalid option, try again.")


main()
