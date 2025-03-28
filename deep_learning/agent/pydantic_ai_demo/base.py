from pydantic_ai import Agent
import os

os.environ["GEMINI_API_KEY"] = ""

agent = Agent(
    "gemini-1.5-pro",
    system_prompt="Be concise, reply with one sentence.",
)

result = agent.run_sync('Where does "hello world" come from?')
print(result.data)
