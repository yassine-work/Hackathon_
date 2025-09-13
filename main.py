import requests
import json



def start():
    welcome="Welcome, ladies and gentlemen, to the ultimate battleground, where legends are made and history is written! I’m your host, bringing you the fastest plays, sharpest calls, and spectacular highlights from today’s high-stakes tournament. Get ready for insane strategies, jaw-dropping moves, and edge-of-your-seat action as our top contenders prove why they deserve to be called the best in the game. Strap in—because the only thing faster than the gameplay tonight is the excitement in the arena!"
    #add text to speech 
    #-------------------------

    
def get_commentary_from_lcu_llm(event_data, llm_model=GEMINI_LLM_MODEL, api_key=GEMINI_API_KEY):
    """
    Sends LCU event JSON to an LLM to generate professional esports commentary.

    Args:
        event_data (dict): JSON object from LCU API for a single event or current game state.
        llm_model (str): The LLM model to use.
        api_key (str): API key for OpenAI or similar provider.

    Returns:
        str: Generated commentary.
    """

    # Build the system prompt
    system_prompt = """
    You are a professional League of Legends esports commentator. 
    Provide live, energetic, and accurate commentary based on structured game events.
    Rules:
    1. Only comment on actual events; do not invent anything.
    2. Prioritize kills, first blood, dragons, baron, towers, ultimates, and major fights.
    3. Provide context, e.g., gold lead, team rotations, map control.
    4. During downtime, comment on lane status, farming, vision, or upcoming fights.
    5. Keep commentary human-like, concise, and engaging.
    """

    # Format the message to send to the LLM
    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": f"Generate commentary for this event:\n{json.dumps(event_data)}"
        }
    ]

    # API call
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_LLM_MODEL}:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": llm_model,
        "messages": messages,
        "temperature": 0.8,  # Slight randomness for variety
        "max_tokens": 100
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        commentary = result['choices'][0]['message']['content'].strip()
        return commentary
    except requests.exceptions.RequestException as e:
        return f"Error generating commentary: {e}"







while(True):
    start()
    #add -----