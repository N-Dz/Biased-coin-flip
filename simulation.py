import numpy


class CoinFlip:

    def __init__(self, probability_win, probability_loss, bet_size, balance, number_of_bets, risk, reward):
        self.probability_win = probability_win
        self.probability_loss = probability_loss
        self.bet_size = bet_size
        self.balance = balance
        self.number_of_bets = number_of_bets
        self.risk = risk
        self.reward = reward

        self.win_loss = [1, -1]
        self.win = self.win_loss[0]
        loss = self.win_loss[1]
        self.portfolio = [self.balance]
        self.counter = 0

    def flip(self):
        while self.counter < self.number_of_bets:
            outcome = numpy.random.choice(self.win_loss, p=[self.probability_win, self.probability_loss])
            self.counter += 1
            if outcome == self.win:
                self.portfolio.append(self.portfolio[-1] + self.reward * self.bet_size)
            else:
                self.portfolio.append(self.portfolio[-1] - self.risk * self.bet_size)





