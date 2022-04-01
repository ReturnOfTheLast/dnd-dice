# Import randint
from random import randint

# Method to calculate the probability of beating a specific Difficulty Class
def prob_check(dc: int, mod: int) -> tuple:
    norm = (21 + mod - dc)/20
    adv = 1 - (1 + mod - dc)**2 / 400
    dis = (21 + mod - dc)**2 / 400

    return norm, adv, dis

# Method to calculate the probability of hitting a specific Armor Class
def prob_hit(ac: int, mod: int) -> tuple:
    norm, adv, dis = prob_check(ac, mod)

    if norm < 1/20: norm = 1/20
    elif norm > 19/20: norm = 19/20

    if adv < 1 - 19**2 / 400: adv = 1 - 19**2 / 400
    elif adv > 1 - 1 / 400: adv = 1 - 1 / 400

    if dis < 1/400: dis = 1/400
    elif dis > 19**2 / 400: dis = 19**2 / 400

    return norm, adv, dis

# Roll Dice
def roll(n: int, s: int, m: int) -> int:
    t = 0
    for _ in range(n): t += randint(1, s)
    t += m
    return t

# Roll Dice Groups (Optional Comment)
def roll_groups(dgs: list) -> list:
    r = list()
    for dg in dgs:
        n = dg[0]
        s = dg[1]
        m = dg[2]

        try:
            c = dg[3]
        except IndexError:
            c = ""

        t = roll(n, s, m)

        r.append((t, c))

    return r
