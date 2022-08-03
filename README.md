
# Blockchain
Como o próprio nome sugere, blockchain é basicamente um conjunto de blocos que estão conectados de forma criptografada. A ideia principal é que cada bloco tenha: a hash do bloco anterior, sua própria hash e seu dado. Como na figura abaixo:

<img src="/images/Block.png" width="300px">

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
Como todos os blocos do blockchain estão conectados de forma criptografada, qualquer alteração no documento, referência hash, nonce ou código hash pode quebrar a sequência dos blocos. Então, para que seja possível corromper o conteúdo de um bloco, seria necessário que fossem feitas alterações em todos os outros blocos que foram inseridos depois, gerando uma dificuldade imensa para tal. Daí surge um dos principais pilares do blockchain e o principio da imutabilidade de blocos após a inserção. É possível visualizar na imagem abaixo a consequência gerada.

<img src="/images/Imutabilidade.png" width="500px">

## Rede P2P Distribuída
Como o conceito da imutabilidade possibilita que haja (mesmo que seja difícil) a alteração de um bloco e os seus subsequentes, surge um conceito no contexto blockchain que são as redes ponto a ponto distribuidas com o intuito de aumentar a segurança e imutabilidade dos blocos.

A rede P2P distribuida se trata de varios computadores(nós/nodes) conectados entre se (nem todos de maneira ponta a ponta), no qual, todos os nodes contém a lista de blocos adicionados até o momento. 

Para que um bloco seja corrompido/alterado, é necessário que este bloco e todos os subsequentes sejam alterados também. Como este computador (c1) que alterou (sofreu ataque) o bloco pertence a uma rede P2P, os outros computadores vão análisar e perceber que há um erro nos blocos de c1 e o alertando. O computador c1 percebendo ser minoria na rede, aceita os blocos corrigidos e descartas os que foram alterados. Portanto, para que um bloco seja alterado em um blockchain, é necessário que 50% + 1 computadores da rede façam as mesmas alterações em toda a cadeia de blocos (tornando o hackeamento quase impossível dependendo do tamanho da rede).

## Mineração

<img src="/images/Miner.png" width="400px">

### Competição
Para que um node seja o escolhido para adicionar um bloco na rede, o blockchain separa de forma aleatória um conjunto de código hash aceitável. Como o codigo hash até o momento é gerado por dados imutáveis (previousHash e Data) fez-se necessário um novo itém gerador que foi chamado de Nonce (campo de 32 bits). Resumidamente, nonce é a contribuição do node para que o código hash esteja dentro do conjunto aceitável. Visto que a criptografia SHA-256 é não previsível, cada node tenta na força bruta (gera valores aleatórios) encontrar um nonce capaz de obter um hash desejado. O node que encontrar um hash aceito (um nonce que resolva o desafio) ganha o direito de inserir o bloco na rede.

<a href="https://andersbrownworth.com/blockchain/block">Descobrir um nonce válido</a>

## Tolerância a Falhas Bizantima
A ideia do algoritmo é que haja um consenso (sim ou não) da maioria (se houver ele passou/venceu a falha/invasão).

O termo leva o nome do nome conhecido "Problema dos generais bizantinos". Isso foi desenvolvido para descrever uma circunstância em que os atores devem concordar com uma estratégia ou consentimento para evitar falhas catastróficas do sistema. E eles também devem atingir esse objetivo, sabendo que, entre eles, pode haver atores não confiáveis.

O problema dos generais bizantinos foi descrito por Robert Shostak em 1978, no âmbito de um projeto do laboratório de Ciência da Computação da SRI International. Este projeto foi chamado SIFT, e teve o apoio da mesma agência aeroespacial NASA. O caso descrito representa em essência um problema de comunicação distribuída entre computadores. Nele, computadores focados em diferentes propósitos devem ser capazes de estabelecer comunicação em pares e chegar a um consenso. E eles devem ser capazes de fazê-lo, mesmo que alguns deles estejam danificados.

## Protocolo de Consenso
Protocolos de consenso são amplamente utilizados em sistemas distribuídos, permitindo que
um conjunto de processos independentes concorde sobre um mesmo valor proposto.
Baseado nos conceitos das falhas Bizantima, os protocolos de consenso buscam solucionar este problema com maior eficiência e segurança. Diminuindo os pontos de vulnerabilidades. Pensando nisso, há dois protocolos que são os mais conhecidos no contextp blockchain, sendo eles PoW e PoS.
### Proof of Work (PoW) - (Utilizado no Bitcoin)
É justamente a obtenção da hash para o bloco que se quer adicionar à blockchain. 
O primeiro minerador que encontrar o nonce certo e passar na verificação dos outros blocos, ganha as recompensas e também as taxas de mineração, que são as taxas associadas às transações realizadas na blockchain.
Caso dois nodes encontrem a hash no mesmo momento e os disponibilizem à rede de forma simultânea, a rede é subdividida em duas redes, sendo considerada como verdadeira a rede que encontrar o proximo valor hash primeiro.
### Proof of Stake (PoS) - (Utilizado na Ethereum)
É um mecanismo que permite que aqueles que tenham a maior quantidade de criptomoedas associadas àquela blockchain (daí a ideia da 'participação' no nome do mecanismo) "forgem" ou "cunhem" - ou seja, gravem os dados na blockchain. 
O criador de um novo bloco é escolhido de maneira pseudoaleatória, dependendo da riqueza do usuário, também definida como "participação"

## Referências
<a href="https://academy.bit2me.com/pt/o-que-%C3%A9-falha-bizantina/">Falhas Bizantima</a>


# Cripto Moeda (Protocolo)
Cada cripto (protocolo) está associada ao seu blockchain, estabelecendo regras que definem como os 'Nós' se comunicam (consenso, chaves publicas...)

