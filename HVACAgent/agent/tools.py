import os

from dotenv import load_dotenv
from langchain import agents
from langchain.base_language import BaseLanguageModel

from tools.calculate_pipe_length import calculate_pipe_length
from tools.system_arrangement import system_arrangement
from tools.parameter_search import ground_temperature_search_tool
from tools.docs_answering import FindContext
from tools.pipe_diagram import make_diagram
from tools.utils import Text, Doc, search_texts, load_texts

def make_tools(llm: BaseLanguageModel, verbose=False):
    load_dotenv()

    all_tools = agents.load_tools([ "human", "llm-math"], llm)

    # add visualization tools

    all_tools += [system_arrangement(),
                    calculate_pipe_length(),
                    ground_temperature_search_tool(),
                    FindContext(),
                    make_diagram()
    ]

    # add registry tools

    # add literature search tool
 
    return all_tools