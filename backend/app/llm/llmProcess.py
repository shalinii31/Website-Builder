# from app.llm.prompt import build_prompt
# from app.llm.llm_config import llm
# from app.history import add_to_history
# from app.tools.Tools import tools

# from langchain.agents import create_agent


# # Create agent with LLM + website tools
# agent = create_agent(
#     model=llm,
#     tools=tools,
# )


# def llm_processing(query: str) -> str:

#     prompt = build_prompt(query=query)

#     response = agent.invoke({
#         "messages": [
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     })

#     result = response["messages"][-1].content

#     add_to_history("user", query)
#     add_to_history("assistant", result)

#     print("diagnostic:", result)

#     return result












from app.llm.prompt import build_prompt
from app.llm.llm_config import llm
from app.history import add_to_history
from app.tools.Tools import tools

from langchain.agents import create_agent


agent = create_agent(
    model=llm,
    tools=tools,
)


def llm_processing(query: str) -> str:

    prompt = build_prompt(query=query)

    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })

    content = response["messages"][-1].content

    # Gemini may return content as a list of blocks
    if isinstance(content, list):
        result = " ".join(
            block.get("text", "")
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        ).strip()
    else:
        result = str(content)

    add_to_history("user", query)
    add_to_history("assistant", result)

    print("diagnostic:", result)

    return result