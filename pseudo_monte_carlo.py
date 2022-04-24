from simulation import Simulation
import matplotlib.pyplot as pyplot


def pseudo_simulation_plot(number_of_simulations, probability_win, probability_loss, bet_size, balance,
                           number_of_bets,
                           risk,
                           reward):
    for x in range(number_of_simulations):
        strategy = Simulation(probability_win, probability_loss, bet_size, balance,
                              number_of_bets, risk, reward)
        strategy.flip()
        pyplot.plot(strategy.portfolio)

    pyplot.xlabel('Number of bets')
    pyplot.ylabel('Portfolio')
    pyplot.show()
