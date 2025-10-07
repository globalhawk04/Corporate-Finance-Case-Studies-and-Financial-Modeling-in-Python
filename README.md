Corporate Finance Case Studies and Financial Modeling in Python

This repository contains a collection of Python scripts that apply financial theories and modeling techniques to solve complex corporate finance problems. The scripts serve as practical, hands-on examples of how to analyze financing decisions, evaluate derivatives, and use simulation to understand financial outcomes.

The core of this repository is built around detailed case studies, from an academic setting, demonstrating the application of financial principles in a computational environment.

Table of Contents

Description

Core Concepts Demonstrated

Scripts Breakdown

Key Libraries Used

Usage

Disclaimer

Description

This project translates textbook corporate finance problems into executable Python code. Instead of relying solely on spreadsheets, these scripts leverage the power of Python for calculations, simulations, and financial analysis. The repository includes in-depth analysis of debt financing options, interest rate derivatives, and capital budgeting decisions.

Core Concepts Demonstrated

Corporate Financing Decisions: Analyzing and comparing the costs of different methods of raising capital.

Financial Derivatives: Modeling the mechanics and financial impact of interest rate swaps and interest rate caps.

Capital Budgeting: Using Net Present Value (NPV) and Internal Rate of Return (IRR) to make refinancing decisions.

Monte Carlo Simulation: Applying simulation to understand the average outcomes of financial scenarios involving variable interest rates.

Financial Modeling: Structuring problems by defining variables, calculating cash flows, and using financial libraries to derive decision metrics.

Scripts Breakdown

The repository is structured around several key case studies and financial models:

1. The Philadelphia Medical Corporation Case Study (philcase.py and fincase.py)

These two scripts tackle the same problem: analyzing the most cost-effective way for a company to raise $16.5 million. They evaluate and compare four distinct options:

Private Placement Loan: A direct loan from an institutional investor with a front-end fee.

LIBOR-Based Loan with an Interest Rate Swap: Converting a variable-rate loan into a fixed-rate loan.

LIBOR-Based Loan with an Interest Rate Cap: Hedging against rising interest rates by purchasing a cap.

Do Nothing: Analyzing the cost of maintaining the existing debt structure.

fincase.py: Provides a straightforward, direct calculation of the total costs associated with each financing method.

philcase.py: Offers a more formal and advanced analysis. It constructs detailed cash flow schedules for each option and uses the numpy_financial library to calculate the Internal Rate of Return (IRR), providing a robust metric for comparison.

2. Financial Toolkit & Simulations (make.py)

This script is a collection of smaller, focused financial models and simulations:

Bank of St. Louis - Preferred Stock Refinancing: A classic capital budgeting problem. The script uses both the IRR and NPV methods to determine whether the company should refinance its existing preferred stock with a new issue, accounting for flotation costs and dividend savings.

Interest Rate Swap Simulation: A Monte Carlo simulation involving two companies with different credit ratings. It runs millions of iterations with a variable LIBOR to calculate the average net borrowing cost for each company after they engage in an interest rate swap, demonstrating the benefits of the swap.

Discounted Cash Flow (DCF) Simulation: A simple simulation that calculates the present value of a series of cash flows over millions of iterations with a random discount rate (k).

Key Libraries Used

numpy: For numerical operations.

pandas: Used to structure and display cash flow schedules.

numpy_financial: A dedicated library for financial functions like irr().

random: For generating random numbers in the Monte Carlo simulations.

Usage

These scripts are designed as self-contained case study solutions. To use them:

Clone the repository.

Ensure you have the necessary libraries installed:

code
Bash
download
content_copy
expand_less
pip install numpy pandas numpy-financial

Run any script from your terminal:

code
Bash
download
content_copy
expand_less
python philcase.py

The script will execute the financial analysis and print the results—such as costs, IRR, or NPV—directly to the console.

Disclaimer

These scripts are for educational and illustrative purposes only. They are intended to demonstrate the application of financial theory in Python and should not be considered financial advice. All scenarios are based on the specific details provided in the case studies.
