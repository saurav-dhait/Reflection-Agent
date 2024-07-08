# Reflection Agent 
In the context of LLM agent building, reflection refers to the process of prompting an LLM to observe its past steps (along with potential observations from tools/the environment) to assess the quality of the chosen actions. This is then used downstream for things like re-planning, search, or evaluation.
## Project Structure

- `app.py`: This is the main script that contains the streamlit app.
- `reflection_graph.py`: This file contains langgraph code to create a reflection agent.

## Workflow

### 1. Initialization
The system initializes by loading necessary environment variables and importing required libraries. It also sets up the language model and tools needed for the task.

### 2. Planning
A `planner` component generates a step-by-step plan to achieve the given objective. This plan includes individual tasks that, when executed correctly, will lead to the desired outcome. The planner ensures that each step is clear and contains all necessary information.

### 3. Execution
An `agent executor` component is responsible for carrying out the tasks in the plan. It sequentially executes each step and collects the results. If the execution of a step fails or if new information necessitates a change in the plan, the system moves to the re-planning phase.

### 4. Re-planning
The `re-planner` component reviews the current plan, the steps already executed, and any issues encountered. It then updates the plan by adding new steps or modifying existing ones as needed. The goal is to ensure that the objective can still be achieved despite any setbacks.

### 5. Conditional Decision Making
The system includes logic to determine whether the process should continue with execution, move to re-planning, or end. This decision-making process is based on the current state of the plan and the results obtained from executing steps.


## Langgraph Graph structure

![image](https://github.com/saurav-dhait/Plan-and-Execute-Agent/blob/main/assets/graph.jpeg)
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