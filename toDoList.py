def addTasks():
    addTask = input("Enter task to add: ")
    with open("Tasks.txt", "a") as taskFile:
        taskFile.write(addTask + "\n")
def showTasks():
    with open("Tasks.txt","r") as taskFile:
        listofTasks = taskFile.readlines()
        taskNum = 1
        for i in listofTasks:
            print(f"Task {taskNum}: {i}",end="")
            taskNum += 1
def markComplete():
    taskNums = input("Enter task numbers to mark complete: ")
    linesToComplete = [int(n.strip()) for n in taskNums.split(",")]
    with open("Tasks.txt","r") as taskFile:
        lines = taskFile.readlines()
    for i in range(len(lines)):
        if (i+1) in linesToComplete:
            if not lines[i].strip().endswith("completed"):
                lines[i] = lines[i].strip() + " completed\n"
                print(f"Task{i} marked completed!\n")
    with open("Tasks.txt","w") as taskFile:
        taskFile.writelines(lines)
def deleteTask():
    taskNums = input("Enter task numbers to delete: ")
    linesToDelete = [int(n.strip()) for n in taskNums.split(",")]
    with open("Tasks.txt","r") as taskFile:
        lines = taskFile.readlines()
    i = 0
    newlines = []
    for i in range(len(lines)):
        if i+1 not in linesToDelete:
            newlines.append(lines[i])
        else:
            print(f"Task{i} deleted!\n")
    with open("Tasks.txt","w") as taskFile:
        taskFile.writelines(newlines)
while(True):
    print("\n---To-do-list by Athar Minallah---\n")
    command = input("'e' to exit\n'a' to add tasks\n's' to showtasks\n'c' to mark complete\n'd' to delete task\nEnter: ")
    if command == 'e':
        break
    elif command == 'a':
        addTasks()
        print("Task added to the list successfully!\n")
    elif command == 's':
        print("\nHere is your to-do-list: ")
        showTasks()
    elif command == 'c':
        markComplete()
    elif command == 'd':
        deleteTask()