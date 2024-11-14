# Modern Portfolio Theory Optimization
Welcome to my portfolio optimization tool repository!

## Overview

My portfolio optimization tool harnesses the power of Mean-Variance Optimization (MVO) to optimize your stock portfolio allocation. By intelligently balancing risk and return, my tool empowers you to achieve optimal diversification and enhance your investment performance. The tool specifically focuses on companies listed in the S&P 500, ensuring that your portfolio optimization is based on a carefully selected subset of stocks representing a diverse range of industries and sectors. This targeted approach enables you to make informed investment decisions tailored to the composition of the S&P 500 index.

## Key Features

- **Historical Data Analysis:** Analyze historical stock price data to understand past performance and trends.
- **Covariance Matrices:** Calculate covariance matrices to quantify the relationships between different stocks in your portfolio.
- **Efficient Frontier Modeling:** Utilize efficient frontier modeling to identify the optimal portfolio allocation that maximizes expected return for a given level of risk.
- **Sharpe Ratio Optimization:** Automatically calculates the optimal weights of allocation for your portfolio to maximize the Sharpe ratio, helping you achieve the best risk-return trade-off.

## Getting Started

To get started with my portfolio optimization tool, follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine using the following command:

    ```
    git clone https://github.com/timoconnnor/PortfolioOptimization.git
    ```

2. **Install Dependencies:** Install any necessary dependencies by running the appropriate package manager command (e.g., `pip install -r requirements.txt`).

3. **Run the Tool:** Execute the main script or application to start using the portfolio optimization tool.

## Usage

To use the portfolio optimization tool, follow these instructions:

1. **Select Start and End Years:** Use the dropdown menus to select the start and end years for your portfolio optimization period. Ensure that the dates are correctly formatted as 'YYYY-MM-DD' (e.g., '2024-01-01').

2. **Input Stock Tickers:** Enter the stock symbols in the provided input fields. You can add multiple stocks by clicking the '+ Add Stock Entry' button.

3. **Calculate and Visualize:** Click the 'Click Here to Create Plot' button to calculate the optimal portfolio weights and visualize the efficient frontier. The tool will download historical price data for the selected stocks, calculate expected returns and covariance matrices, and perform the optimization.

4. **Review Results:** The efficient frontier plot will be displayed, showing the optimal risk-return combinations. You can see the expected returns, volatility, and Sharpe ratio of your portfolio.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
