from brownie import FundMe, MockV3Aggregator, network, config
from pytest import console_main
from scripts.helpful_scripts import get_account, deploy_mock_aggregator, LOCAL_BLOCKCHAIN_ENVIRONMENTS, FORKED_LOCAL_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    current_network = network.show_active()
    if current_network not in  LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][current_network]["eth_usd_address"]
    else:
        # if ganache development environment (local), then
        # we first deploy mock aggregator contract
        # we then assign address of mock aggregator contract to fund me contract price aggregator
        deploy_mock_aggregator(account)
        price_feed_address = MockV3Aggregator[-1].address

    # pass the price feed address to our fundme contract
    fund_me_contract = FundMe.deploy(price_feed_address, {"from": account}, publish_source=config["networks"][current_network].get("verify"))
    print(f"Contract deployed to ${fund_me_contract.address}")
    return fund_me_contract

def main():
    deploy_fund_me()