import os
from dotenv import load_dotenv

# .env load karo (same folder me .env hona chahiye)
load_dotenv("hel.env")

# ❌ GALAT: os.getenv("agent_9801....")
# ✅ Sahi: env variable ka NAAM pass karo
AGENT_ID = os.getenv("agent_9801kae42540fybr0kxyxbbwggdz")
API_KEY = os.getenv("Ask_06658ff9ee6309af11ad288f05f845a8c06dbc488d7d154fY")

# Basic check – agar env se kuch nahi aaya to clearly error de
if not AGENT_ID or not API_KEY:
    missing = []
    if not AGENT_ID:
        missing.append("AGENT_ID")
    if not API_KEY:
        missing.append("API_KEY")
    raise RuntimeError(
        "Missing environment variables: "
        + ", ".join(missing)
        + ".\nMake sure your .env file has AGENT_ID and API_KEY."
    )

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

user_name = "Kshitij"
schedule = "Sales Meeting with Taipy at 10:00; Gym with Sophie at 17:00"
prompt = f"You are a helpful assistant. Your interlocutor has the following schedule: {schedule}."
first_message = f"Hye {user_name}, how can I help you today?"

conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

config = ConversationConfig(
    conversation_config_override=conversation_override,
    extra_body={},
    dynamic_variables={},
)

# Client ab env se API_KEY use karega (hardcode nahi)
client = ElevenLabs(api_key=API_KEY)

# Callbacks
def print_agent_response(response):
    print(f"Agent: {response}")

def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")

def print_user_transcript(transcript):
    print(f"User: {transcript}")

# ❌ Duplicate Conversation banane ki zarurat nahi
# 🔴 IMPORTANT: abhi ke liye requires_auth=False rakho
conversation = Conversation(
    client,
    AGENT_ID,
    config=config,
    requires_auth=False,  # pehle True tha, fir convai_write error aa raha tha
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

# Start session
conversation.start_session()
