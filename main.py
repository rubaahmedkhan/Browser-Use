from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio
from pydantic import SecretStr
import os

os.environ["ANONYMIZED_TELEMETRY"] = "false"

api_key = "AIzaSyCGfC8gVqltAStzbfVJK2JXoYknF8ErtKQ"

llm = ChatGoogleGenerativeAI(api_key=SecretStr(api_key), model="gemini-1.5-flash")

async def main():
    agent = Agent(
        task="go to google and search for 'Python tutorial for beginners' and open the first blog post link",
        llm=llm
    )
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
