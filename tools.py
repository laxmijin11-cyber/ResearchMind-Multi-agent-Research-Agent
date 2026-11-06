from langchain.tools import tool
import requests

# online web search
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os

# file management system
from dotenv import load_dotenv
from rich import print

# terminal pe ache se dikhta result
load_dotenv()

# load the Tavily API key from the environment variable
# tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information.Returns titles,URLs and snippets
    """
    # load the Tavily API key from the environment variable
    tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    # call tavily search API
    results = tavily.search(query=query, max_results=5)
    # return results

    out = []
    for r in results["results"]:
        out.append(
            f'Title:{r["title"]}\nURL:{r["url"]}\nSnippet:{r["content"][:300]}\n'
        )

    return "\n-----\n".join(out)


# print(web_search.invoke("what are recent news of war?"))
# inspect mode se html se particular data scrape kar sakte ho!


@tool
def scrape_url(url: str) -> str:
    """
    Scrape the content of a given URL.
    IMPORTANT: The input MUST be a valid string URL starting with http or https.
    """
    try:
        response = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        # timeout yani 8 sec ke baad naa chale toh rehne do,headers se website ko batao ki hum browser se aa rahe hai
        soup = BeautifulSoup(response.text, "html.parser")
        # soup se html ko parse karenge
        # remove script and style elements
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[
            :3000
        ]  # return first 3000 characters of clean text
    except Exception as e:
        return f"Could not scrape the URL: {str(e)}"


# print(scrape_url.invoke("https://www.csis.org/programs/latest-analysis-war-iran"))
