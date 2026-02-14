import json
import os
from bank_acc import BankAccount
import logging

# ================= LOGGING =================
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)
logger = logging.getLogger(__name__)

DATA_FILE = 'account.json'

class BankManager:
    def __init__(self):
        self.accounts = self._load_accounts()
        
    def _load_accounts(self):
        if not os.path.exists(DATA_FILE):
            return {}
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return {
                k: BankAccount.from_dict(v) for k, v in data.items()
            }
            
    def _save_accounts(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in self.accounts.items()},
                f,
                indent=4
            )
    
    def create_account(self, account_number, holder_name):
        if account_number in self.accounts:
            raise ValueError("Account number already exists.")
        self.accounts[account_number] = BankAccount(account_number, holder_name)
        self._save_accounts()
        logger.info("Created account %s for %s", account_number, holder_name)
        
    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account number does not exist.")
        return self.accounts[account_number]
    
