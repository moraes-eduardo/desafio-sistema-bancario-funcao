## Sobre

Esse projeto é um dos desafios de código propostos no Bootcamp DIO, Python AI Backend Developer (Vivo).


### Módulo

O desafio 'Criando um Sistema Bancário com Python', sob a responsabilidade do professor Guilherme Arthur de Carvalho.


## Tecnologias

- Python 3 (básico)


## Objetivo

Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

### Operação de depósito
Deve ser possível depositar valores positivos para uma conta bancária. A v1 do projeto trabalha com apenas 1 usuário, então não é necessário se preocupar com a identificação do número da agência e nem da conta bancária.

Todos os depósitos devem ser armazenados numa variável e exibidos na operação de extrato.

### Operação de saque
O sistema deve permitir realizar 5 saques diários com limite máximo de R$500,00/saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar dinheiro por falta de saldo.

Todos os saques devem ser armazenados numa variável e exibidos na operação de extrato.

### Operação de extrato
Deve listar todos os depósitos e saques realizados na conta. No fim da lista, deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx.