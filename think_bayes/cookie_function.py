import fractions


def cookie_function(bowl, cookie):
    probability = {'bowl1': fractions.Fraction(1, 2),
                   ('vanilla', 'bowl1'): fractions.Fraction(30, 40),
                   'vanilla': fractions.Fraction(50, 80)}
    result = (probability[bowl] * probability[(cookie, bowl)]) / probability[cookie]
    return result
