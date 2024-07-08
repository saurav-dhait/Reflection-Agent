# Reflection Agent 
In the context of LLM agent building, reflection refers to the process of prompting an LLM to observe its past steps (along with potential observations from tools/the environment) to assess the quality of the chosen actions. This is then used downstream for things like re-planning, search, or evaluation.
## Project Structure

- `app.py`: This is the main script that contains the streamlit app.
- `reflection_graph.py`: This file contains langgraph code to create a reflection agent.
## Features 
- `Reflection and Feedback`: Provides detailed critique and recommendations to improve the essay.
- `Feedback Loop`: Iteratively improves the essay based on the provided feedback.

## Explanation

- `create_generate_agent`: Creates the essay generation agent using the ChatGroq model.
- `create_reflect_agent`: Creates the reflection agent that provides feedback on the essay.
- `generation_node`: Handles the essay generation step.
- `should_continue`: Determines whether to continue the feedback loop or end it.
- `reflection_node`: Handles the reflection and feedback step.
- `create_graph`: Builds the message graph and sets up the feedback loop.


## Langgraph Graph structure

![image](https://github.com/saurav-dhait/Reflection-Agent/blob/main/assets/graph.png)
## Requirements

Ensure you have the following Python packages installed:

- streamlit
- langchain
- langgraph
- python-dotenv 
- langchain-groq

You can install the required packages using the following command:

```sh
pip install -r requirements.txt
```

## Running the code
- To run the project, execute the following command (make sure you are in the project directory):

```sh
streamlit run app.py
```

## Acknowledgements
This project is inspired by various tutorials and resources available for Multi-Agent Systems.