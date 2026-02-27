import streamlit as st
from function import get_todos,write_todos
todos = get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)

def complete_todo():
    todo = st.session_state
    todo_index = int([index for index, item in todo.items() if item == True][0])
    todos.pop(todo_index)
    write_todos(todos)

st.title("Todo App")
st.subheader("Todos")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    todo = todo.replace("\n", "")
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if  checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[f"{todo}_{index}"]
        st.session_state["new_todo"] = ""
        st.rerun()


st.text_input(" ", label_visibility="hidden", placeholder="Enter your productivity here",
              on_change=add_todo, key="new_todo")