import streamlit as st
import functions as f

tasks = f.get_list_from_file(f.TODO_FILEPATH)
tasks = [t.title() for t in tasks]


def add_task():
    todo = st.session_state["new_task"].title() + '\n'
    tasks.append(todo)
    f.write_list_to_file(tasks, f.TODO_FILEPATH)


st.title("My To-Do List App")
st.subheader("Increase your productivity")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        f.write_list_to_file(tasks, f.TODO_FILEPATH)
        del st.session_state[task]
        st.experimental_rerun()

st.text_input(label="Enter a new task: ",
              on_change=add_task, key="new_task")

