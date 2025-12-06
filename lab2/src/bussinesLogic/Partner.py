from uuid import uuid4
from src.techs.Validator import Validator
from typing import Optional
from src.products.TourCatalog import TourCatalog

class Partner:
    def __init__(self, name: str, level: str = "bronze"):
        Validator.validate_nonempty_str(name, "name")
        self.__id = str(uuid4())
        self.__name = name
        self.__level = level
        self.__offers_shared = 0
        self.__requested_campaign: Optional[str] = None

    def share_offer(self, catalog: TourCatalog) -> None:
        self.__offers_shared += 1
        try:
            old = getattr(catalog, "_TourCatalog__title", "")
            setattr(catalog, "_TourCatalog__title", old + f" • offer from {self.__name}")
        except Exception:
            pass

    def request_campaign(self, campaign_id: str) -> None:
        self.__requested_campaign = campaign_id
