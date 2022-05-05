from brownie import accounts, config, network, FundMe, MockV3Aggregator
from scripts.helpful_scripts import get_account, create_mock_aggreator, LOCAL_CHAIN_ENV, FORKED_CHAIN_ENV

def deploy_fund_me():
    is_virtual_env = network.show_active() in LOCAL_CHAIN_ENV or network.show_active() in FORKED_CHAIN_ENV
    print(f"virtual env is: {is_virtual_env}")
    if not is_virtual_env:
        price_feed_address = config['networks'][network.show_active()][
            'eth_to_usd_feed'
        ]
    else:
        create_mock_aggreator()
        price_feed_address = MockV3Aggregator[-1].address
        print(f"Deploy mocks succeed! Address: {price_feed_address}")

    if_verify = config['networks'][network.show_active()]['verify']
    fund_me = FundMe.deploy(price_feed_address, {"from": get_account(),"gas_price": 20000000000}, publish_source=if_verify)
    print(f"Contract deployed to{fund_me.address}")
    return fund_me

       
def main():
    deploy_fund_me()