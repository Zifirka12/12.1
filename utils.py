import json
import os
from typing import List, Dict, Union

import requests


def read_transactions(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """
    Читает данные о транзакциях из JSON-файла.

    Args:
        file_path: Путь к JSON-файлу.

    Returns:
        Список словарей с данными о транзакциях.
    """
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []


def get_transaction_amount_rub(transaction: Dict[str, Union[str, float]]) -> float:
    """
    Возвращает сумму транзакции в рублях.

    Args:
        transaction: Словарь с данными о транзакции.

    Returns:
        Сумма транзакции в рублях (float).
    """
    amount = transaction["amount"]
    currency = transaction.get("currency", "RUB")

    if currency != "RUB":
        # Получение курса валют с exchangeratesapi.io
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/latest?access_key=zreg2uCOFNUBn4Or2wvNJ1VlpSF22ByN&base=RUB&symbols={currency}"
        )
        data = response.json()
        if data["success"]:
            exchange_rate = data["rates"][currency]
            amount *= exchange_rate
        else:
            raise ValueError("Не удалось получить курс валют")

    return amount
