def ac_calc(ac, mod):
    def normal():
        ch = (21 + mod - ac)/20
        if ch < 1/20: ch = 1/20
        elif ch > 19/20: ch = 19/20
        return ch
    def adv():
        ch = 1 - (1 + mod - ac)**2 / 400
        if ch < 1 - 19**2 / 400: ch = 1 - 19**2 / 400
        elif ch > 1 - 1 / 400: ch = 1 - 1 / 400
        return ch
    def dis():
        ch = (21 + mod - ac)**2 / 400
        if ch < 1/400: ch = 1/400
        elif ch > 19**2 / 400: ch = 19**2 / 400
        return ch

    print(f"Normal Roll: {round(normal() * 100, 2)}%\tAdvantage: {round(adv() * 100, 2)}%\tDisadvantage: {round(dis() * 100, 2)}%")
