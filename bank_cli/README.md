# Bank Account Simulation

A simple CLI-based bank account manager written in Python. This application allows users to create accounts, deposit and withdraw money, view balances, and review transaction history. All account data is persisted in a JSON file.

## Features
- Create new bank accounts
- Deposit funds
- Withdraw funds
- View account balance
- View transaction history
- Data persistence using `account.json`

## File Structure
- `main.py`: Entry point and CLI interface
- `bank_manager.py`: Manages accounts and operations
- `bank_acc.py`: Defines the account structure and transaction logic
- `account.json`: Stores account data

## Getting Started
### Prerequisites
- Python 3.x

### Running the Application
1. Open a terminal in the project directory.
2. Run:
   ```bash
   python main.py
   ```
3. Follow the on-screen prompts to manage bank accounts.

## Usage
- **Create Account**: Enter a unique account number and holder name.
- **Deposit**: Enter account number and deposit amount.
- **Withdraw**: Enter account number and withdrawal amount.
- **View Balance**: Enter account number to see current balance.
- **View Transactions**: Enter account number to see transaction history.
- **Exit**: Quit the application.

## Logging
- The application uses Python's logging module for info and error messages.

## License
This project is for educational purposes.
