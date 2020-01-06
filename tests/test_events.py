import sys
import pytest
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock
from discord import Message, MessageType


base_directory = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(base_directory / "Rekt"))

from Rekt.Events import (
    checks,
    hasAttachments,
    hasImages,
    hasDocuments,
    CheckedMessage,
)

#: Fixtures


@pytest.fixture()
def discord_message():
    attachment_data = {
        "id": 1,
        "size": 123,
        "height": 69,
        "width": 69,
        "filename": "test.jpg",
        "url": "https://test.com",
    }
    message_data = {
        "id": 1,
        "attachments": [attachment_data],
        "embeds": [],
        "edited_timestamp": datetime.now().isoformat(),
        "type": MessageType.premium_guild_tier_1,
        "pinned": False,
        "mention_everyone": False,
        "tts": False,
        "content": "discordpy is hard to mock",
    }
    state = MagicMock()
    channel = MagicMock()
    message: Message = Message(channel=channel, data=message_data, state=state)
    yield message


#: Tests


def test_hasAttachments(discord_message):
    assert hasAttachments(discord_message) == True


def test_hasImages(discord_message):
    assert hasImages(discord_message) == True


def test_hasDocuments(discord_message):
    assert hasDocuments(discord_message) == False


def test_CheckedMessage(discord_message):
    message = CheckedMessage(discord_message, checks=checks)
    assert message() == {
        "hasAttachments": True,
        "hasImages": True,
        "hasDocuments": False,
    }
