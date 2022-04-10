from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    fund_me_contract = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me_contract.getEntranceFee()
    print(f'current entrance fee is {entrance_fee}')

    conversion = fund_me_contract.getConversionRate(20)
    print(f'conversion rate is {conversion}')

    price = fund_me_contract.getPrice()
    print(f'price is {price}')

    raw_price = fund_me_contract.rawPrice()
    print(f'raw price is {raw_price}')

    print('funding....')

    fund_me_contract.fund({"from": account, "value": entrance_fee})

def withdraw():
    fund_me_contract = FundMe[-1]
    account = get_account()
    print('withdrawing funds...')
    fund_me_contract.withdraw({"from": account})

def main():
    fund()
    withdraw()

