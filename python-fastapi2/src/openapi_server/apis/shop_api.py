# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.shop_api_base import BaseShopApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from typing import List, Optional
from openapi_server.models.artikel import Artikel


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/artikel",
    responses={
        200: {"model": List[Artikel], "description": "Ok"},
    },
    tags=["Shop"],
    summary="Gebe alle Artikel zurück",
    response_model_by_alias=True,
)
async def artikel_get(
) -> List[Artikel]:
    """Liefert alle Artikel zurück"""
    if not BaseShopApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseShopApi.subclasses[0]().artikel_get()


@router.post(
    "/artikel",
    responses={
        201: {"model": Artikel, "description": "Created"},
    },
    tags=["Shop"],
    summary="Erstelle einen Artikel",
    response_model_by_alias=True,
)
async def artikel_post(
    artikel: Optional[Artikel] = Body(None, description=""),
) -> Artikel:
    """Ein *Artikel* wird erstellt | Tables        | Are           | Cool  | | ------------- |:-------------:| -----:| | col 3 is      | right-aligned | $1600 | | col 2 is      | centered      |   $12 | | zebra stripes | are neat      |    $1 |  Inline-style:  ![alt text](https://d2ms8rpfqc4h24.cloudfront.net/what_factors_to_consider_while_working_with_rest_apis_3e9ffb67d4.jpg \&quot;Logo Title Text 1\&quot;)         """
    if not BaseShopApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseShopApi.subclasses[0]().artikel_post(artikel)
