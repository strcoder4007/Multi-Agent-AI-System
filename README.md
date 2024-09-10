# Reddit Multi-Agent AI Research System

## Overview

This project implements a sophisticated multi-agent AI system designed to conduct comprehensive research across various subreddits based on user queries. Utilizing CrewAI, Langchain, and the Gemini API, this system automates the process of gathering, analyzing, and synthesizing information from Reddit, providing users with well-structured and insightful reports.

## Features

- **Dynamic Query Processing**: Accepts user-defined queries for targeted Reddit research.
- **Multi-Subreddit Analysis**: Searches across multiple relevant subreddits to gather diverse perspectives.
- **Engagement Metrics**: Collects and analyzes post engagement data (upvotes, comments) to gauge topic popularity.
- **Comprehensive Reporting**: Generates detailed reports synthesizing findings into coherent, insightful content.
- **Scalable Agent Architecture**: Utilizes specialized AI agents for research and content creation tasks.

## Technologies

- [CrewAI](https://github.com/joaomdmoura/crewAI): For orchestrating multiple AI agents.
- [Langchain](https://github.com/hwchase17/langchain): For building applications with large language models.
- [Gemini API](https://ai.google.dev/docs): Google's advanced language model for natural language processing tasks.


![Multi Agent AI System Architecture](/image.jpg)

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/reddit-multi-agent-ai.git
    cd reddit-multi-agent-ai
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Set up API keys:
- Create a `.env` file in the project root.
- Add your API keys:
  ```
  OPENAI_API_KEY=your_openai_api_key
  GOOGLE_CSE_ID=your_google_cse_id
  GOOGLE_API_KEY=your_google_api_key
  ```

## Usage

Run the main script:
```
python agent.py
```

Follow the prompts to enter your research query. The system will then:
1. Conduct research across relevant subreddits.
2. Analyze the gathered information.
3. Generate a comprehensive report based on the findings.

## System Architecture

- **Reddit Research Specialist**: An AI agent specialized in navigating and extracting relevant information from various subreddit communities.
- **Content Synthesizer and Analyst**: An AI agent focused on analyzing research findings and creating coherent, insightful reports.

## Output

The system produces two main outputs:
1. A detailed bullet-point analysis of the research findings.
2. A comprehensive blog post synthesizing the gathered information.

## Future Enhancements

1. Implement RAG (Retrieval-Augmented Generation) support for improved context and accuracy.
2. Develop a user-friendly web interface for easier interaction with the system.
3. Expand support for multiple, interconnected tasks to handle more complex research scenarios.
4. Integrate with Reddit API for direct data access and more comprehensive analysis.

## Contributing

Contributions to improve the system are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.