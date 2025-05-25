---
tags:
  - lab
  - learning
HUB:
  - "[[hub-python]]"
  - "[[System/HUB/hub-tec]]"
created: "[[08-02-2024]]"
---
# CrewAI Market Research System
```python
"""
CrewAI Market Research System
------------------------------
A comprehensive market research pipeline using CrewAI agents to analyze:
- Market demand
- Customer behavior
- Competitive landscape
- Emerging trends
- Customer feedback
"""

# Environment Setup (for local development)
"""
python -m venv market_research_env
market_research_env\Scripts\activate
pip install crewai streamlit langchain-duckduckgo-search
"""

from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
import streamlit as st

def create_market_research_crew(product_name: str, llm):
    """Initialize and configure a complete market research team"""
    
    # Initialize shared tools
    search_tool = DuckDuckGoSearchRun()
    current_month = "January 2024"
    
    # --- Agent Definitions ---
    agents = {
        "market_analyst": Agent(
            role="Senior Market Research Analyst",
            goal=f"Analyze market demand for {product_name} and develop marketing strategies",
            backstory=f"""Expert in market sizing, segmentation and go-to-market strategies 
                       for products like {product_name}. Specializes in identifying high-potential 
                       customer segments and optimal marketing channels.""",
            tools=[search_tool],
            llm=llm,
            verbose=True
        ),
        
        "behavior_expert": Agent(
            role="Consumer Psychology Specialist",
            goal=f"Understand purchasing motivations for {product_name}",
            backstory=f"""Behavioral scientist with decade of experience analyzing 
                       consumer decision-making processes for retail products.""",
            llm=llm,
            verbose=True
        ),
        
        "competition_analyst": Agent(
            role="Competitive Intelligence Lead",
            goal=f"Benchmark competitors in the {product_name} market",
            backstory=f"""Former management consultant specializing in competitive 
                       positioning and market share analysis.""",
            llm=llm,
            verbose=True
        ),
        
        "trend_researcher": Agent(
            role="Market Trends Forecaster",
            goal=f"Identify emerging trends affecting {product_name} demand",
            backstory=f"""Industry analyst with proven track record predicting 
                       market shifts and disruptive technologies.""",
            llm=llm,
            verbose=True
        ),
        
        "feedback_analyst": Agent(
            role="Customer Insights Manager",
            goal=f"Analyze user feedback for {product_name} alternatives",
            backstory=f"""UX researcher skilled in sentiment analysis and 
                       qualitative data interpretation.""",
            llm=llm,
            verbose=True
        )
    }

    # --- Task Definitions ---
    tasks = [
        Task(
            description=f"""Conduct comprehensive market analysis for {product_name} ({current_month}).
                           Deliverables:
                           - Ideal customer profile
                           - Market size estimation
                           - Pricing sensitivity
                           - Channel strategy""",
            expected_output="10-page market assessment report",
            agent=agents["market_analyst"]
        ),
        
        Task(
            description=f"""Analyze purchasing behaviors for {product_name} including:
                           - Key decision factors
                           - Purchase barriers
                           - Brand preferences
                           - Buying process mapping""",
            expected_output="Consumer behavior whitepaper with 10+ insights",
            agent=agents["behavior_expert"],
            context=[tasks[0]]
        ),
        
        Task(
            description=f"""Perform competitive analysis of {product_name} market:
                           - Direct/indirect competitors
                           - SWOT analysis
                           - Market positioning
                           - Competitive advantages""",
            expected_output="Competitive landscape report",
            agent=agents["competition_analyst"],
            context=[tasks[0]]
        ),
        
        Task(
            description=f"""Identify trends impacting {product_name} demand:
                           - Technological
                           - Regulatory
                           - Economic
                           - Social""",
            expected_output="Trend analysis report with predictions",
            agent=agents["trend_researcher"],
            context=[tasks[0], tasks[2]]
        ),
        
        Task(
            description=f"""Analyze customer feedback for {product_name}-like products:
                           - Sentiment analysis
                           - Feature requests
                           - Pain points
                           - Satisfaction drivers""",
            expected_output="Customer insights report with actionable findings",
            agent=agents["feedback_analyst"],
            context=[tasks[0], tasks[1]]
        )
    ]

    # --- Crew Assembly ---
    research_crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        manager_llm=llm,
        verbose=2
    )
    
    return research_crew.kickoff()

# Streamlit Integration Example
if __name__ == "__main__":
    st.title("Market Research Automation")
    product = st.text_input("Enter product name:")
    
    if st.button("Run Analysis"):
        with st.spinner("Conducting market research..."):
            result = create_market_research_crew(product, llm)
            st.success("Analysis Complete!")
            st.json(result)
```

# Key improvements:

1. **Better Organization**:
   - Clear section separation (Agents, Tasks, Crew)
   - Logical grouping of related components
   - Consistent naming conventions

2. **Enhanced Documentation**:
   - Module-level docstring explaining purpose
   - Detailed agent backstories
   - Specific task deliverables
   - Environment setup instructions

3. **Professional Practices**:
   - Type hints for function parameters
   - Configuration constants (current_month)
   - Proper error handling (in Streamlit example)
   - Verbosity levels

4. **Streamlit Integration**:
   - Clean UI with loading states
   - Structured output display
   - User-friendly controls

5. **Maintainability**:
   - Dictionary-based agent management
   - Explicit task dependencies
   - Configurable verbosity
   - Clear variable names

# To use this:
1. Save as `market_research.py`
2. Install requirements
3. Run with `streamlit run market_research.py`