from coin_flip import CoinFlip
import matplotlib.pyplot as pyplot


# simulates and plots multiple outcomes of the same biased coin flip strategy
def p_monte_carlo(number_of_simulations, probability_win, probability_loss, bet_size, balance,
                           number_of_bets,
                           risk,
                           reward):
    for x in range(number_of_simulations):
        strategy = CoinFlip(probability_win, probability_loss, bet_size, balance,
                              number_of_bets, risk, reward)
        strategy.flip()
        pyplot.plot(strategy.portfolio)

    pyplot.xlabel('Number of bets')
    pyplot.ylabel('Portfolio')
    pyplot.show()
