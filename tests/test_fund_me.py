from brownie import accounts, network, FundMe, exceptions
from scripts.helpful_scripts import get_account, LOCAL_CHAIN_ENV
import pytest

def test_can():

    account = get_account()
    fund_me = FundMe[-1]
    print(f"fund_me deployed at: {fund_me}")
    entrance_fee = fund_me.getEntranceFee()

    txn1 = fund_me.fund({"from": account, "value": entrance_fee})
    txn1.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    txn2 = fund_me.withdraw({"from": account})
    txn2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0

def test_only_owner():
    # if network.show_active() not in LOCAL_CHAIN_ENV:
    #     pytest.skip("only for local test")
    fund_me = FundMe[-1]
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})