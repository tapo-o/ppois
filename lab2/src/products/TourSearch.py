from typing import List
from src.products.TourCatalog import TourCatalog
from src.exceptions.exceptions import TourNotFoundException 

class TourSearch:
    def __init__(self):
        self.__last_query = ""
        self.__last_results: List[object] = []

    def find_by_price(self, catalog: TourCatalog, min_price: float, max_price: float) -> List[object]:
        if min_price < 0 or max_price < min_price:
            raise ValueError("Некорректный диапазон цен")
        self.__last_query = f"price:{min_price}-{max_price}"
        results = []
        for t in catalog.list_tours():
            # используем публичный метод price() если есть
            price_callable = getattr(t, "price", None)
            price = price_callable() if callable(price_callable) else getattr(t, "_Tour__price", 0.0)
            if min_price <= price <= max_price:
                results.append(t)
        if not results:
            raise TourNotFoundException("Туры по цене не найдены")
        self.__last_results = results
        return list(results)

    def find_by_hotel(self, catalog: TourCatalog, hotel_id: str) -> List[object]:
        self.__last_query = f"hotel:{hotel_id}"
        results = []
        for t in catalog.list_tours():
            hotel = getattr(t, "_Tour__hotel", None)
            hid = getattr(hotel, "id", None) or getattr(hotel, "_Hotel__id", None)
            if hid == hotel_id:
                results.append(t)
        if not results:
            raise TourNotFoundException("Туры для отеля не найдены")
        self.__last_results = results
        return list(results)

    def last_query(self) -> str:
        return self.__last_query

