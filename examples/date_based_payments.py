from pyEarnapp import EarnApp

auth_tokens = [
]

number_of_payouts = 5

date_format = "%d/%m/%Y"

date_based_receipt = {}

for auth in auth_tokens:
    api = EarnApp(auth)
    user_info = api.get_user_data()
    transaction_info = api.get_transaction_info()
    print(f'[i] ID: {user_info.email:20s}')
    for transaction in transaction_info.transactions[:number_of_payouts]:
        print(f'{transaction.amount:6.2f} redeemed on {transaction.redeem_date.strftime(date_format)} to {transaction.email} is {transaction.status} {[f"on {transaction.payment_date.strftime(date_format)}" if transaction.status == "paid" else ""][0]}')
        if not date_based_receipt.get(transaction.payment_date.strftime(date_format), False):
            date_based_receipt[transaction.payment_date.strftime(date_format)] = 0
        date_based_receipt[transaction.payment_date.strftime(date_format)] += transaction.amount
for key,value in date_based_receipt.items():
    print(f"Received {value} on {key}")
