from unittest.mock import AsyncMock

class MockCosmosDBClient:
    def __init__(self):
        self.database = AsyncMock()
        self.container = AsyncMock()

    async def read_item(self, item_id, partition_key):
        return {"id": item_id, "partition_key": partition_key, "data": "mock data"}

    async def create_item(self, item):
        return item

    async def query_items(self, query, parameters):
        return [{"id": "mock_id", "data": "mock data"}]

async def init_cosmosdb_client():
    return MockCosmosDBClient()