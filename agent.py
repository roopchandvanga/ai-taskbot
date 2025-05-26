from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_community.utilities import SerpAPIWrapper
from config import OPENAI_API_KEY, SERPAPI_API_KEY
from audio import listen

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=OPENAI_API_KEY)

# Initialize Tools
search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)

def write_to_file(input_string):
    if "|" not in input_string:
        filename = "output.txt"
        content = input_string
    else:
        filename, content = input_string.split("|", 1)
        filename = filename.strip()
        content = content.strip()

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Saved to {filename}"


tools = [
    Tool(name="Search", func=search.run, description="Search the web"),
    Tool(name="Python", func=PythonREPLTool().run, description="Run Python code"),
    Tool(
    name="FileWriter",
    func=write_to_file,
    description="Write text to a file. Input should be in the format 'filename.txt|content'. For example: 'books.txt|Learn Python the Hard Way\nAutomate the Boring Stuff'"
)
]

# Initialize Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Command loop
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        try:
            response = agent.run(user_input)
            print("Agent:", response)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    while True:
        user_input = listen()  # Voice input instead of text input
        if not user_input or user_input.lower() in ["exit", "quit"]:
            break
        try:
            response = agent.run(user_input) #response = agent.invoke(user_input)
            print("Agent:", response)
            #display_to_glasses(response)
        except Exception as e:
            print("Error:", e)
