from pypfopt import EfficientFrontier # efficient frontier btwn expected returns and SD in a risky asset portfolio
from pypfopt import risk_models # python portfolio optimization risk models
from pypfopt import expected_returns # expected returns are one of the key inputs in MPT
from pypfopt import plotting # allows to plot with pyportfolioopt
import pandas as pd # panel data analytics and stats
import numpy as np # numerical python
import matplotlib.pyplot as plt # mathematical plotting library
import cvxpy # convex optimization in python
import pypfopt.plotting as plotting # python portfolio optimization plotting module
import yfinance as yf

def calculate_graph(start_year, end_year, stock_symbols):

    stock_data = yf.download(stock_symbols, start=start_year, end = end_year)

    stock_data = stock_data["Adj Close"]

    stock_returns = stock_data.pct_change()[1:]


    # forecast expected returns by taking historical average retunrs from the stocks in the list
    mu2 = expected_returns.mean_historical_return(stock_data) # calculates expected returns based on hisotircal mean returns for stocks int he list
    print(mu2)
    type(mu2)


    # creates the variance-covariance matrix of returns for the stocks in the list
    cov_matrix2 = risk_models.sample_cov(stock_data) # creates the covariance matrix
    print(cov_matrix2) # prints the variance-covariance matrix
    type(cov_matrix2) # prints the data type for the variance-covariance matrix

    # calcualtes the portfolio weights that yield the maximum expected sharpe ratio
    ef = EfficientFrontier(mu2, cov_matrix2) # creates the efficient frontier
    ef.max_sharpe() # finds the set of portfolio weights that yield the maximum expected sharpe ratio

    # displays expected returns, volatility, and sharpe ratio
    ef.portfolio_performance(verbose=True)

    # create a new EfficientFrontier instance for plotting
    ef_plot = EfficientFrontier(mu2, cov_matrix2, weight_bounds=(0,1))

    # Get the efficient weights for plotting
    weights_plot = ef_plot.max_sharpe()

    # Calculate and display the portfolio performance
    ef_plot.portfolio_performance(verbose=True)

    # Create a new EfficientFrontier instance for adding constraints
    ef_constraints = EfficientFrontier(mu2, cov_matrix2, weight_bounds=(0, 1))

    # Add the desired constraints to the new instance
    ef_constraints.add_constraint(lambda x: cvxpy.sum(x) == 1) # constraint sum of weights = 1

    # Plot the EF and risky investment set
    fig, ax = plt.subplots()
    plotting.plot_efficient_frontier(ef_constraints, ax=ax, show_assets=True)

    # Highlight the tangency portfolio
    ax.scatter(ef_plot.portfolio_performance()[1], ef_plot.portfolio_performance()[0], marker="*", color="r", s=200, label="Tangency Portfolio")
    ax.legend()

    plt.style.use('fivethirtyeight')
    # Display the plot
    mean_returns = stock_returns.mean()
    std_dev_returns = stock_returns.std()
    print("Mean returns:", mean_returns)
    print("Standard deviation of returns:", std_dev_returns)
    plt.show()