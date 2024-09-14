import os
from dotenv import load_dotenv

from crewai import Crew, Task, Agent, Process
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_ollama import OllamaLLM

load_dotenv()

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

llm = OllamaLLM(
  model="dolphin-llama3",
  base_url="http://localhost:11434"
)

user_query = input(">>> ")

# Define your agents with roles and goals
researcher = Agent(
  role='Internet Research Specialist',
  goal='Conduct comprehensive research across multiple online platforms and sources to gather relevant and diverse information on specified queries',
  backstory="""You are an experienced digital researcher with expertise in navigating the vast landscape of the internet. With years of experience exploring various online platforms, databases, and information sources, you have developed a keen eye for identifying relevant content, trending topics, and valuable insights across diverse digital ecosystems. Your expertise lies in efficiently filtering through enormous amounts of information to extract the most pertinent and reliable data for any given query. You are relentless in your pursuit of information, always willing to dig deeper and explore unconventional sources to uncover hidden gems of knowledge.""",
  verbose=1,
  llm=llm,
  allow_delegation=False,
  tools=[search_tool, web_rag_tool]
)

writer = Agent(
  role='Content Synthesizer and Analyst',
  goal='Analyze and synthesize research findings into coherent, insightful, and well-structured reports',
  backstory="""You are a skilled content creator with a background in data analysis and journalism. Your forte is taking complex, multi-faceted information and distilling it into clear, engaging, and informative content. You have a talent for identifying key themes, drawing connections between diverse pieces of information, and presenting findings in a way that is both accessible and comprehensive.""",
  verbose=1,
  llm=llm,
  allow_delegation=False
)

# Create tasks for your agents
task1 = Task(
  description=f"""Query: {user_query}. Conduct a thorough internet-wide search for information related to the given query. Explore multiple platforms including but not limited to search engines, academic databases, social media, forums, blogs, news sites, and specialized online communities. Identify key discussions, popular opinions, expert insights, controversies, and any unique perspectives. Collect data on content engagement (views, likes, shares, comments) to gauge topic popularity and impact. Ensure to cover a diverse range of sources to get a comprehensive view. Organize the findings by platform, theme, and relevance. Note any recurring patterns, significant outliers, or emerging trends in the data. Don't hesitate to dive into niche or lesser-known sources that might provide valuable information. If initial searches don't yield satisfactory results, try alternative search strategies, rephrase queries, or explore related topics to uncover more information. If you encounter validation errors make sure you read the error and fix your action input.""",
  expected_output="Comprehensive analysis in bullet points, including source links.",
  output_file="task1output.txt",
  agent=researcher
)

task2 = Task(
  description=f"""User query: {user_query}. Using the research findings provided, and user query create a well composed answer. Make sure it answers my query properly. If it is a Yes/NO type of question then just output Yes/No.""",
  expected_output="Text in simple english minimum 1 word and maximum 1000 words.",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=False,
  memory=False,
  process = Process.sequential
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)