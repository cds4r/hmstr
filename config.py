"""
    FEATURES:
        1. buy_upgrades -> управление покупкой карточек. 
            True -> Включено, 
            False -> Выключено
        2. buy_decision_method -> метод покупки карточек (
            - price -> покупать самую дешевую
            - payback -> покупать ту, что быстрей всего окупится
            - profit -> покупать самую прибыльну
            - profitness -> покупать самую профитную (сколько добыча на каждый потраченный хома-рубль)
            )
        3. delay_between_attempts -> Задержка между заходами в секундах
        4. num_purchases_per_cycle -> Кол-во покупок карточек за цикл
        5. min_cash_value_in_balance -> Если баланс меньше этого карт
    ACCOUNTS:
        name -> Название аккаунта. Так он будет виден в логе
        token -> токен аккаунта
        proxies -> настройки прокси, "кто знает - тот поймет". Если не нужен прокси, лучше убрать
        buy_upgrades -> Описано в FEATURES, можно указать для каждого аккаунта отдельно
        buy_decision_method -> Описано в FEATURES, можно указать для каждого аккаунта отдельно
"""

try:
    from config_local import FEATURES, ACCOUNTS
except:

    FEATURES = {
        "buy_upgrades": True,
        "buy_decision_method": "payback",
        "delay_between_attempts": 10 * 10,     # эта задержка будет применятся c доп. рандомом ( +/- 60сек )
        "num_purchases_per_cycle": 39,
        "min_cash_value_in_balance": 5_000,
    }

    ACCOUNTS = [
        {"hvh": "account1", "token": "1718902865975GLgIVynDzZLPDwQnc", "buy_upgrades": False, "buy_decision_method": "payback",},
       ## {"osinter": "account3", "token": "1719149435519MdCBJbCSB9S", "buy_upgrades": True, "buy_decision_method": "price",},
    ]
for account in ACCOUNTS:
    account['buy_upgrades'] = account.get('buy_upgrades', FEATURES.get('buy_upgrades', True))
    account['buy_decision_method'] = account.get('buy_decision_method', FEATURES.get('buy_decision_method', 'payback'))
    account['num_purchases_per_cycle'] = account.get('num_purchases_per_cycle', FEATURES.get('num_purchases_per_cycle'))
    account['min_cash_value_in_balance'] = account.get('min_cash_value_in_balance', FEATURES.get('min_cash_value_in_balance', 0))
