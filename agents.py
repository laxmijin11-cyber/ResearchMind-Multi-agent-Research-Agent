from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
import os


# Change the global LLM to a builder function
def build_llm(groq_api_key):
    return ChatGroq(
        model="qwen/qwen3.8-27b",
        api_key=groq_api_key,
        temperature=0,
        max_tokens=1000,
    )


def build_search_agent(groq_api_key):
    llm = build_llm(groq_api_key)
    return create_agent(model=llm, tools=[web_search])


def build_reader_agent(groq_api_key):
    llm = build_llm(groq_api_key)
    return create_agent(model=llm, tools=[scrape_url])


# For the chains, we can't initialize them globally anymore.
# We will build them inside the pipeline function.
def build_writer_chain(groq_api_key):
    llm = build_llm(groq_api_key)
    writer_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert research writer. Write clear, structured, and insightful reports based on the information provided by the user and the research agent.",
            ),
            (
                "human",
                """
        Write a detailed report on the topic below.
        Topic: {topic}
        Research Gathered: {research}
        
        Structure the report as:
        - Introduction
        - Key findings (minimum 3 well-explained points)
        - Conclusion
        - Sources (list all URLs in the research)
        
        Be detailed, professional, and factual. Avoid making assumptions or adding information not present in the research.
        """,
            ),
        ]
    )
    return writer_prompt | llm | StrOutputParser()


def build_critic_chain(groq_api_key):
    llm = build_llm(groq_api_key)
    critic_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a sharp and constructive research critic. Be honest and specific.",
            ),
            (
                "human",
                """
        Review the research report below and evaluate it strictly.
        Report: {report}
        
        Respond in this exact format:
        Score: X/10
        Strengths:
        - ...
        - ...
        Areas to improve:
        - ...
        - ...
        One line verdict: ...
        """,
            ),
        ]
    )
    return critic_prompt | llm | StrOutputParser()
