from re import A
from brownie import network, FundMe, accounts, exceptions
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from scripts.deploy import deploy_fund_me
import pytest

def test_can_fund_and_withdraw():
    test_fund_me_contract = deploy_fund_me()
    account = get_account()
    #test funding transaction
    funding_amt = test_fund_me_contract.getEntranceFee() + 100
    tx1 = test_fund_me_contract.fund({"from": account, "value": funding_amt})
    tx1.wait(1)

    # test if the balance in account is equal to funding amount we initially sent
    assert test_fund_me_contract.addressToAmountFunded(account.address) == funding_amt

    tx2 = test_fund_me_contract.withdraw({"from": account})
    tx2.wait(1)
    
    assert test_fund_me_contract.addressToAmountFunded(account.address) == 0


# def test_only_owner_can_withdraw():
    
#     # run test only in ganache-local
#     if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
#         pytest.skip("Test runs only in ganache local environment")    
    
#     test_fund_me_contract = deploy_fund_me()
#     account = accounts.add()
#     account2 = get_account()
    
#     # funding_amt = test_fund_me_contract.getEntranceFee()
#     # tx1 = test_fund_me_contract.fund({"from": account2, "value": funding_amt})
#     # tx1.wait(1)

#     with pytest.raises(exceptions.VirtualMachineError):
#         test_fund_me_contract.withdraw({"from": account2})


    






    
