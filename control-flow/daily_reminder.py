task_description = input("Enter your task:")
task_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match task_priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task_description}' is a {task_priority} priority\ntask that requires immediate attention today!")  
        else:
            print(f"'{task_description}' is a {task_priority} priority\ntask but no immediate attention needed!")      
    case "low":
        if time_bound == "no":
            print(f"Note: '{task_description}' is a {task_priority} priority task. Consider\ncompleting it when youu have free time.")
        else:
            print(f"Note: '{task_description}' is a {task_priority} priority task but requires\nimmediate attention.")
    case "medium":
        if time_bound == "yes":
            print(f"NB: '{task_description}' is a {task_priority} priority task,\nbut need's to be completed asap.")
        else:
            print(f"NB: '{task_description}' is a {task_priority} priority task.\nIt can be completed after allocating some time to it.")
        
    