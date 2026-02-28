"""
Config Package

This package contains all configuration settings for the LinkedIn Content Manager.

Modules:
- settings.py: LLM, agent, task, and system settings

Configuration Categories:
- LLM_CONFIG: Model selection and parameters
- AGENTS_CONFIG: Agent behavior settings
- CONTENT_REQUIREMENTS: Post length and hashtag ranges
- RESEARCH_PARAMETERS: Search depth and topic numbers
- CRITIQUE_CRITERIA: Quality evaluation weights
- OPTIMIZATION_SETTINGS: Formatting preferences
- SCHEDULING_PARAMETERS: Timezone and timing options
- OUTPUT_SETTINGS: Display and verbosity options
- API_SETTINGS: Retry and timeout settings
- LOGGING_SETTINGS: Log file and level settings
"""

from .settings import (
    LLM_CONFIG,
    AGENTS_CONFIG,
    CONTENT_REQUIREMENTS,
    RESEARCH_PARAMETERS,
    CRITIQUE_CRITERIA,
    OPTIMIZATION_SETTINGS,
    SCHEDULING_PARAMETERS,
    OUTPUT_SETTINGS,
    API_SETTINGS,
    LOGGING_SETTINGS,
)

__all__ = [
    "LLM_CONFIG",
    "AGENTS_CONFIG",
    "CONTENT_REQUIREMENTS",
    "RESEARCH_PARAMETERS",
    "CRITIQUE_CRITERIA",
    "OPTIMIZATION_SETTINGS",
    "SCHEDULING_PARAMETERS",
    "OUTPUT_SETTINGS",
    "API_SETTINGS",
    "LOGGING_SETTINGS",
]
