from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import asyncio
from pathlib import Path

load_dotenv()

async def main():
    base_dir = Path(__file__).resolve().parent
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [str(base_dir / "mathserver.py")],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable-http",
            },
        }
    )

    tools = await client.get_tools()
    llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
    agent = create_react_agent(llm, tools)

    response = await agent.ainvoke({
        "messages": [{"role": "user", "content": "What is 5 + 3?"}]
    })
    print("Math Response:", response["messages"][-1].content)

    response = await agent.ainvoke({
        "messages": [{"role": "user", "content": "What is the weather in New York?"}]
    })
    print("Weather Response:", response["messages"][-1].content)

asyncio.run(main())