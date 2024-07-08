import streamlit as st
from reflection_graph import create_graph
from langchain_core.messages import HumanMessage


def main():
    st.set_page_config(page_title="Reflection-Agent",
                       page_icon="🤖",
                       layout="centered",
                       initial_sidebar_state="expanded",
                       menu_items=None)
    # sidebar
    with st.sidebar:
        st.subheader("Chat options ")
        clear_chat = st.button("Clear chat", type="primary")

    # main body
    st.title("🤖 Reflection-Agent : ")
    if clear_chat:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hey, how can i help you ? "}]
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hey, how can i help you ? "}]
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).markdown(msg["content"], unsafe_allow_html=True)
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = "No response"
        with st.spinner(f"Generating response"):
            graph = create_graph()
            for event in graph.stream(
                    [
                        HumanMessage(
                            content=prompt
                        )
                    ],
            ):
                b = event.popitem()
                response = b[1].content
                name = b[0]
                match name:
                    case "generate":
                        styled_list = f"""
                            <h4 style='margin:0;padding :0;'>📃Generate : </h4><br>
                            <div style='font-family: Arial; font-size: 18px; color: #4CAF50;'>
                                {response}
                            </div>
                        """
                        a = {"role": "assistant", "content": styled_list}
                        st.session_state.messages.append(a)
                        st.chat_message(a["role"]).markdown(a["content"], unsafe_allow_html=True)
                    case "reflect":
                        styled_list = f"""
                            <h4 style='margin:0;padding :0;'>🔍Reflect : </h4><br>
                            <div style='font-family: Arial; font-size: 18px; color: #4CAF50;'>
                                {response}
                            </div>
                        """
                        a = {"role": "assistant", "content": styled_list}
                        st.session_state.messages.append(a)
                        st.chat_message(a["role"]).markdown(a["content"], unsafe_allow_html=True)


if __name__ == '__main__':
    main()
