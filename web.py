import streamlit as st
from functions import *


todos = read_file()


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(f'{new_todo}\n')
    write_file(todos)
    clean_input()


def clean_input():
    pass


st.title("My Todo App")


for todo in todos:
    is_checkbox = st.checkbox(todo, key=todo)
    print(is_checkbox)
    if is_checkbox:
        find_todo = find_todo_func(todo, todos)
        todos.pop(find_todo)
        write_file(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")


