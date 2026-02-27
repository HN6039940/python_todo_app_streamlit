FILEPATH = "todos_items.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath,"r",encoding="shift-jis") as file_local:
        todos = file_local.readlines()
        return todos

def write_todos(todos, filepath=FILEPATH):
    with open(filepath,"w",encoding="shift-jis") as file_local:
        file_local.writelines(todos)

if __name__ == "__main__":
    print(get_todos())