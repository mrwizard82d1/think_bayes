import fractions


def cookie_function(bowl, cookie):
    probability = {'bowl1': fractions.Fraction(1, 2),
                   'bowl2': fractions.Fraction(1, 2),
                   ('vanilla', 'bowl1'): fractions.Fraction(30, 40),
                   ('vanilla', 'bowl2'): fractions.Fraction(20, 40),
                   ('chocolate', 'bowl1'): fractions.Fraction(10, 40),
                   ('chocolate', 'bowl2'): fractions.Fraction(20, 40),
                   'vanilla': fractions.Fraction(50, 80),
                   'chocolate': fractions.Fraction(30, 80)}
    result = (probability[bowl] * probability[(cookie, bowl)]) / probability[cookie]
    return result
