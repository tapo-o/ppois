from uuid import uuid4
from src.techs.Validator import Validator

class Review:
    def __init__(self, author_name: str, text: str):
        Validator.validate_nonempty_str(author_name, "author_name")
        Validator.validate_nonempty_str(text, "text")
        self.__id = str(uuid4())
        self.__author_name = author_name
        self.__text = text
        self.__created = None

    def publish_to_catalog(self, catalog: object) -> None:
        try:
            old = getattr(catalog, "_TourCatalog__title", None)
            if old is not None:
                setattr(catalog, "_TourCatalog__title", old + " • отзыв")
        except Exception:
            pass

    def attach_to_hotel(self, hotel: object) -> None:
        try:
            name = getattr(hotel, "_Hotel__name", "")
            setattr(hotel, "_Hotel__name", name + " (есть отзыв)")
        except Exception:
            pass
