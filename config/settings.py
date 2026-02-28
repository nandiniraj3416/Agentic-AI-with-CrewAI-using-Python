"""
Configuration file for LinkedIn Content Manager

This file contains customizable settings for the CrewAI system.
Modify these to adjust agent behavior, task parameters, and output settings.

Located in: config/settings.py
"""

# ============================================================================
# LLM CONFIGURATION
# ============================================================================

LLM_CONFIG = {
    "model": "gpt-4",  # Options: gpt-4, gpt-4o, gpt-3.5-turbo
    "temperature": 0.7,  # 0.0-1.0 (higher = more creative, lower = more focused)
    "max_tokens": 2000,  # Maximum tokens per response
}

# ============================================================================
# AGENT CONFIGURATION
# ============================================================================

AGENTS_CONFIG = {
    "trend_researcher": {
        "role": "LinkedIn Trend Researcher",
        "verbose": True,
        "allow_delegation": False,
        "memory": True,
    },
    "content_writer": {
        "role": "LinkedIn Content Writer",
        "verbose": True,
        "allow_delegation": False,
        "memory": True,
    },
    "content_critic": {
        "role": "Content Quality Critic",
        "verbose": True,
        "allow_delegation": False,
        "memory": True,
    },
    "content_optimizer": {
        "role": "LinkedIn Post Optimizer",
        "verbose": True,
        "allow_delegation": False,
        "memory": True,
    },
    "scheduling_agent": {
        "role": "LinkedIn Publishing Strategist",
        "verbose": True,
        "allow_delegation": False,
        "memory": True,
    },
}

# ============================================================================
# CONTENT REQUIREMENTS
# ============================================================================

CONTENT_REQUIREMENTS = {
    "post_min_length": 150,  # Minimum words
    "post_max_length": 300,  # Maximum words
    "min_hashtags": 5,
    "max_hashtags": 8,
    "required_hook_lines": 2,  # First N lines = hook
}

# ============================================================================
# RESEARCH PARAMETERS
# ============================================================================

RESEARCH_PARAMETERS = {
    "num_trending_topics": 5,  # Number of trending angles to find
    "num_hashtags": 8,  # Number of hashtags to research
    "search_depth": "detailed",  # Options: quick, standard, detailed
}

# ============================================================================
# CRITIQUE CRITERIA
# ============================================================================

CRITIQUE_CRITERIA = {
    "hook_strength": {
        "weight": 30,  # Percentage weight in overall score
        "description": "Will first 2 lines make people click 'see more'?"
    },
    "storytelling_quality": {
        "weight": 20,
        "description": "Is the narrative compelling and relatable?"
    },
    "engagement_potential": {
        "weight": 20,
        "description": "How likely is this to generate comments and shares?"
    },
    "cta_effectiveness": {
        "weight": 15,
        "description": "Does the CTA motivate action?"
    },
    "tone_consistency": {
        "weight": 10,
        "description": "Is the tone appropriate and consistent?"
    },
    "mobile_formatting": {
        "weight": 5,
        "description": "Is it readable on mobile devices?"
    },
}

# ============================================================================
# OPTIMIZATION SETTINGS
# ============================================================================

OPTIMIZATION_SETTINGS = {
    "emoji_usage": "strategic",  # Options: none, minimal, strategic, moderate
    "line_break_strategy": "optimal",  # Options: minimal, standard, optimal
    "hashtag_placement": "end",  # Options: end, mixed, smart
    "focus_on_engagement": True,
    "mobile_first": True,
}

# ============================================================================
# SCHEDULING PARAMETERS
# ============================================================================

SCHEDULING_PARAMETERS = {
    "post_timezones": ["EST", "CST", "PST", "UTC"],  # Timezones to consider
    "preferred_day": "weekday",  # Options: weekday, weekend, any
    "optimal_hours": {
        "early_morning": (6, 8),  # 6 AM - 8 AM
        "morning": (8, 10),       # 8 AM - 10 AM
        "lunch": (12, 1),         # 12 PM - 1 PM
        "afternoon": (3, 5),      # 3 PM - 5 PM
        "evening": (7, 9),        # 7 PM - 9 PM
    },
    "engagement_monitoring_hours": 1,  # Hours to actively monitor after posting
}

# ============================================================================
# OUTPUT FORMATTING
# ============================================================================

OUTPUT_SETTINGS = {
    "show_research_details": True,
    "show_critique_details": True,
    "show_optimization_steps": True,
    "include_section_separators": True,
    "verbosity_level": "detailed",  # Options: minimal, standard, detailed
}

# ============================================================================
# API SETTINGS
# ============================================================================

API_SETTINGS = {
    "retry_attempts": 3,  # Number of retries on API failure
    "retry_delay": 2,  # Seconds to wait between retries
    "timeout": 60,  # Request timeout in seconds
}

# ============================================================================
# LOGGING SETTINGS
# ============================================================================

LOGGING_SETTINGS = {
    "log_to_file": True,
    "log_file": "linkedin_content_manager.log",
    "log_level": "INFO",  # Options: DEBUG, INFO, WARNING, ERROR
    "include_timestamps": True,
}
