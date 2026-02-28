"""
Utility helpers and functions for LinkedIn Content Manager

This module provides helper functions for logging, formatting, and output management.

Located in: utils/helpers.py
"""

import logging
import sys
from datetime import datetime
from typing import Optional, List
from config import LOGGING_SETTINGS, OUTPUT_SETTINGS

# ============================================================================
# LOGGING SETUP
# ============================================================================

def setup_logging():
    """
    Configure logging for the application.
    
    Returns:
        logger: Configured logger instance
    """
    log_level = getattr(logging, LOGGING_SETTINGS.get("log_level", "INFO"))
    
    # Create logger
    logger = logging.getLogger("LinkedInContentManager")
    logger.setLevel(log_level)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    
    # Formatter
    timestamp_format = " | %(asctime)s" if LOGGING_SETTINGS.get("include_timestamps") else ""
    formatter = logging.Formatter(
        f"%(levelname)-8s{timestamp_format} | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(formatter)
    
    # Add handler
    if not logger.handlers:
        logger.addHandler(console_handler)
    
    # File handler (if enabled)
    if LOGGING_SETTINGS.get("log_to_file"):
        file_handler = logging.FileHandler(LOGGING_SETTINGS.get("log_file", "linkedin_content_manager.log"))
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

# Initialize logger
logger = setup_logging()

# ============================================================================
# OUTPUT FORMATTING
# ============================================================================

class OutputFormatter:
    """Class for formatting and displaying output sections."""
    
    SECTION_WIDTH = 80
    
    @staticmethod
    def print_header(title: str):
        """Print a formatted header."""
        if not OUTPUT_SETTINGS.get("include_section_separators"):
            print(f"\n{title}\n")
            return
        
        separator = "=" * OutputFormatter.SECTION_WIDTH
        print(f"\n{separator}")
        print(f"{title.center(OutputFormatter.SECTION_WIDTH)}")
        print(f"{separator}\n")
    
    @staticmethod
    def print_subheader(title: str):
        """Print a formatted subheader."""
        separator = "-" * OutputFormatter.SECTION_WIDTH
        print(f"\n{title}")
        print(separator)
    
    @staticmethod
    def print_section(title: str, content: str):
        """Print a complete section with header and content."""
        OutputFormatter.print_subheader(title)
        print(content)
    
    @staticmethod
    def print_result(result: str, title: str = "FINAL RESULT"):
        """Print the final result with prominent formatting."""
        OutputFormatter.print_header(f"✅ {title} - PIPELINE COMPLETE")
        print(result)
        OutputFormatter.print_footer()
    
    @staticmethod
    def print_footer():
        """Print a footer."""
        separator = "=" * OutputFormatter.SECTION_WIDTH
        print(f"\n{separator}")
        print(f"{'🎉 Your content is ready for publishing!'.center(OutputFormatter.SECTION_WIDTH)}")
        print(f"{separator}\n")
    
    @staticmethod
    def print_bullet_list(items: List[str], title: Optional[str] = None):
        """Print a bulleted list."""
        if title:
            print(f"\n{title}:")
        for item in items:
            print(f"  • {item}")
    
    @staticmethod
    def print_numbered_list(items: List[str], title: Optional[str] = None):
        """Print a numbered list."""
        if title:
            print(f"\n{title}:")
        for idx, item in enumerate(items, 1):
            print(f"  {idx}. {item}")

# ============================================================================
# VALIDATION HELPERS
# ============================================================================

class Validators:
    """Validation utility functions."""
    
    @staticmethod
    def validate_topic(topic: str) -> bool:
        """
        Validate user input topic.
        
        Args:
            topic: User-provided topic
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not topic:
            logger.error("Topic cannot be empty")
            return False
        
        if len(topic) < 3:
            logger.error("Topic must be at least 3 characters long")
            return False
        
        if len(topic) > 200:
            logger.error("Topic must be less than 200 characters")
            return False
        
        return True
    
    @staticmethod
    def validate_api_keys(required_keys: dict) -> bool:
        """
        Validate that all required API keys are present.
        
        Args:
            required_keys: Dictionary of {key_name: key_value}
            
        Returns:
            bool: True if all keys are present, False otherwise
        """
        all_valid = True
        
        for key_name, key_value in required_keys.items():
            if not key_value:
                logger.error(f"Missing required API key: {key_name}")
                all_valid = False
        
        return all_valid

# ============================================================================
# CONTENT ANALYSIS HELPERS
# ============================================================================

class ContentAnalyzer:
    """Content analysis utilities."""
    
    @staticmethod
    def count_words(text: str) -> int:
        """Count words in text."""
        return len(text.split())
    
    @staticmethod
    def count_hashtags(text: str) -> int:
        """Count hashtags in text."""
        return text.count("#")
    
    @staticmethod
    def count_emojis(text: str) -> int:
        """Estimate emoji count (rough approximation)."""
        # Common emoji patterns - this is a naive check
        emoji_count = 0
        for char in text:
            # Check if character is in emoji ranges (simplified)
            if ord(char) > 127:
                emoji_count += 1
        return emoji_count
    
    @staticmethod
    def analyze_post(post: str) -> dict:
        """
        Comprehensive analysis of a LinkedIn post.
        
        Args:
            post: LinkedIn post content
            
        Returns:
            dict: Analysis metrics
        """
        words = ContentAnalyzer.count_words(post)
        hashtags = ContentAnalyzer.count_hashtags(post)
        emojis = ContentAnalyzer.count_emojis(post)
        lines = len(post.split("\n"))
        
        return {
            "word_count": words,
            "hashtag_count": hashtags,
            "emoji_count": emojis,
            "line_count": lines,
            "average_line_length": words // max(lines, 1),
        }
    
    @staticmethod
    def get_analysis_report(post: str) -> str:
        """Get a formatted analysis report."""
        analysis = ContentAnalyzer.analyze_post(post)
        
        report = f"""
📊 CONTENT ANALYSIS:
  • Word Count: {analysis['word_count']} words
  • Hashtags: {analysis['hashtag_count']}
  • Emojis: {analysis['emoji_count']}
  • Lines: {analysis['line_count']}
  • Avg Line Length: {analysis['average_line_length']} words
"""
        return report

# ============================================================================
# TIME & SCHEDULING HELPERS
# ============================================================================

class SchedulingHelper:
    """Helper functions for scheduling recommendations."""
    
    TIMEZONES = {
        "EST": "Eastern Standard Time",
        "CST": "Central Standard Time",
        "PST": "Pacific Standard Time",
        "UTC": "Coordinated Universal Time",
    }
    
    OPTIMAL_POSTING_TIMES = {
        "Monday": ["8:00 AM", "12:00 PM", "5:00 PM"],
        "Tuesday": ["8:00 AM", "12:00 PM", "5:00 PM"],
        "Wednesday": ["8:00 AM", "12:00 PM", "5:00 PM"],
        "Thursday": ["8:00 AM", "12:00 PM", "5:00 PM"],
        "Friday": ["8:00 AM", "10:00 AM", "4:00 PM"],
        "Saturday": ["10:00 AM", "2:00 PM"],
        "Sunday": ["5:00 PM", "7:00 PM"],
    }
    
    @staticmethod
    def get_current_day() -> str:
        """Get current day of week."""
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[datetime.now().weekday()]
    
    @staticmethod
    def get_optimal_posting_times(day: str) -> List[str]:
        """Get optimal posting times for a given day."""
        return SchedulingHelper.OPTIMAL_POSTING_TIMES.get(day, ["9:00 AM", "1:00 PM", "5:00 PM"])

# ============================================================================
# PROMPT & TEMPLATE HELPERS
# ============================================================================

class PromptTemplates:
    """Pre-defined prompt templates for agents."""
    
    @staticmethod
    def get_research_focus_prompt(topic: str) -> str:
        """Get focused research prompt for a topic."""
        return f"""
Focus your research on LinkedIn-specific insights for: {topic}

Look for:
1. Recent viral posts in this space
2. High-engagement content patterns
3. Industry-specific hashtags
4. Trending news and announcements
5. Thought leaders and conversations
"""
    
    @staticmethod
    def get_writing_brief(research_summary: str, topic: str) -> str:
        """Get writing brief based on research."""
        return f"""
Topic: {topic}

Research Insights:
{research_summary}

Write a post that:
- Captures one key insight from the research
- Uses the suggested hooks and patterns
- Speaks to LinkedIn's professional audience
- Includes a clear CTA that encourages engagement
"""

# ============================================================================
# ERROR HANDLING
# ============================================================================

class ErrorHandler:
    """Centralized error handling."""
    
    @staticmethod
    def handle_api_error(error: Exception, context: str = "") -> None:
        """
        Handle API-related errors.
        
        Args:
            error: The exception that occurred
            context: Context about what was happening
        """
        error_msg = str(error)
        
        if "OPENAI_API_KEY" in error_msg or "authentication" in error_msg.lower():
            logger.error("Authentication Error: Invalid OpenAI API key")
            logger.error("Please check your .env file and API key validity")
        elif "rate" in error_msg.lower():
            logger.error("Rate Limit Error: API rate limit exceeded")
            logger.error("Please wait a moment and try again")
        elif "timeout" in error_msg.lower():
            logger.error("Timeout Error: Request took too long")
            logger.error("Check your internet connection and try again")
        else:
            logger.error(f"API Error: {error_msg}")
        
        if context:
            logger.error(f"Context: {context}")
    
    @staticmethod
    def handle_user_input_error(field: str) -> None:
        """Handle user input validation errors."""
        logger.error(f"Invalid input for {field}")
        logger.info(f"Please provide a valid {field} and try again")

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_timestamp() -> str:
    """Get current timestamp as string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

