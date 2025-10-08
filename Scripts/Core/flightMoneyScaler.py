def flightMoneyScaler(countryDistance):
    extraMoney = 0
    if countryDistance > 9000:
        if countryDistance < 11000:
            extraMoney = 2
        elif 11000 < countryDistance < 13000:
            extraMoney = 4
        elif 13000 < countryDistance < 15000:
            extraMoney = 5
        elif countryDistance > 15000:
            extraMoney = 7
    return extraMoney