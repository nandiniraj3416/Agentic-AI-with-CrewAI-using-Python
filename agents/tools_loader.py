"""
Tool Loader - Load tools from tools package

This module provides compatibility with the agents module by importing
from the centralized tools package.

It delegates all tool loading to tools.tools module.
"""

from tools import (
    load_tools_as_tuple,
    get_search_tool_lazy,
    get_scrape_tool_lazy,
)


def load_tools():
    """
    Initialize and return tools for agents.
    
    Returns:
        tuple: (search_tool, scrape_tool)
        
    Delegates to: tools.tools.load_tools_as_tuple()
    """
    return load_tools_as_tuple()


def get_search_tool():
    """
    Get only the search tool with lazy loading.
    
    Returns:
        SerperDevTool: Configured search tool
    """
    return get_search_tool_lazy()


def get_scrape_tool():
    """
    Get only the scrape tool with lazy loading.
    
    Returns:
        ScrapeWebsiteTool: Configured scrape tool
    """
    return get_scrape_tool_lazy()
