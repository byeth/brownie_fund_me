from traceback import FrameSummary
from brownie import FundMe,MockV3Aggregator, accounts,network,config
from scripts.helper_scripts import deploy_mocks, get_account,LOCAL_BLOCKCHAIN_ENVIRONMENTS

from web3 import Web3



def deploy_fund_me():
    account = get_account()
    #pass the price feed adress to fundme contract
    #if we are in a persistent network like rinkeby, use the associated
    #address otherwise use mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:#!= "development":
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"] #"0x8A753747A1Fa494EC906cE90E9f37563A8AF630e"
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    
    fund_me = FundMe.deploy(price_feed_address,{"from":account},publish_source=config["networks"][network.show_active()].get("verify"))
    
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()