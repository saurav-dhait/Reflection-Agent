from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import List, Sequence
from langgraph.graph import END, MessageGraph, START
import functools

load_dotenv()


def create_generate_agent():
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an essay assistant tasked with writing excellent 3-paragraph essays."
                " Generate the best essay possible for the user's request."
                " If the user provides critique, respond with a revised version of your previous attempts.",
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    llm = ChatGroq(
        temperature=0,
        model="llama3-70b-8192",
    )
    generate = prompt | llm
    return generate


def create_reflect_agent():
    reflection_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a teacher grading an essay submission. Generate critique and recommendations for the user's submission."
                " Provide detailed recommendations, including requests for length, depth, style, etc.",
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    llm = ChatGroq(
        temperature=0,
        model="llama3-70b-8192",
    )
    reflect = reflection_prompt | llm
    return reflect


def generation_node(state: Sequence[BaseMessage], generate):
    return generate.invoke({"messages": state})


def should_continue(state: List[BaseMessage]):
    if len(state) > 4:
        # End after 3 iterations
        return END
    return "reflect"


def reflection_node(messages: Sequence[BaseMessage], reflect) -> List[BaseMessage]:
    # Other messages we need to adjust
    cls_map = {"ai": HumanMessage, "human": AIMessage}
    # First message is the original user request. We hold it the same for all nodes
    translated = [messages[0]] + [
        cls_map[msg.type](content=msg.content) for msg in messages[1:]
    ]
    res = reflect.invoke({"messages": translated})
    # We treat the output of this as human feedback for the generator
    return HumanMessage(content=res.content)


def create_graph():
    partial_generation_node = functools.partial(generation_node, generate=create_generate_agent())
    partial_reflection_node = functools.partial(reflection_node, reflect=create_reflect_agent())

    builder = MessageGraph()
    builder.add_node("generate", partial_generation_node)
    builder.add_node("reflect", partial_reflection_node)
    builder.add_edge(START, "generate")

    builder.add_conditional_edges("generate", should_continue)
    builder.add_edge("reflect", "generate")
    graph = builder.compile()
    return graph


# graph = create_graph()
# for event in graph.stream(
#         [
#             HumanMessage(
#                 content="Generate an essay on the topicality of The Little Prince and its message in modern life"
#             )
#         ],
# ):
#     print(event)
#     print("---")
