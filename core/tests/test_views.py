from http import HTTPStatus
import json

import pytest

from core.views import get_proxies


def test_everything_is_fine(mocker, rf):
    service = mocker.patch("core.views.get_proxies_from_db", return_value=([], {}))
    request = rf.get("/")
    response = get_proxies(request)
    response_content = json.loads(response.content.decode("utf-8"))

    assert response.status_code == HTTPStatus.OK
    service.assert_called_once()
    assert len(response_content) == 2
