# nagios
script para nagiosql
Este é um script Python que realiza uma consulta SNMP (Simple Network Management Protocol) para obter o status de uma porta PON (Passive Optical Network) em um dispositivo OLT (Optical Line Terminal).

O script recebe como argumentos o endereço IP da OLT e o número da porta PON. Ele usa o comando snmpwalk para obter o nome da porta PON correspondente e, em seguida, extrai o índice da porta na lista e determina o valor MIB correspondente.

Em seguida, o script verifica se o número da porta começa com algum dos prefixos na lista de prefixos de porta a serem verificadas e usa o valor de "num_elements" para obter os últimos elementos da lista.

Em seguida, o script usa o valor MIB para obter o status atual da porta PON. Ele verifica se o status é 0 (PON está desligada) ou 1 (PON está ligada) e exibe uma mensagem correspondente.

O script retorna um código de saída diferente dependendo do status da porta PON. Se a porta estiver desligada, ele retorna o código 2. Se a porta estiver ligada, ele retorna o código 0. Se ocorrer algum erro durante a execução do script, ele retorna o código 1.

Para utilizar basta roda check_pon.py [HOST IP] [SLOT/PON]
