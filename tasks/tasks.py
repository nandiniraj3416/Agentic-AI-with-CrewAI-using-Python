"""
LinkedIn Content Manager - Task Definitions

This module contains all 5 sequential tasks for the LinkedIn content creation pipeline.
Each task is designed to work with a specific agent and builds upon the previous task's output.

Tasks:
1. Research Task - Assigned to Trend Researcher
2. Writing Task - Assigned to Content Writer
3. Critique Task - Assigned to Content Critic
4. Optimization Task - Assigned to Content Optimizer
5. Scheduling Task - Assigned to Scheduling Agent

Process: Sequential pipeline (research → write → critique → optimize → schedule)
"""

from crewai import Task


def create_research_task(agent):
    """
    Create the Research Task.
    
    Args:
        agent: Trend Researcher Agent
        
    Returns:
        Task: Configured research task
    """
    task = Task(
        description="""
        Research the latest trends, viral content patterns, and hot topics on LinkedIn for the given niche.
        
        Task Details:
        - Find 3-5 trending angles and themes currently performing well in {topic}
        - Identify relevant, high-performing hashtags (#hashtag format)
        - Discover content hooks and narrative patterns that resonate
        - Analyze recent viral posts in this niche
        - Note any industry news or emerging patterns
        
        Your research should be data-driven and provide specific, actionable insights.
        """,
        expected_output="""
        A structured research brief including:
        1. Trending Topics (3-5 angles with explanation of current momentum)
        2. Top-Performing Hashtags (#hashtag - expected reach)
        3. Content Hook Ideas (specific hook patterns that work well)
        4. Viral Content Patterns (what makes content perform well)
        5. Industry News & Context (recent developments in {topic})
        
        Format as clear sections with bullet points.
        """,
        agent=agent,
        verbose=True,
    )
    
    return task


def create_writing_task(agent):
    """
    Create the Writing Task.
    
    Args:
        agent: Content Writer Agent
        
    Returns:
        Task: Configured writing task
    """
    task = Task(
        description="""
        Using the research brief, write a compelling LinkedIn post about {topic}.
        
        Requirements:
        - Strong hook in first 2 lines (the most important part - make people want to click "see more")
        - Storytelling or value-driven body (3-5 paragraphs)
        - Clear, action-oriented CTA (Call-To-Action)
        - Length: 150-300 words
        - Use the trending angles and hooks from the research
        - Conversational yet professional tone
        - Include natural hashtag suggestions
        
        The post should feel authentic, engaging, and aligned with LinkedIn best practices.
        """,
        expected_output="""
        A complete LinkedIn post including:
        1. Hook (first 2 lines - make it compelling!)
        2. Body (main content with value or storytelling)
        3. CTA (call-to-action to drive engagement)
        4. Suggested Hashtags (5-8 relevant hashtags)
        5. Post Length (word count)
        
        Present the complete post as it would appear on LinkedIn.
        """,
        agent=agent,
        verbose=True,
    )
    
    return task


def create_critique_task(agent):
    """
    Create the Critique Task.
    
    Args:
        agent: Content Critic Agent
        
    Returns:
        Task: Configured critique task
    """
    task = Task(
        description="""
        Review the LinkedIn post draft and provide detailed, honest, constructive feedback.
        
        Evaluation Criteria:
        1. Hook Strength (0-10): Will the first 2 lines make people click "see more"?
        2. Storytelling Quality (0-10): Is the narrative compelling and relatable?
        3. Engagement Potential (0-10): How likely is this to generate comments and shares?
        4. CTA Effectiveness (0-10): Does the CTA motivate action?
        5. Tone Consistency (0-10): Is the tone appropriate for the audience?
        6. Mobile Formatting (0-10): Is it readable on mobile devices?
        7. Viral Potential (0-10): Could this post go viral?
        
        For each criterion, provide:
        - A score (0-10)
        - Specific feedback
        - Actionable improvement suggestions
        
        Be constructive but honest about what's working and what's not.
        """,
        expected_output="""
        A detailed critique report including:
        
        1. OVERALL SCORE (out of 10)
        2. DETAILED SCORES:
           - Hook Strength: X/10
           - Storytelling Quality: X/10
           - Engagement Potential: X/10
           - CTA Effectiveness: X/10
           - Tone Consistency: X/10
           - Mobile Formatting: X/10
           - Viral Potential: X/10
        
        3. STRENGTHS (what works well - be specific)
        
        4. WEAKNESSES (areas for improvement - be honest)
        
        5. SPECIFIC IMPROVEMENT SUGGESTIONS (actionable + detailed)
        
        6. REWRITE RECOMMENDATIONS (if needed)
        """,
        agent=agent,
        verbose=True,
    )
    
    return task


def create_optimization_task(agent):
    """
    Create the Optimization Task.
    
    Args:
        agent: Content Optimizer Agent
        
    Returns:
        Task: Configured optimization task
    """
    task = Task(
        description="""
        Take the original LinkedIn post and the critic's feedback, then rewrite and polish.
        
        Your Goals:
        1. Improve the hook to maximize clickability (first 2 lines are CRITICAL)
        2. Tighten the copy - remove fluff, strengthen value proposition
        3. Optimize formatting:
           - Use short lines for scannability
           - Add strategic line breaks between ideas
           - Use emojis strategically (not overdone)
           - Create visual hierarchy
        4. Strengthen the CTA to drive specific action
        5. Optimize hashtags for reach and relevance
        6. Ensure mobile-first readability
        
        Incorporate ALL feedback from the critic while maintaining authenticity.
        The final post should be publish-ready and highly optimized for LinkedIn's algorithm.
        """,
        expected_output="""
        A final, polished, publish-ready LinkedIn post including:
        
        1. OPTIMIZED POST (as formatted for LinkedIn)
        2. KEY OPTIMIZATIONS MADE (brief explanation of changes)
        3. FORMATTING NOTES (line breaks, emoji usage, etc.)
        4. HASHTAG STRATEGY (recommended hashtags with brief rationale)
        5. ENGAGEMENT HOOKS (key elements designed to drive interaction)
        
        The post should be ready to copy-paste directly into LinkedIn.
        """,
        agent=agent,
        verbose=True,
    )
    
    return task


def create_scheduling_task(agent):
    """
    Create the Scheduling Task.
    
    Args:
        agent: Scheduling Agent
        
    Returns:
        Task: Configured scheduling task
    """
    task = Task(
        description="""
        Analyze the final post content and the target audience for {topic}. 
        Recommend the best day and time to publish with timezone considerations.
        
        Analysis Includes:
        1. Determine optimal posting day and time:
           - Consider industry standards for {topic}
           - Factor in timezone considerations (recommend for major timezones)
           - Account for day-of-week patterns
           - Consider content type (thought leadership, viral story, announcement, etc.)
        
        2. Prepare final formatted post:
           - Ensure proper spacing and formatting
           - Verify hashtag placement
           - Check for mobile readability
           - Make it copy-paste ready
        
        3. Create engagement strategy:
           - Tips for the first hour after posting
           - When to respond to comments
           - Engagement techniques to boost reach
           - Hashtag strategy explained
        
        Provide actionable timing recommendations backed by LinkedIn analytics principles.
        """,
        expected_output="""
        A COMPLETE PUBLISHING BRIEF including:
        
        📅 OPTIMAL POSTING TIME:
        - Recommended Day(s)
        - Recommended Time(s)
        - Timezone(s) considered
        - Reasoning based on {topic} industry patterns
        
        📋 FINAL FORMATTED POST:
        [COMPLETE POST TEXT - READY TO COPY-PASTE]
        
        #️⃣ HASHTAG STRATEGY:
        - Hashtag List (organized by reach tier)
        - Hashtag Placement Tips
        - Hashtag Strategy Rationale
        
        🚀 FIRST-HOUR ENGAGEMENT STRATEGY:
        - Actions to take immediately after posting
        - When to engage with comments
        - Tips to boost reach in first hour
        - Monitoring recommendations
        
        📊 EXPECTED OUTCOMES:
        - Estimated reach potential
        - Engagement benchmarks for this content type
        """,
        agent=agent,
        verbose=True,
    )
    
    return task


def get_all_tasks(agents):
    """
    Create and return all 5 tasks in sequential order.
    
    Args:
        agents: Tuple of (trend_researcher, content_writer, content_critic, 
                content_optimizer, scheduling_agent)
        
    Returns:
        tuple: (research_task, writing_task, critique_task, 
                optimization_task, scheduling_task)
    """
    (
        trend_researcher,
        content_writer,
        content_critic,
        content_optimizer,
        scheduling_agent,
    ) = agents
    
    research_task = create_research_task(trend_researcher)
    writing_task = create_writing_task(content_writer)
    critique_task = create_critique_task(content_critic)
    optimization_task = create_optimization_task(content_optimizer)
    scheduling_task = create_scheduling_task(scheduling_agent)
    
    return (
        research_task,
        writing_task,
        critique_task,
        optimization_task,
        scheduling_task,
    )
