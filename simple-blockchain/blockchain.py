import datetime       # Para definir a Data atual de cada bloco
import hashlib        # Utilizada parea função hash
import json
from flask import Flask, jsonify

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = "0")
        
    def create_block(self, proof, previous_hash):
        #criando um bloco
        block = {'index': len(self.chain) +1,     
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)                                    # Add o bloco a lista chain
        return block
    
    def get_previous_block(self):
        return self.chain[-1]                                       # Retorna o penultimo itém da lista
    
    # define uma regra de mineração para o blockchain
    def role(self, current_proof, previous_proof):
        r = str(current_proof**2 - previous_proof**2).encode()      # Regra de mineração 
        return hashlib.sha3_256(r).hexdigest()                      # Critografando a regra de mineração por sha-256 e convertendo para hexadecimal
    
    # Descobre uma 'proof' que se encaixa de acordo com a regra de mineração estabelecida
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        
        while check_proof is False:
            hash_operation = self.role(new_proof, previous_proof)   # Critografando a regra de mineração por sha-256 e convertendo para hexadecimal
            if hash_operation[:4] == '0000' :                       # Verificando se o 'new_proof' aplicado a regra de mineração atende ao requisito hash de ter os 4 primeiros caracteres sendo 0
                check_proof = True
            else:
                new_proof += 1
        
        return new_proof                                            # Retorna a 'proof' que atendeu a regra de mineração e a condição imposta
     
    # Converte um bloco no seu código hash-sha256
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()  # Transformando o bloco no formato Json
        return hashlib.sha3_256(encoded_block).hexdigest()          # Criptografa pela sha-256 e converte para hexadecimal
    
    # Verifica se o bloco é valido para a cadeia
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        
        while block_index < len(chain):
            block = chain[block_index]
            
            # Verifica se previous_hash realmente bate com o codigo hash(sha256) do bloco anterior
            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            # Verifica se a 'proof' minerada é válida de acordo com a regra estabelecida
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = self.role(proof, previous_proof)
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    
    

app = Flask(__name__)                                   # Inicializa o flask (ferramenta facilitadora para levantar servidor)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
blockchain = Blockchain()

# Definindo Função e rota para minerar um bloco
@app.route('/mine_block', methods=["GET"])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {"message": "Parabéns você minerou um bloco",
                "index": block['index'],
                "timestamp": block['timestamp'],
                "proof": block['proof'],
                "previous_hash": block['previous_hash']}
    return jsonify(response), 200

# Definindo Função e rota para recuperar o chain de blocos
@app.route("/get_chain", methods=["GET"])
def get_chain():
    response = {"chain": blockchain.chain,
                "length": len(blockchain.chain)}
    return jsonify(response), 200

# Definindo Função e rota para verificar se o blockchain ainda é válido
@app.route("/is_valid", methods=["GET"])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {"message": 'Tudo Certo'}
    else:
        response = {"message": "O blockchain não é válido"}
    return jsonify(response), 200

# Executando a aplicação/servidor criado pelo flask
app.run(host="0.0.0.0", port=5000)