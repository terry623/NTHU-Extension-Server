from datetime import date
# FIXME: 日期若一樣還沒有處理
# 0  第 1 次選課
# 1  第 1 次選課 log 記錄
# 2  第 1 次選課亂數結果
# 3  第 2 次選課
# 4  第 2 次選課 log 記錄
# 5  第 2 次選課結束(已亂數處理)
# 6  第 3 次選課
# 7  第 3 次選課 log 記錄
# 8  第 3 次選課結束(已亂數處理)
# 9 加退選開始前(含擋修、衝堂)
# 10 加退選 log 記錄
# 11 加退選結束(已處理)
# 12 停修 log 記錄
date_1 = date(2018, 6, 7)
date_2 = date(2018, 6, 11)
date_4 = date(2018, 6, 14)
date_5 = date(2018, 6, 18)
date_7 = date(2018, 8, 24)
date_8 = date(2018, 8, 28)
date_9 = date(2018, 8, 29)
date_10 = date(2018, 9, 6)
date_11 = date(2018, 9, 25)
date_12 = date(2018, 10, 29)
# today = date.today()
today = date(2018, 8, 25)

collection = {
    '1': date_1,
    '2': date_2,
    '4': date_4,
    '5': date_5,
    '7': date_7,
    '8': date_8,
    '9': date_9,
    '10': date_10,
    '11': date_11,
    '12': date_12
}


def getCloseDay(pos):
    if pos == 1:
        result = nearest_positive(collection.values(), today)
    else:
        result = nearest_negative(collection.values(), today)
    return result


def nearest_positive(items, pivot):
    close = date(2020, 1, 1)
    for n in items:
        gap = n - pivot
        if n < close and gap.days > 0:
            close = n
    return close


def nearest_negative(items, pivot):
    close = date(2016, 1, 1)
    for n in items:
        gap = n - pivot
        if n > close and gap.days < 0:
            close = n
    return close


def getCountDown():
    pos = 1
    target_day = getCloseDay(pos)
    countdown = (target_day - date.today()).days
    return countdown


def getCurrentPhase():
    pos = 0
    target_phase = getCloseDay(pos)
    print(target_phase)
    currentphase = list(collection.keys())[
        list(collection.values()).index(target_phase)]
    return currentphase
