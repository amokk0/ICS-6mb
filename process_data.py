""" Делаем Аналіз динаміки оборотних коштів та оборотного капіталу підприємства
"""

from data_service import  get_balance, get_indexes_balance

# Шаблон для заполнения таблицы "Аналіз динаміки оборотних коштів та оборотного капіталу підприємства"
temp_analysis = {
    'name_balance'                      : '',   # Назва підрозділу балансу
    'indicator'                         : '',   # Показник
    'beginning_year'                    : 0,    # На початок року
    '2sq_sum'                           : 0,    # На початок 2 кв. Сумма.грн
    '2sq_tempo_growth'                  : 0,    # На початок 2 кв. Темп росту %
    '3sq_sum'                           : 0,    # На початок 3 кв. Сумма.грн
    '3sq_tempo_growth'                  : 0,    # На початок 3 кв. Темп росту %
    '4sq_sum'                           : 0,    # На початок 4 кв. Сумма.грн
    '4sq_tempo_growth'                  : 0,    # На початок 4 кв. Темп росту %
    'end_year_sum'                      : 0,    # На кінець року Сумма.грн
    'end_year_tempo_growth'             : 0     # На кінець року Темп росту %
}


def get_analytics():
    """ Делаем и возвращаем пользователю Аналіз динаміки оборотних коштів та оборотного капіталу підприємства

    Returns:
        analytics_list: Список динаміки оборотних коштів та оборотного капіталу підприємства
    """

    def get_type_indicators(code):
        """ Вертаємо показник по коду рядка

        Args:
            type_indicators([code]): Код рядка

        Returns:
            [type]: Показник
        """
        for balance_indicator in balance_indicators:
            if balance_indicator[0] == code:
                return balance_indicator[1]

        return "Показник не найден!"


    # Массив с конечной информацией
    analytics_list = []

    # Получаем информацию с двух таблиц
    balance_enterprises = get_balance()
    balance_indicators = get_indexes_balance()

    for balance_enterprise in balance_enterprises:

        # Создаем шаблон заполняемой строки
        temp = temp_analysis.copy()

        temp["name_balance"]            = balance_enterprise[0]                                                     # Назва підрозділу балансу
        temp["indicator"]               = get_type_indicators(balance_enterprise[1])                                # Показник
        temp["beginning_year"]          = round(float(balance_enterprise[2]),1)                                     # На початок року
        temp["2sq_sum"]                 = round(float(balance_enterprise[3]),1)                                     # На початок 2 кв. Сумма.грн
        temp["2sq_tempo_growth"]        = round((100 * float(balance_enterprise[3])) / temp["beginning_year"], 1)   # На початок 2 кв. Темп росту %
        temp["3sq_sum"]                 = round(float(balance_enterprise[4]),1)                                     # На початок 3 кв. Сумма.грн
        temp["3sq_tempo_growth"]        = round((100 * float(balance_enterprise[4])) / temp["2sq_sum"], 1)          # На початок 3 кв. Темп росту %
        temp["4sq_sum"]                 = round(float(balance_enterprise[5]),1)                                     # На початок 4 кв. Сумма.грн
        temp["4sq_tempo_growth"]        = round((100 * float(balance_enterprise[5])) / temp["3sq_sum"], 1)          # На початок 4 кв. Темп росту %
        temp["end_year_sum"]            = round(float(balance_enterprise[6]),1)                                     # На кінець року Сумма.грн
        temp["end_year_tempo_growth"]   = round((100 * float(balance_enterprise[6])) / temp["4sq_sum"], 1)          # На кінець року Темп росту %

        analytics_list.append(temp)


    return analytics_list
