import fractions
import unittest
import think_bayes


word_list = """Four score and seven years ago, our fathers brought forth on this continent a new nation conceived in 
liberty and dedicated to the proposition that all men are created equal. 
        
Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can 
long endure. We are met on a great battlefield of that war. We have come to dedicate a portion of that field, as a final 
resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that 
we should do this.

But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, 
living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will 
little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, 
rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is 
rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take 
increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve 
that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and 
that government of the people, by the people, for the people, shall not perish from the earth.
""".split()

class TestPmf(unittest.TestCase):

    def test_set_fraction(self):
        sut = think_bayes.Pmf()
        for i in range(6):
            sut.set(i, fractions.Fraction(1, 6))

        for i in range(6):
            self.assertEqual(fractions.Fraction(1, 6), sut.probability(i))


    def test_set_float(self):
        sut = think_bayes.Pmf()
        for i in range(6):
            sut.set(i, 1 / 6.0)

        for i in range(6):
            self.assertEqual(1 / 6.0, sut.probability(i))


    def test_increment(self):
        sut = think_bayes.Pmf()

        for word in word_list:
            sut.increment(word)

        self.assertEqual(1, sut.probability('Four'))
        self.assertEqual(9, sut.probability('the'))
        self.assertEqual(13, sut.probability('that'))


    def test_normalize(self):
        sut = think_bayes.Pmf()

        for word in word_list:
            sut.increment(word)
        sut.normalize()

        self.assertEqual(fractions.Fraction(1, 278), sut.probability('Four'))
        self.assertEqual(fractions.Fraction(9, 278), sut.probability('the'))
        self.assertEqual(fractions.Fraction(13, 278), sut.probability('that'))



if __name__ == '__main__':
    unittest.main()
