from asyncio import AbstractEventLoop
from typing import Generator
from unittest import mock

import pytest
from httpx import AsyncClient

from worker.application import app, container
from worker.services import Service


@pytest.fixture
def client(event_loop: AbstractEventLoop) -> Generator[AsyncClient, None, None]:
    client = AsyncClient(app=app, base_url="http://test")
    yield client
    event_loop.run_until_complete(client.aclose())


@pytest.mark.asyncio
async def test_index(client: AsyncClient) -> None:
    service_mock = mock.AsyncMock(spec=Service)
    service_mock.process.return_value = "Foo"

    with container.service.override(service_mock):
        response = await client.get("/")

    assert response.status_code == 200
    assert response.json() == {"result": "Foo"}
