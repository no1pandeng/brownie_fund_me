// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0;

contract SimpleStorage {
    uint256 public favouriteNum = 5;

    function store(uint256 newNum) public returns(uint256) {
        favouriteNum = newNum;
        return favouriteNum;
    }

    struct people {
        uint256 _num;
        string _name;
    }
    people[] public crowds;
    // create dict-like mapping
    mapping(string => uint256) public nameToNum;

    // Use to retun calculated results
    function showNum() public view returns (uint256) {
        return favouriteNum;
    }

    function addPerson(string memory _personName, uint256 _personNum) public {
        crowds.push(people({_name: _personName, _num: _personNum}));
        // get mapping string --> uint256
        nameToNum[_personName] = _personNum;
    }
}
