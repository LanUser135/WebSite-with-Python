FILE_PATH = "./todos.txt"


def number_of_task():
    """
    Enter a number of the task
    :return:
    """
    return int(input("Enter a number of a task: ")) - 1


def read_file(filepath_local=FILE_PATH):
    """
    Read a text file and return the list of tasks
    :param filepath_local:
    :return:
    """
    with open(filepath_local, "r") as file:
        # return a list of tasks
        todos_local = file.readlines()
        return todos_local


def write_file(todos_local, filepath_local=FILE_PATH):

    # DOK Strings are useful to explain what function does.
    """
    This is used for writing new todos into the list
    :param todos_local:
    :param filepath_local:
    :return:
    """
    with open(filepath_local, "w") as file:
        file.writelines(todos_local)

# The code below is executed only in this file, not anywhere else.
# It's the point of the __main__ it is replaced with actual name of the file
# functions.py in the case.


def add_space(values):
    return values["todo"] + "\n"


def extract_value(values):
    return values["todos"][0]


def update_display(values, window):
    return window["todos"].update(values=values)


def remove_input(window):
    return window['todo'].update(value="")


def find_todo_func(value, todo):
    return todo.index(value)


def update_function(todos, window):
    write_file(todos)
    update_display(todos, window)
    remove_input(window)

if __name__ == "__main__":
    print("I won't be executed anywhere except of here!")

