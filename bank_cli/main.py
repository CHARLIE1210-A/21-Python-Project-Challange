from bank_manager import BankManager
import logging

# ================= LOGGING =================
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)
logger = logging.getLogger(__name__)

# ================= CLI =================
def main():
    manager = BankManager()
    
    while True:
        logger.info("\n--- Bank Account Manager ---")
        logger.info("1. Create Account")
        logger.info("2. Deposit")       
        logger.info("3. Withdraw")
        logger.info("4. View Balance")
        logger.info("5. View Transactions")
        logger.info("6. Exit\n")
        
        choice = input("Select an option: ")
        try:
            if choice == '1':
                acc_no = input("Enter account number: ")
                holder_name = input("Enter holder name: ")
                manager.create_account(acc_no, holder_name)
                
            elif choice == '2':
                acc_no = input("Enter account number: ")
                amount = float(input("Enter deposit amount: "))
                manager.get_account(acc_no).deposit(amount)
                manager._save_accounts()
                
            elif choice == '3':
                acc_no = input("Enter account number: ")
                amount = float(input("Enter deposit amount: "))
                manager.get_account(acc_no).withdraw(amount)
                manager._save_accounts()
                
            elif choice == '4':
                acc_no = input("Enter account number: ")
                account = manager.get_account(acc_no)
                logger.info("Current balance: %.2f", account.balance)
                
            elif choice == '5':
                acc_no = input("Enter account number: ")
                for t in manager.get_account(acc_no).transactions:
                    logger.info("%s: %.2f (Balance after: %.2f)")
                    
            elif choice == '6':
                logger.info("Exiting...")
                break
            
            else:
                logger.warning("Invalid option. Please try again.")
                
                
        except Exception as e:
            logger.error("Error: %s", e)
            
if __name__ == "__main__":
    main()