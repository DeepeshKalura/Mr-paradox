# import os
# import sys
# from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper
# from langchain_community.tools.wolfram_alpha import WolframAlphaQueryRun
# from langchain.agents import AgentExecutor, create_react_agent
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import SystemMessage
# from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder, HumanMessagePromptTemplate, PromptTemplate
# from langchain import hub


# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))
# import constant


# llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=1, google_api_key=os.getenv("GEMINI_API_KEY"))

# computational_tool = WolframAlphaQueryRun(api_wrapper=WolframAlphaAPIWrapper())

# tools = [computational_tool]

# message = [
#     SystemMessage(constant.explain_paradox),
#     HumanMessagePromptTemplate.from_template("{input}"),
#     MessagesPlaceholder(variable_name="agent_scratchpad"),
# ]
# chat_template = ChatPromptTemplate.from_messages(
#     messages=message,

# )


# # prompt_template = PromptTemplate.from_template(constant.explain_paradox)

# prompt = hub.pull("himmel/mr-paradox")



# def conversation(destination: str, time: str, money: str) -> str:
#     agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

#     agent_executor = AgentExecutor(agent=agent, tools=tools, )
#     print(agent_executor.execute({"input": f"destination: {destination}, time: {time}, money: {money}" }))
#     for i in range(5):
#         print()
#         human_message = input("User: ")
#         message.append(HumanMessagePromptTemplate(human_message))
#         ai_message = agent_executor.execute({"input": human_message})
#         print(f"Paradox: {ai_message}")
#         # message.append(SystemMessage(ai_message))


