import logging

# ================= LOGGING =================
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)
logger = logging.getLogger(__name__)

class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
        self.transactions = []
        
    def deposit(self, amount):
        self._validate_amount(amount)
        self.balance += amount
        self._log_transaction("DEPOSIT", amount)
        logger.info("Deposited %.2f to account %s", amount, self.account_number)
        
    def withdraw(self, amount):
        self._validate_amount(amount)
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance for withdrawal.")
        self.balance -= amount
        self._log_transaction("WITHDRAW", amount)
        logger.info("Withdrew %.2f from account %s", amount, self.account_number)
        
    def _validate_amount(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive.")
        
    def _log_transaction(self, transaction_type, amount):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance_after": self.balance
        }
        self.transactions.append(transaction)
        
    def to_dict(self):
        return {
            "account_no": self.account_number,
            "holder_name": self.holder_name,
            "balance": self.balance,
            "transactions": self.transactions
        }
    
    @staticmethod
    def from_dict(data):
        account = BankAccount(
            data["account_no"],
            data["holder_name"],
            data["balance"]
        )
        account.transactions = data["transactions"]
        return account
            
        
    