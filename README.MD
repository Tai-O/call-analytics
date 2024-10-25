# Customer Call Analytics

This project provides tools for analyzing customer service call transcripts using various NLP techniques including sentiment analysis, topic modeling, and LLM-based analysis.

## Features

- Sentiment analysis of customer conversations
- Topic modeling to identify key themes
- Word frequency analysis
- Custom LLM analysis using Azure OpenAI
- Vector database integration for efficient transcript retrieval

## Project Structure

```
call_analytics/
├── src/                    # Source code
│   ├── data_loader.py     # Transcript loading and processing
│   ├── sentiment_analyzer.py # Sentiment analysis
│   ├── topic_modeling.py  # Topic modeling
│   ├── word_analysis.py   # Word frequency analysis
│   └── llm_analyzer.py    # LLM integration
├── config/                 # Configuration files
│   └── config.py          # Project configuration
└── utils/                  # Utility functions
    └── text_processing.py  # Text preprocessing utilities
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Tai-O/call-analytics.git
cd call-analytics
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download required NLTK data:
```python
import nltk
nltk.download('all')
```

## Configuration

Get Open AI API KEY
- Create an account on https://platform.openai.com/api-keys and get an API KEY (Needed to access GPT 3.5 turbo model)
- Open command prompt (Windows)
- ```bash
    setx OPENAI_API_KEY "your-api-key-here"
    ```
- Permanent setup: To make the setup permanent, add the variable through the system properties as follows:

Right-click on 'This PC' or 'My Computer' and select 'Properties'.
- Click on 'Advanced system settings'.
- Click the 'Environment Variables' button.
- In the 'System variables' section, click 'New...' and enter OPENAI_API_KEY as the variable name and your API key as the variable value.
- Verification: To verify the setup, reopen the command prompt and type the command below. It should display your API key: echo %OPENAI_API_KEY%


Update the Azure OpenAI credentials in `config/config.py`:

```python
AZURE_CONFIG = {
    "endpoint": "your-endpoint",
    "deployment": "your-deployment",
    "api_key": "your-api-key"
}
```

## Usage

### Basic Analysis

```python
from src.data_loader import read_transcripts, extract_member_lines
from src.sentiment_analyzer import analyze_sentiment, plot_sentiment_distribution

# Load transcripts
transcripts = read_transcripts('path/to/transcripts')
member_lines = extract_member_lines(transcripts)

# Analyze sentiment
sentiment_scores = [(line, analyze_sentiment(line)) for line in member_lines]
plot_sentiment_distribution(sentiment_scores)
```

### LLM Analysis

```python
from src.llm_analyzer import LLMAnalyzer
from config.config import AZURE_CONFIG, LLM_PROMPT_TEMPLATE

# Initialize LLM analyzer
analyzer = LLMAnalyzer(
    azure_endpoint=AZURE_CONFIG["endpoint"],
    api_key=AZURE_CONFIG["api_key"]
)

# Create vector database
collection = analyzer.create_vector_db("transcripts", member_lines)

# Generate insights
query = "Identify the sentiment of the call"
context = analyzer.query_vector_db(collection, query)
response = analyzer.generate_response(
    LLM_PROMPT_TEMPLATE.format(query, context)
)
```
