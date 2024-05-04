from src.widget import mask_number, convert_date_format
import pytest

"""
# Проверка функции mask_number()
"""


@pytest.mark.parametrize(
    "input_number, expected_output",
    [
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("Maestro 9876543210987654", "Maestro 9876 54** **** 7654"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Some_Text_123456", "Some_Text_123456")
    ]
)
def test_mask_number(input_number: str, expected_output: str) -> None:
    assert mask_number(input_number) == expected_output
    assert mask_number(input_number) == expected_output
    assert mask_number(input_number) == expected_output
    assert mask_number(input_number) == expected_output


"""
# Проверка функции convert_date_format()
"""


def test_convert_date_format() -> None:
    assert convert_date_format("2018-07-11T02:26:18.671407") == "11.07.2018"
    assert convert_date_format("2023-12-31T23:59:59.999999") == "31.12.2023"
