
# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Start processing using match-case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Schedule it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that should be handled today.")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Complete it when your schedule allows.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task but still needs attention today.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("\nInvalid priority level entered. Please use high, medium, or low.")
