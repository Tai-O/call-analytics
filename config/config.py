AZURE_CONFIG = {
    "endpoint": "******************************",
    "deployment": "******************************",
    "api_key": "******************************"
}

LLM_PROMPT_TEMPLATE = """
ROLE:
You are an exceptional customer service professional. 
You are very competent and able to extract meaningful insights from transcripts of customer calls that are submitted to you.
You are provided with customer side of the transcript only to analyse
INSTRUCTION: Respond to the following question: "{}"
CONTEXT: "{}"
SUMMARY: (Provide a one or two sentence summary)
"""
