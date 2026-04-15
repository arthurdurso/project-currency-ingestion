import dlt
import requests
from dlt.sources import DltResource
from typing import Iterator


# FreeCurrency API base URL
BASE_URL = "https://api.freecurrencyapi.com/v1"

# Target currencies available in the FreeCurrency API
DEFAULT_CURRENCIES = "EUR,GBP,JPY,USD,MXN,CAD,AUD"


@dlt.source(name="freecurrency")
def freecurrency_source(
        api_key: str = dlt.secrets.value,
        base_currency: str = "BRL",
        currencies: str = DEFAULT_CURRENCIES,
) -> DltResource:
    """
    dlt source that exposes the latest exchange rates from the FreeCurrency API.

    Args:
        api_key: API key loaded from SOURCES__FREECURRENCY__API_KEY.
        base_currency: Base currency for the rates (default BRL).
        currencies: Comma-separated list of target currencies.
    """
    return latest_rates(api_key = api_key, base_currency=base_currency, currencies=currencies)


@dlt.resource(name="latest_rates", write_disposition="append")
def latest_rates(
        api_key: str,
        base_currency: str,
        currencies: str,
) -> Iterator[dict]:
    """
    Retrieves the latest exchange rates and yields one record per currency,

    including base currency, target currency, rate, and extraction timestamp.
    """
    from datetime import datetime, timezone

    response = requests.get(
        f"{BASE_URL}/latest",
        params={
            "apikey": api_key,
            "base_currency": base_currency,
            "currencies": currencies,
        },
        timeout=30,
    )

    response.raise_for_status()

    payload = response.json()
    data: dict = payload.get("data", {})
    extracted_at = datetime.now(timezone.utc).isoformat()

    for target_currency, rate in data.items():
        yield {
            "base_currency": base_currency,
            "target_currency": target_currency,
            "rate": rate,
            "extracted_at": extracted_at,
        }