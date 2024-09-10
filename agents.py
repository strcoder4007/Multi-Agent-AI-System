import os
from crewai import Crew, Task, Agent, Process
from crewai_tools import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI


from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.chat_models.huggingface import ChatHuggingFace

# Get the Hugging Face token
huggingface_token = "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"

# Initialize the Hugging Face model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3.1-8B-Instruct",  # Replace with the model you want to use
    huggingfacehub_api_token=huggingface_token
)


# os.environ["GOOGLE_API_KEY"] = "AIzaSyAdvi5FDIVPLUokRD4KBjve4UdfZOSmbVo"
os.environ["SERPER_API_KEY"] = "29e9856df645a3ac5c5bcb6bdad3e582be0322fa"
# os.environ["HUGGINGFACE_TOKEN"] = "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"


# # Create the first LLM
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-pro",
#     temperature=0,
#     max_tokens=300,
#     timeout=None,
#     max_retries=2
# )

search_tool = SerperDevTool()

user_query = input("Search Reddit: ")

# Define your agents with roles and goals
researcher = Agent(
  role='Reddit Research Specialist',
  goal='Conduct comprehensive research across multiple subreddits to gather relevant and diverse information on specified queries',
  backstory="""You are an experienced digital anthropologist specializing in Reddit communities. With years of experience navigating the complex ecosystem of subreddits, you have developed a keen eye for identifying relevant discussions, trending topics, and valuable insights across various communities. Your expertise lies in efficiently filtering through vast amounts of information to extract the most pertinent and reliable data for any given query.""",
  verbose=True,
  llm=llm,
  allow_delegation=False,
  tools=[search_tool]
)

writer = Agent(
  role='Content Synthesizer and Analyst',
  goal='Analyze and synthesize research findings into coherent, insightful, and well-structured reports',
  backstory="""You are a skilled content creator with a background in data analysis and journalism. Your forte is taking complex, multi-faceted information and distilling it into clear, engaging, and informative content. You have a talent for identifying key themes, drawing connections between diverse pieces of information, and presenting findings in a way that is both accessible and comprehensive.""",
  verbose=0,
  llm=llm,
  allow_delegation=False
)

# Create tasks for your agents
task1 = Task(
  description=f"""Query: {user_query}. Search across multiple relevant subreddits for information related to the given query. Identify key discussions, popular opinions, controversies, and any unique insights. Collect data on post engagement (upvotes, comments) to gauge topic popularity. Ensure to cover a diverse range of subreddits to get a comprehensive view. Organize the findings by subreddit, theme, and relevance. Note any recurring patterns or significant outliers in the data.""",
  expected_output="Full analysis in bullet points",
  output_file="task1output.txt",
  agent=researcher
)

task2 = Task(
  description=f"""User query: {user_query}. Using the research findings provided, and user query create a well composed answer. Make sure it answers my query properly.""",
  expected_output="Text in simple english max 200 words.",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=0,
  process = Process.sequential
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)