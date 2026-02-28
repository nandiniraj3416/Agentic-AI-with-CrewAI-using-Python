"""
Tools Management - Initialize and manage all external tools

This module manages all tools used by agents in the LinkedIn Content Manager.

Available Tools:
1. SerperDevTool: Web search capability
   - Used by: Trend Researcher Agent
   - Purpose: Search for trending topics, hashtags, and viral content
   - Requires: SERPER_API_KEY in environment

2. ScrapeWebsiteTool: Website scraping capability
   - Used by: Trend Researcher Agent
   - Purpose: Scrape website content for research insights
   - Requires: Internet connectivity

Tool Configuration:
- All tools are initialized on-demand when needed
- Each tool has error handling for API failures
- Tools can be individually accessed or loaded together
"""

import os
import sys
from crewai_tools import SerperDevTool, ScrapeWebsiteTool


# ============================================================================
# TOOL INITIALIZATION
# ============================================================================

def _verify_api_keys():
    """
    Verify that required API keys are set in environment.
    
    Returns:
        bool: True if all required keys are present
        
    Raises:
        SystemExit: If required keys are missing
    """
    serper_key = os.getenv("SERPER_API_KEY")
    
    if not serper_key:
        print("Error: SERPER_API_KEY not found in .env file")
        print("Please set SERPER_API_KEY in your .env file")
        sys.exit(1)
    
    return True


# ============================================================================
# INDIVIDUAL TOOL LOADERS
# ============================================================================

def initialize_search_tool():
    """
    Initialize the Serper Dev search tool.
    
    This tool enables web search capabilities for researching trends,
    finding hashtags, and discovering viral content patterns.
    
    Returns:
        SerperDevTool: Configured search tool instance
        
    Raises:
        SystemExit: If SERPER_API_KEY is not found
    """
    _verify_api_keys()
    
    try:
        search_tool = SerperDevTool()
        return search_tool
    except Exception as e:
        print(f"Error initializing search tool: {e}")
        sys.exit(1)


def initialize_scrape_tool():
    """
    Initialize the website scraping tool.
    
    This tool enables scraping of website content for research insights,
    trend analysis, and content pattern discovery.
    
    Returns:
        ScrapeWebsiteTool: Configured scrape tool instance
    """
    try:
        scrape_tool = ScrapeWebsiteTool()
        return scrape_tool
    except Exception as e:
        print(f"Error initializing scrape tool: {e}")
        sys.exit(1)


# ============================================================================
# COMBINED TOOL LOADERS
# ============================================================================

def load_research_tools():
    """
    Load all tools needed for research (search + scrape).
    
    These tools are used together by the Trend Researcher agent
    to gather comprehensive trend data.
    
    Returns:
        dict: Dictionary containing 'search' and 'scrape' tools
              Example: {'search': SerperDevTool, 'scrape': ScrapeWebsiteTool}
    """
    search_tool = initialize_search_tool()
    scrape_tool = initialize_scrape_tool()
    
    return {
        'search': search_tool,
        'scrape': scrape_tool,
    }


def load_tools_as_list():
    """
    Load all tools as a single list.
    
    Useful for passing directly to agent tool parameter.
    
    Returns:
        list: List of [search_tool, scrape_tool]
    """
    search_tool = initialize_search_tool()
    scrape_tool = initialize_scrape_tool()
    
    return [search_tool, scrape_tool]


def load_tools_as_tuple():
    """
    Load all tools as a tuple (legacy compatibility).
    
    Returns:
        tuple: (search_tool, scrape_tool)
    """
    search_tool = initialize_search_tool()
    scrape_tool = initialize_scrape_tool()
    
    return (search_tool, scrape_tool)


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_tool_info():
    """
    Get information about available tools.
    
    Returns:
        dict: Dictionary with tool information
    """
    return {
        'search': {
            'name': 'SerperDevTool',
            'description': 'Web search for trends, hashtags, viral content',
            'agent': 'Trend Researcher',
            'requires': 'SERPER_API_KEY',
        },
        'scrape': {
            'name': 'ScrapeWebsiteTool',
            'description': 'Scrape website content for research insights',
            'agent': 'Trend Researcher',
            'requires': 'Internet connectivity',
        },
    }


def display_tool_info():
    """
    Display tool information to console.
    
    Useful for debugging and understanding tool configuration.
    """
    info = get_tool_info()
    
    print("\n" + "="*70)
    print("AVAILABLE TOOLS FOR LINKEDIN CONTENT MANAGER")
    print("="*70)
    
    for tool_key, tool_data in info.items():
        print(f"\n📦 {tool_data['name']}")
        print(f"   Description: {tool_data['description']}")
        print(f"   Used by: {tool_data['agent']} Agent")
        print(f"   Requires: {tool_data['requires']}")
    
    print("\n" + "="*70 + "\n")


# ============================================================================
# LAZY LOADING (Optional)
# ============================================================================

# Cache for lazy loading
_tools_cache = {}


def get_search_tool_lazy():
    """
    Get search tool with lazy loading (caches after first load).
    
    Returns:
        SerperDevTool: Cached or newly initialized search tool
    """
    if 'search' not in _tools_cache:
        _tools_cache['search'] = initialize_search_tool()
    return _tools_cache['search']


def get_scrape_tool_lazy():
    """
    Get scrape tool with lazy loading (caches after first load).
    
    Returns:
        ScrapeWebsiteTool: Cached or newly initialized scrape tool
    """
    if 'scrape' not in _tools_cache:
        _tools_cache['scrape'] = initialize_scrape_tool()
    return _tools_cache['scrape']


def clear_tool_cache():
    """
    Clear the tool cache.
    
    Useful for testing or resetting tool state.
    """
    global _tools_cache
    _tools_cache = {}
