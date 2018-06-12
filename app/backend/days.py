from datetime import date
# 0  第 1 次選課
# 1  第 1 次選課 log 記錄
# 2  第 1 次選課亂數結果
# 3  第 2 次選課
# 4  第 2 次選課 log 記錄
# 5  第 2 次選課結束(已亂數處理)
# 6  第 3 次選課
# 7  第 3 次選課 log 記錄
# 8  第 3 次選課結束(已亂數處理)
# 9  加退選開始前(含擋修、衝堂)
# 10 加退選 log 記錄
# 11 加退選結束(已處理)
# 12 停修 log 記錄
collection = {
    '1': date(2018, 6, 7),
    # 11 + 1
    '2': date(2018, 6, 12),
    '4': date(2018, 6, 14),
    # 18 + 1
    '5': date(2018, 6, 19),
    '7': date(2018, 8, 24),
    '8': date(2018, 8, 28),
    '9': date(2018, 8, 29),
    '10': date(2018, 9, 6),
    '11': date(2018, 9, 25),
    '12': date(2018, 10, 29)
}

def getCloseDay(pos, today):
    if pos == 1:
        result = nearest_positive(collection.values(), today)
    else:
        result = nearest_negative(collection.values(), today)
    return result


def nearest_positive(items, pivot):
    close = date(2020, 1, 1)
    for n in items:
        gap = n - pivot
        if n <= close and gap.days > 0:
            close = n
    return close


def nearest_negative(items, pivot):
    close = date(2016, 1, 1)
    for n in items:
        gap = n - pivot
        if n >= close and gap.days <= 0:
            close = n
    return close


def getCountDown(today):
    pos = 1
    target_day = getCloseDay(pos, today)
    countdown = (target_day - today).days
    return countdown


def getCurrentPhase(today):
    pos = 0
    target_phase = getCloseDay(pos, today)
    if target_phase != date(2016, 1, 1):
        currentphase = list(collection.keys())[
            list(collection.values()).index(target_phase)]
        return currentphase
    else:
        return 'too_early'
