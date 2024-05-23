import pytest


@pytest.fixture  # fixture - prepare data for tests
async def prepare_data():
    print("This is a fixture")
