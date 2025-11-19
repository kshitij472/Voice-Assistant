import os
from dotenv import load_dotenv

load_dotenv()

AGENT_ID = os.getenv("agent_9801kae42540fybr0kxyxbbwggdz")
API_KEY = os.getenv("sk_06658ff9ee6309af11ad288f05f845a8c06dbc488d7d154f")

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig