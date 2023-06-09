from flask import Flask, request
from langchain import OpenAI, Wikipedia
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.agents.react.base import DocstoreExplorer
docstore=DocstoreExplorer(Wikipedia())

app = Flask(__name__)

def create_auto_agent():
    # Create the agent
    tools = [
    Tool(
        name="Search",
        func=docstore.search,
        description="useful for when you need to ask with search"
    ),
    Tool(
        name="Lookup",
        func=docstore.lookup,
        description="useful for when you need to ask with lookup"
    )
]

llm = OpenAI(temperature=0, model_name="text-davinci-003")

react = initialize_agent(tools, llm, agent=AgentType.REACT_DOCSTORE, verbose=True)

    return agent

@app.route("/agent")
def agent():
    task = request.args.get("task")
    macaroon = request.args.get("macaroon")

    agent = create_auto_agent()

    response = agent.run(task)

  # Return the response
    return response

if __name__ == "__main__":
    app.run(debug=True)
