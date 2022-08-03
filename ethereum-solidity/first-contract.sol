// SPDX-License-Identifier: AFL-3.0
pragma solidity ^0.8.14;                            // Especifica a versão do solidity que está sendo utilizada

contract Inbox{
    string public message;

    constructor(string memory _initialMessage) {
        message = _initialMessage;
    } 

    function setMessage(string memory newMessage) public{
        message = newMessage;
    }

    function getMessage ()public view returns (string memory) {
        return message;
    }

}