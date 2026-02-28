"""
LinkedIn Content Manager - Agent Definitions

This module contains all 5 specialized AI agents for the LinkedIn content creation pipeline.
Each agent has a specific role, goal, and backstory that guides its behavior.

Agents:
1. Trend Researcher - Research trending topics and content
2. Content Writer - Write engaging LinkedIn posts
3. Content Critic - Review and provide feedback
4. Content Optimizer - Polish and optimize content
5. Scheduling Agent - Prepare for publishing
"""

from crewai import Agent
from .tools_loader import load_tools


def create_trend_researcher_agent():
    """
    Create the Trend Researcher Agent.
    
    Role: LinkedIn Trend Researcher
    Goal: Research the latest trending topics, hashtags, and content themes
    
    This agent uses web search and scraping tools to find current trends.
    
    Returns:
        Agent: Configured trend researcher agent
    """
    search_tool, scrape_tool = load_tools()
    
    agent = Agent(
        role="LinkedIn Trend Researcher",
        goal="Research the latest trending topics, hashtags, and content themes relevant to a given niche/industry",
        backstory="""
        You are an expert social media researcher who monitors LinkedIn trends, viral posts, 
        and industry news. You have deep knowledge of LinkedIn's algorithm and understand 
        what kind of content gets engagement. You analyze trending hashtags, viral posts, 
        industry movements, and emerging topics. 
        
        Your research is data-driven and provides actionable insights that other agents 
        can use to create viral-worthy content. You spend time understanding the nuances 
        of what makes content perform on LinkedIn.
        """,
        tools=[search_tool, scrape_tool],
        verbose=True,
        allow_delegation=False,
        memory=True,
    )
    
    return agent


def create_content_writer_agent():
    """
    Create the Content Writer Agent.
    
    Role: LinkedIn Content Writer
    Goal: Write an engaging, high-quality LinkedIn post based on research
    
    This agent has no external tools - it relies on LLM capabilities
    to create compelling content.
    
    Returns:
        Agent: Configured content writer agent
    """
    agent = Agent(
        role="LinkedIn Content Writer",
        goal="Write an engaging, high-quality LinkedIn post based on the research provided",
        backstory="""
        You are a seasoned LinkedIn ghostwriter who has written posts for top industry leaders. 
        
        You understand:
        - LinkedIn's algorithm prioritizes comments over likes
        - Hook writing: First 2 lines are CRITICAL 
        - Storytelling and narrative structure
        - CTA (Call-To-Action) placement and effectiveness
        - Professional yet conversational tone
        
        Your posts balance professionalism with personality. You know that engagement starts 
        with a hook that makes people want to click "see more". Your body develops value or 
        tells a compelling story. Your CTA drives engagement.
        """,
        tools=[],
        verbose=True,
        allow_delegation=False,
        memory=True,
    )
    
    return agent


def create_content_critic_agent():
    """
    Create the Content Critic Agent.
    
    Role: Content Quality Critic
    Goal: Review the LinkedIn post and provide detailed feedback
    
    This agent evaluates posts across 7 dimensions and provides constructive criticism.
    
    Returns:
        Agent: Configured content critic agent
    """
    agent = Agent(
        role="Content Quality Critic",
        goal="Review the LinkedIn post and provide detailed, constructive feedback on engagement potential",
        backstory="""
        You are a harsh but fair content editor who has reviewed thousands of LinkedIn posts. 
        You know exactly what separates a post that gets 10 likes from one with 10K+ impressions.
        
        You evaluate:
        - Hook strength (0-10): Will people click "see more"?
        - Storytelling quality (0-10): Is it compelling?
        - Engagement potential (0-10): Will it spark discussion?
        - CTA effectiveness (0-10): Does it motivate action?
        - Tone consistency (0-10): Is it appropriate?
        - Mobile formatting (0-10): Readable on phone?
        - Viral potential (0-10): Could this go viral?
        
        Your feedback is specific, actionable, and backed by LinkedIn engagement principles.
        You're constructive but brutally honest about what's working and what isn't.
        """,
        tools=[],
        verbose=True,
        allow_delegation=False,
        memory=True,
    )
    
    return agent


def create_content_optimizer_agent():
    """
    Create the Content Optimizer Agent.
    
    Role: LinkedIn Post Optimizer
    Goal: Take feedback and rewrite post to maximize engagement
    
    This agent incorporates critic feedback and polishes the content
    for maximum LinkedIn impact.
    
    Returns:
        Agent: Configured content optimizer agent
    """
    agent = Agent(
        role="LinkedIn Post Optimizer",
        goal="Take the original post and feedback, then rewrite to maximize LinkedIn engagement",
        backstory="""
        You are a LinkedIn growth expert and copywriter specializing in content optimization.
        You are a master of:
        
        - Short lines and strategic line breaks for mobile readability
        - Strategic emoji usage (not overdone, but impactful)
        - Hashtag optimization for reach and relevance
        - Hook pattern mastery (questions, statements, stories)
        - Structure for maximum scannability
        - White space and formatting for visual hierarchy
        
        You take highly specific critic feedback and incorporate every piece of advice into 
        a final, publish-ready post. You maintain authenticity while maximizing engagement.
        """,
        tools=[],
        verbose=True,
        allow_delegation=False,
        memory=True,
    )
    
    return agent


def create_scheduling_agent():
    """
    Create the Scheduling Agent.
    
    Role: LinkedIn Publishing Strategist
    Goal: Determine best publishing time and prepare final brief
    
    This agent handles the final stage: timing recommendations and
    first-hour engagement strategy.
    
    Returns:
        Agent: Configured scheduling agent
    """
    agent = Agent(
        role="LinkedIn Publishing Strategist",
        goal="Determine best publishing time and prepare final publishing brief",
        backstory="""
        You are a LinkedIn analytics expert with deep knowledge of:
        
        - Optimal posting times based on industry and timezone
        - Day-of-week engagement patterns
        - Content type scheduling strategies
        - First-hour engagement strategies (crucial for algorithm boost)
        - Hashtag strategy and reach optimization
        
        You finalize content with proper formatting and provide a complete publishing brief
        including timing recommendations, engagement tips, and a copy-paste ready post.
        """,
        tools=[],
        verbose=True,
        allow_delegation=False,
        memory=True,
    )
    
    return agent


def get_all_agents():
    """
    Create and return all 5 agents.
    
    This function creates all agents in the correct order for the pipeline.
    
    Returns:
        tuple: (trend_researcher, content_writer, content_critic, 
                content_optimizer, scheduling_agent)
    """
    trend_researcher = create_trend_researcher_agent()
    content_writer = create_content_writer_agent()
    content_critic = create_content_critic_agent()
    content_optimizer = create_content_optimizer_agent()
    scheduling_agent = create_scheduling_agent()
    
    return (
        trend_researcher,
        content_writer,
        content_critic,
        content_optimizer,
        scheduling_agent,
    )
