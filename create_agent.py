import json
import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

MILLIS_API_KEY: str = os.getenv("MILLIS_API_KEY")
AGENT_ID: str = os.getenv("AGENT_ID")  # paste agent_id to update existing, leave "" to create new

# Read prompt from markdown file
with open("system_prompt.md", "r", encoding="utf-8") as f:
    prompt = f.read().strip()
 
# Read agent config and inject prompt
with open("millis_create_agent.json", "r", encoding="utf-8") as f:
    payload = json.load(f)
 
payload["config"]["prompt"] = prompt
 
headers = {
    "authorization": MILLIS_API_KEY,
    "Content-Type": "application/json"
}
 
if AGENT_ID:
    response = requests.put(
        f"https://api-west.millis.ai/agents/{AGENT_ID}",
        headers=headers,
        json=payload
    )
    print(f"Updated agent: {AGENT_ID}")
else:
    response = requests.post(
        "https://api-west.millis.ai/agents",
        headers=headers,
        json=payload
    )
    print("Created new agent")
 
print(response.status_code)
print(response.text)