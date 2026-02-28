"""
Agents Package

This package contains all agent definitions and tool configuration for the
LinkedIn Content Manager system.

Modules:
- agents.py: All 5 agent definitions
- tools_loader.py: Tool initialization and management
"""

from .agents import (
    create_trend_researcher_agent,
    create_content_writer_agent,
    create_content_critic_agent,
    create_content_optimizer_agent,
    create_scheduling_agent,
    get_all_agents,
)
from .tools_loader import load_tools, get_search_tool, get_scrape_tool

__all__ = [
    "create_trend_researcher_agent",
    "create_content_writer_agent",
    "create_content_critic_agent",
    "create_content_optimizer_agent",
    "create_scheduling_agent",
    "get_all_agents",
    "load_tools",
    "get_search_tool",
    "get_scrape_tool",
]
