
# Blockchain
Como o próprio nome sugere, blockchain é basicamente um conjunto de blocos que estão conectados de forma criptografada. A ideia principal é que cada bloco tenha: a hash do bloco anterior, sua própria hash e seu dado. Como na figura abaixo:

<div style="text-align: center">
    <img src="/images/Block.png" width="300px">
</div>


## Entendendo Hash SHA 256
É uma maneira muito segura de criptografar dados utilizada na construção do blockchain. O código hash gerado é composto por 64 caracteres em que qualquer dado/arquivo digital pode ser criptografado pela Hash SHA-256.

### Tem-se 5 requisitos para um algoritmo Hash
1. Sem retorno (Não é possivel transformar o codigo em arquivo/dado novamente)
1. Determinístico (O mesmo arquivo/dado deve sempre apresentar o mesmo código hash)
1. Processamento rápido
1. Efeito avalanche (Qualquer alteração no documento gerador deve alterar o código hash)
1. Deve suportar colisões

<a href="https://tools.superdatascience.com/blockchain/hash/">Simulador Hash</a>

## Registros Imutáveis
