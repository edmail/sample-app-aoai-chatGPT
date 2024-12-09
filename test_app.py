import os
import pytest
import asyncio
from mocks import (
    MockAzureOpenAI,
    MockCosmosConversationClient,
    mock_get_authenticated_user_details,
    mock_get_msdefender_user_json,
    MockResponse
)

@pytest.fixture
def set_env_vars(monkeypatch):
    monkeypatch.setenv("USE_MOCKS", "true")

@pytest.mark.asyncio
async def test_mock_azure_openai(set_env_vars):
    client = MockAzureOpenAI()
    response = await client.completions()
    print("Azure OpenAI response:", response)
    assert response == {"choices": [{"message": {"content": "Mock response"}}]}

@pytest.mark.asyncio
async def test_mock_cosmos_conversation_client(set_env_vars):
    client = MockCosmosConversationClient()
    ensure_response = await client.ensure()
    print("Ensure response:", ensure_response)
    assert ensure_response == (True, None)

    create_response = await client.create_conversation()
    print("Create conversation response:", create_response)
    assert create_response == {"id": "mock_id"}

    get_response = await client.get_conversation()
    print("Get conversation response:", get_response)
    assert get_response == {"id": "mock_id", "messages": []}

    delete_response = await client.delete_conversation()
    print("Delete conversation response:", delete_response)
    assert delete_response == True

    get_conversations_response = await client.get_conversations()
    print("Get conversations response:", get_conversations_response)
    assert get_conversations_response == []

    delete_messages_response = await client.delete_messages()
    print("Delete messages response:", delete_messages_response)
    assert delete_messages_response == True

@pytest.mark.asyncio
async def test_mock_get_authenticated_user_details(set_env_vars):
    user_details = await mock_get_authenticated_user_details()
    print("Authenticated user details:", user_details)
    assert user_details == {"user_id": "mock_user_id", "username": "mock_user"}

@pytest.mark.asyncio
async def test_mock_get_msdefender_user_json(set_env_vars):
    user_json = await mock_get_msdefender_user_json()
    print("MS Defender user JSON:", user_json)
    assert user_json == {"user": "mock_user", "status": "safe"}
    assert ensure_response == (True, None)

    create_response = await client.create_conversation()
    print("Create conversation response:", create_response)
    assert create_response == {"id": "mock_id"}

    get_response = await client.get_conversation()
    print("Get conversation response:", get_response)
    assert get_response == {"id": "mock_id", "messages": []}

    delete_response = await client.delete_conversation()
    print("Delete conversation response:", delete_response)
    assert delete_response == True

    get_conversations_response = await client.get_conversations()
    print("Get conversations response:", get_conversations_response)
    assert get_conversations_response == []

    delete_messages_response = await client.delete_messages()
    print("Delete messages response:", delete_messages_response)
    assert delete_messages_response == True

@pytest.mark.asyncio
async def test_mock_get_authenticated_user_details(set_env_vars):
    user_details = await mock_get_authenticated_user_details()
    print("Authenticated user details:", user_details)
    assert user_details == {"user_id": "mock_user_id", "username": "mock_user"}

@pytest.mark.asyncio
async def test_mock_get_msdefender_user_json(set_env_vars):
    user_json = await mock_get_msdefender_user_json()
    print("MS Defender user JSON:", user_json)
    assert user_json == {"user": "mock_user", "status": "safe"}

@pytest.mark.asyncio
async def test_mock_response_async_iteration():
    # Test the async iteration of MockResponse
    mock_response = MockResponse()
    results = []
    async for choice in mock_response:
        results.append(choice)
    
    print("MockResponse async iteration results:", results)
    assert len(results) == len(mock_response.choices)
    for choice in results:
        assert choice.id == "mock-id"
        assert choice.message.content == "Mock response content"