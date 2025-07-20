# Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task using match-case based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Reminder: '{task}' has an undefined priority."

# Modify the reminder if time-bound is yes
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print final reminder
print(reminder)
