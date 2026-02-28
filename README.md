# Autonomous LinkedIn Content Manager - CrewAI

A production-ready AI-powered system that orchestrates a team of 5 specialized agents to research, write, critique, optimize, and prepare LinkedIn posts for publishing.

## 🎯 System Overview

This system automates the entire LinkedIn content creation pipeline:

1. **Trend Researcher** 📊 - Researches trending topics and content patterns
2. **Content Writer** ✍️ - Writes engaging LinkedIn posts
3. **Content Critic** 📝 - Reviews and provides detailed feedback
4. **Content Optimizer** 🚀 - Polishes and optimizes for maximum engagement
5. **Scheduling Agent** 🗓️ - Determines best posting time and prepares publishing brief

### Sequential Pipeline

The agents work in a sequential pipeline where the output of each agent feeds into the next:

```
Trend Research → Content Writing → Critique Review → Content Optimization → Publishing Strategy
```

---

## 📋 Prerequisites

- Python 3.9+
- OpenAI API key (GPT-4 or GPT-4o recommended)
- Serper Dev API key (for web search)

### Get Your API Keys

1. **OpenAI API Key**
   - Visit: https://platform.openai.com/api-keys
   - Create a new API key
   - Copy it securely

2. **Serper Dev API Key**
   - Visit: https://serper.dev/
   - Sign up for free
   - Get your API key from the dashboard

---

## 🚀 Installation & Setup

### Step 1: Clone or Download

Navigate to the project directory.

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   # Windows
   copy .env.example .env
   
   # Mac/Linux
   cp .env.example .env
   ```

2. Edit `.env` and add your API keys:
   ```
   OPENAI_API_KEY=your_actual_openai_key_here
   SERPER_API_KEY=your_actual_serper_key_here
   ```

---

## 💻 Usage

You have two ways to run the LinkedIn Content Manager:

### Option 1: Web Dashboard (Recommended)

Run the interactive Streamlit web interface:

```bash
streamlit run streamlit_app.py
```

**Features:**
- Modern web interface
- Real-time pipeline status
- Download results as text or JSON
- Easy topic selection with quick buttons
- Sidebar configuration options

The dashboard opens at: `http://localhost:8501`

### Option 2: Command-Line Interface

Run the CLI version for terminal-based usage:

```bash
python linkedin_content_manager_advanced.py
```

**Features:**
- Simple prompt-based input
- Detailed console output
- Good for automation/scripting
- Minimal UI overhead

---

## 📝 Usage Examples

- "AI in Healthcare"
- "Future of Remote Work"
- "Python for Data Science"
- "Cybersecurity Best Practices"
- "Climate Tech Innovation"
- "Quantum Computing"
- "Sustainable Business Practices"

---

## 🤖 Agents Explained

### 1. Trend Researcher Agent

**Role**: LinkedIn Trend Researcher

- Monitors LinkedIn trends and viral content
- Identifies industries news and emerging patterns
- Finds high-performing hashtags
- Discovers content hooks that resonate

**Output**: Research brief with trending topics, hashtags, hook ideas, and viral patterns

### 2. Content Writer Agent

**Role**: LinkedIn Content Writer

- Writes engaging, professional LinkedIn posts
- Creates compelling hooks (first 2 lines)
- Develops storytelling or value-driven body
- Includes clear call-to-action (CTA)
- Length: 150-300 words

**Output**: Complete LinkedIn post with hook, body, CTA, and hashtags

### 3. Content Critic Agent

**Role**: Content Quality Critic

Evaluates the post on 7 dimensions:
- Hook Strength (0-10)
- Storytelling Quality (0-10)
- Engagement Potential (0-10)
- CTA Effectiveness (0-10)
- Tone Consistency (0-10)
- Mobile Formatting (0-10)
- Viral Potential (0-10)

**Output**: Detailed critique with specific improvement suggestions

### 4. Content Optimizer Agent

**Role**: LinkedIn Post Optimizer

- Rewrites incorporating all feedback
- Optimizes formatting for mobile readability
- Adds strategic emoji usage
- Strengthens hook and CTA
- Optimizes hashtag placement

**Output**: Final, publish-ready post

### 5. Scheduling Agent

**Role**: LinkedIn Publishing Strategist

- Recommends optimal posting day and time
- Considers industry patterns and timezones
- Prepares final formatted post
- Provides first-hour engagement strategy
- Includes hashtag strategy

**Output**: Complete publishing brief with timing, formatted post, and engagement tips

---

## 📊 Output Structure

The final output includes:

```
✅ TREND RESEARCH
- Trending topics and angles
- Top-performing hashtags
- Content hooks and patterns
- Viral patterns analysis

✅ CONTENT DRAFT
- Initial LinkedIn post
- Hook, body, CTA structure
- Suggested hashtags

✅ CRITIQUE FEEDBACK
- Overall score (0-10)
- Detailed scores across 7 dimensions
- Strengths and weaknesses
- Specific improvement suggestions

✅ OPTIMIZED POST
- Final, polished post
- Key optimizations made
- Engagement hooks
- Hashtag strategy

✅ PUBLISHING BRIEF
- Optimal posting time(s)
- Final formatted post (copy-paste ready)
- Hashtag list and strategy
- First-hour engagement strategy
- Expected outcomes
```

---

## 🔧 Configuration

### Model Selection

You can modify the LLM model in the code (default: gpt-4):

```python
# In the agent initialization
llm=ChatOpenAI(
    model_name="gpt-4",  # or "gpt-4o" or "gpt-3.5-turbo"
    temperature=0.7
)
```

### Process Control

The crew uses a sequential process:

```python
crew = Crew(
    agents=[...],
    tasks=[...],
    verbose=True,      # Show detailed output
    memory=True,       # Maintain context between agents
    process="sequential"  # Sequential pipeline
)
```

- **verbose=True**: Shows detailed agent thinking and output
- **memory=True**: Agents have context from previous steps
- **process="sequential"**: Tasks run one after another

---

## 💡 Best Practices

### Input Topics

Choose topics that:
- Are current and relevant
- Have recent trending content
- Are specific enough for focused research
- Are industry-related for B2B LinkedIn audience

### Expected Results

- Research phase: 2-3 minutes
- Full pipeline: 5-10 minutes (depending on API response times)
- Quality: Professional, LinkedIn-optimized content

### Tips for Maximum Engagement

1. **Post Timing**: Follow the agent's recommendation for your timezone
2. **Early Engagement**: Respond to first 5-10 comments immediately
3. **Hashtags**: Use all recommended hashtags
4. **First Hour**: Critical for algorithm boost - be active in first 60 minutes
5. **Authenticity**: The content maintains your voice while being optimized

---

## 🐛 Troubleshooting

### "Error: OPENAI_API_KEY not found"

- Make sure you created `.env` file (from `.env.example`)
- Verify the key is correctly pasted
- Restart your terminal after creating `.env`

### "Error: SERPER_API_KEY not found"

- Make sure Serper API key is in `.env`
- Verify the key is valid at serper.dev

### "API Rate Limit Exceeded"

- Wait a few minutes and try again
- Consider upgrading your API plan
- Use GPT-3.5-turbo for more cost-effective testing

### "No module named 'crewai'"

```bash
pip install -r requirements.txt --upgrade
```

### Response Too Long

If the post exceeds 300 words, the optimizer will trim it in the next run. You can also manually edit the post.

---

## 📈 Optimization Tips

### For Better Engagement:

1. **Hook**: Make first 2 lines irresistible
2. **Value**: Provide clear takeaway
3. **Story**: Use narrative when possible
4. **CTA**: Be specific about desired action
5. **Hashtags**: Mix broad and niche tags

### For LinkedIn Algorithm:

- Post when audience is most active
- Encourage comments (questions in CTA)
- Short lines and line breaks
- Strategic emoji usage
- Mobile-first formatting

---

## 🔒 API Cost Considerations

### Estimated Costs Per Post

- OpenAI (GPT-4): ~$0.10-0.30 per post
- Serper Search: ~$0.01-0.05 per search
- **Total**: ~$0.15-0.35 per complete pipeline

### Cost Optimization

- Use GPT-3.5-turbo for faster, cheaper results
- Limit Serper searches in research phase
- Batch multiple posts in one session

---

## 📝 Example Output

### Research Phase Output:
```
TRENDING TOPICS:
1. AI Ethics in Enterprise (High momentum - 450 posts/week)
2. Responsible AI Development
3. AI Governance Frameworks

TOP HASHTAGS:
#AI #MachineeLearning #Ethics #Enterprise #Innovation

CONTENT HOOKS:
"Everyone's talking about AI, but nobody's talking about..."
"Here's what companies are getting wrong about AI safety..."
```

### Final Post (Ready to Publish):
```
Here's what companies are getting wrong about AI safety 🔒

Everyone's talking about AI implementation.
But nobody's talking about the ethical framework.

I've worked with 50+ companies building AI systems.
Here's what I've learned...

[Body content with value]

Drop a comment: What's YOUR biggest AI ethics concern?

#AI #Ethics #MachineeLearning #Enterprise #Innovation
```

---

## 📚 Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [OpenAI API Docs](https://platform.openai.com/docs/)
- [Serper API Docs](https://serper.dev/docs/)
- [LinkedIn Content Strategy](https://business.linkedin.com/marketing-solutions/marketing-strategy)

---

## 📄 License

This project is provided as-is for educational and professional use.

---

## 🤝 Contributing

To improve this system:
1. Test with various topics
2. Refine agent backstories for your use case
3. Adjust task descriptions based on your style
4. Share feedback and improvements

---

## ⚙️ Advanced Configuration

### Custom LLM Parameters

Edit agent initialization to customize:

```python
trend_researcher = Agent(
    role="LinkedIn Trend Researcher",
    goal="...",
    backstory="...",
    tools=[search_tool, scrape_tool],
    verbose=True,
    allow_delegation=False,  # Set to True to allow task delegation
    memory=True,
    max_iterations=5,  # Maximum iterations per task
    # llm=custom_llm_instance  # Custom LLM if needed
)
```

### Custom Tools

Add additional tools to Trend Researcher:

```python
from crewai_tools import BrowserTools, FileTools

trend_researcher = Agent(
    tools=[search_tool, scrape_tool, BrowserTools.browse_website],
    ...
)
```

---

## ✅ Success Checklist

Before running:

- [ ] Python 3.9+ installed
- [ ] Virtual environment activated
- [ ] requirements.txt installed
- [ ] .env file created with API keys
- [ ] API keys are valid and have sufficient balance
- [ ] Topic is specific and trend-worthy

After running:

- [ ] Research brief is comprehensive
- [ ] Post is 150-300 words
- [ ] Critique provides actionable feedback
- [ ] Final post is optimized and formatted
- [ ] Publishing brief includes timing recommendation

---

## 🎓 Learning & Customization

### Customize for Your Brand

Edit agent backstories to reflect:
- Your writing style
- Your industry expertise
- Your target audience
- Your unique voice

### Modify Task Requirements

Adjust task descriptions to:
- Change post length (e.g., 200-400 words)
- Add specific requirements (tone, style, topics to avoid)
- Include company/personal branding guidelines
- Specify hashtag preferences

---

## 📞 Support

For issues or questions:

1. Check the Troubleshooting section above
2. Review API key configuration
3. Check your API usage/balance
4. Review CrewAI and OpenAI documentation

---

## 🚀 Version History

- **v1.0** (Current): Initial release with 5 agents and sequential pipeline

---

**Happy content creating! 🎉**
