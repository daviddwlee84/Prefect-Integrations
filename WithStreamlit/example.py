import streamlit as st
import prefect

st.title("Prefect Test")

# NOTE: st.session_state can't be used with Prefect
# if "messages" not in st.session_state:
#     st.session_state["messages"] = []


@prefect.task(name="flow1_task1")
def task1():
    # NOTE: wrapped with prefect.task won't show the toast
    st.toast("execute task 1")
    # st.session_state["messages"].append("execute task 1")


def task2():
    # NOTE: this toast will be shown
    st.toast("execute task 2")


@prefect.flow(name="flow1")
def flow1():
    # NOTE: this toast will be shown
    st.toast("execute flow 1")
    # st.session_state["messages"].append("execute flow 1")
    task1()
    task2()


st.button("Trigger function 1", on_click=flow1)

# with st.chat_message("user"):
#     for msg in st.session_state["messages"]:
#         st.write(msg)
