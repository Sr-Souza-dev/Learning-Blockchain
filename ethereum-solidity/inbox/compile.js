const path = require('path');
const fs = require('fs');
const solc = require('solc'); 

const inboxPath = path.resolve(__dirname, 'contracts', 'inbox.sol');
const source = fs.readFileSync(inboxPath, 'utf8');
 
var solcInput = {
    language: "Solidity",
    sources: { 
        contract: {
            content: source
        }
     },
    settings: {
        optimizer: {
            enabled: true
        },
        evmVersion: "byzantium",
        outputSelection: {
            "*": {
              "": [
                "legacyAST",
                "ast"
              ],
              "*": [
                "abi",
                "evm.bytecode.object",
                "evm.bytecode.sourceMap",
                "evm.deployedBytecode.object",
                "evm.deployedBytecode.sourceMap",
                "evm.gasEstimates"
              ]
            },
        }
    }
};

solcInput = JSON.stringify(solcInput);

console.log("Inicio");
console.log(JSON.parse(solc.compile(solcInput)));
console.log("FIm");

