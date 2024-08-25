import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("My list of things to do.")
#st.write("This is for simple text")

incrementor = 1
for todo in todos:
    st.checkbox(todo, key=incrementor)
    incrementor = incrementor + 1

st.text_input(label="", placeholder="Add something to do: ")