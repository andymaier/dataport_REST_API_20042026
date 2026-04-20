# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from typing import List, Optional
from openapi_server.models.artikel import Artikel


class BaseShopApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseShopApi.subclasses = BaseShopApi.subclasses + (cls,)
    async def artikel_get(
        self,
    ) -> List[Artikel]:
        """Liefert alle Artikel zurück"""
        ...


    async def artikel_post(
        self,
        artikel: Optional[Artikel],
    ) -> Artikel:
        """Ein *Artikel* wird erstellt | Tables        | Are           | Cool  | | ------------- |:-------------:| -----:| | col 3 is      | right-aligned | $1600 | | col 2 is      | centered      |   $12 | | zebra stripes | are neat      |    $1 |  Inline-style:  ![alt text](https://d2ms8rpfqc4h24.cloudfront.net/what_factors_to_consider_while_working_with_rest_apis_3e9ffb67d4.jpg \&quot;Logo Title Text 1\&quot;)         """
        ...
