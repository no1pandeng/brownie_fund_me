from brownie import accounts, config, network
from brownie import MockV3Aggregator
from web3 import Web3

FORKED_CHAIN_ENV = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_CHAIN_ENV = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    is_virtual_env = network.show_active() in LOCAL_CHAIN_ENV or network.show_active() in FORKED_CHAIN_ENV

    if is_virtual_env:
        print(f"from account:{accounts[0]}")
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def create_mock_aggreator():
    print("Deploying mocks ...")
    if len(MockV3Aggregator) == 0:
        mock_aggregator = MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"),{"from": get_account(),"gas_price": 20000000000})

       