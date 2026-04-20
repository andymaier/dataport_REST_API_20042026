# coding: utf-8

from fastapi.testclient import TestClient


from typing import List, Optional  # noqa: F401
from openapi_server.models.artikel import Artikel  # noqa: F401


def test_artikel_get(client: TestClient):
    """Test case for artikel_get

    Gebe alle Artikel zurück
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artikel",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artikel_post(client: TestClient):
    """Test case for artikel_post

    Erstelle einen Artikel
    """
    artikel = {"preis":3.99,"name":"Kirsche","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/artikel",
    #    headers=headers,
    #    json=artikel,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

