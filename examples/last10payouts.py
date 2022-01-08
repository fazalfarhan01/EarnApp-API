from pyEarnapp import EarnApp

auth_tokens = [
]

number_of_payouts = 5


for auth in auth_tokens:
    api = EarnApp(auth)
    user_info = api.get_user_data()
    transaction_info = api.get_transaction_info()
    print(f'[i] ID: {user_info.email:20s}')
    for transaction in transaction_info.transactions[:number_of_payouts]:
        print(f'{transaction.amount:6.2f} redeemed on {transaction.redeem_date.strftime("%d/%m/%Y")} to {transaction.email} is {transaction.status:12s}')