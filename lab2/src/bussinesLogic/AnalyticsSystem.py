from typing import Dict
from src.techs.Validator import Validator

class AnalyticsSystem:
    def __init__(self, version: str, source: str):
        Validator.validate_nonempty_str(version, "version")
        Validator.validate_nonempty_str(source, "source")
        self.__version = version
        self.__source = source

    # Собирает базовые метрики по компании: число активных контрактов и клиентов
    def collect_metrics(self, company: object) -> Dict[str, float]:
        active_contracts = sum(1 for c in getattr(company, "_Company__contracts", {}).values() if getattr(c, "is_active", lambda: False)())
        clients_count = len(getattr(company, "_Company__clients", {}))
        return {"active_contracts": float(active_contracts), "clients": float(clients_count)}

    # Оценивает доставляемость кампании в процентах (delivered / sent * 100)
    def evaluate_campaign(self, campaign: object) -> float:
        sent = getattr(campaign, "_MarketingCampaign__sent_total", 0)
        delivered = getattr(campaign, "_MarketingCampaign__delivered_total", 0)
        return 0.0 if sent == 0 else (delivered / sent) * 100.0
