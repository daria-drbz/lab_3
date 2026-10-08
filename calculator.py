def calculate_commission(amount: int) -> float:
    """
    Рассчитывает комиссию для денежного перевода.

    Args:
        amount (int): Сумма перевода (от 100 до 50 000 руб.)

    Returns:
        float: Размер комиссии

    Raises:
        ValueError: Если сумма не входит в допустимый диапазон
    """
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise TypeError("Сумма должна быть числом")
    if amount < 100 or amount > 50000:
        raise ValueError("Сумма перевода должна быть от 100 до 50 000 руб.")

    if amount <= 1000:
        return 50.0
    if amount <= 20000:
        return 100.0
    if amount <= 40000:
        return 200.0 + (amount * 0.01)

        # Новое правило: фиксированная комиссия 500 руб. для сумм от 40 001 до 50 000 руб.
    return 500.0