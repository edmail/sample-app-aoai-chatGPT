# mocks.py

class MockAzureOpenAI:
    class Chat:
        class Completions:
            async def create(self, model, messages, temperature, max_tokens):
                # Return a mock response
                return MockResponse(model)

            class WithRawResponse:
                async def create(self, **model_args):
                    # Return a mock raw response
                    return MockRawResponse(model_args.get("model"))

            def __init__(self):
                self.with_raw_response = MockAzureOpenAI.Chat.Completions.WithRawResponse()

        def __init__(self):
            self.completions = MockAzureOpenAI.Chat.Completions()
    
    async def completions(self):
        # Simulates a direct call to `completions`
        return {"choices": [{"message": {"content": "Mock response"}}]}
    
    def __init__(self):
        self.chat = MockAzureOpenAI.Chat()

class MockResponse:
    def __init__(self, model=None):
        self.choices = [MockChoice(model)]
        self.iter_index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.iter_index < len(self.choices):
            choice = self.choices[self.iter_index]
            self.iter_index += 1
            return choice
        else:
            raise StopAsyncIteration

    def parse(self):
        # Return a parsed mock response
        return self

class MockRawResponse:
    def __init__(self, model=None):
        self.content = "Mock raw response content"
        self.headers = {"apim-request-id": "mock-request-id"}
        self.model = model

    def parse(self):
        # Return a parsed mock response
        return MockResponse(self.model)

class MockChoice:
    def __init__(self, model=None):
        self.id = "mock-id"
        self.model = model
        self.message = MockMessage()
        self.created = "mock-created-timestamp"
        self.object = "mock-object"

class MockMessage:
    def __init__(self):
        self.content = "Mock response content"

class MockCosmosConversationClient:
    async def ensure(self):
        return True, None

    async def create_conversation(self, *args, **kwargs):
        return {"id": "mock_id"}

    async def get_conversation(self, *args, **kwargs):
        return {"id": "mock_id", "messages": []}

    async def delete_conversation(self, *args, **kwargs):
        return True

    async def get_conversations(self, *args, **kwargs):
        return []
    
    async def delete_messages(self, *args, **kwargs):  # Add this method
        return True

class MmockUtilities:
    @staticmethod
    async def mock_get_authenticated_user_details(*args, **kwargs):
        return {"user_id": "mock_user_id", "username": "mock_user"}

    async def mock_get_msdefender_user_json(*args, **kwargs):
        return {"user": "mock_user", "status": "safe"}

    async def mock_format_as_ndjson(*args, **kwargs):
        return "mock_ndjson"

    async def mock_format_stream_response(*args, **kwargs):
        return "mock_stream_response"

    async def mock_format_non_streaming_response(*args, **kwargs):
        return "mock_non_streaming_response"

    async def mock_convert_to_pf_format(*args, **kwargs):
        return "mock_pf_format"

    async def mock_format_pf_non_streaming_response(*args, **kwargs):
        return "mock_pf_non_streaming_response"