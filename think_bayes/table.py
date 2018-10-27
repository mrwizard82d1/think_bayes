class Table:

    class Row:

        def __init__(self, prior, likelihood):
            self.prior = prior
            self.likelihood = likelihood

        def __repr__(self):
            return 'Table.Row(prior={0}, likelihood={1}'.format(self.prior, self.likelihood)

    def __init__(self, table):
        self._data = table

    def posterior(self, hypothesis):
        normalizing_factor = sum([self._data[h].prior * self._data[h].likelihood for h in iter(self._data)])
        result = (self._data[hypothesis].prior * self._data[hypothesis].likelihood) / normalizing_factor

        return result

