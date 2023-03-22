#!/usr/bin/env python3
#-----------------------------------------------------------------------
# Nagios check PON in OLT Fiberhome
# This plugin check status of all ONUs connected in a specific PON 
# and return if these ONUs operational state is UP or DOWN
#
# ----
# -----
# Usage:
# ./check_pon_fiberhome [IP_OLT] [PON_SLOT/PON_PORT]
# Like:
# ./check_pon_fiberhome 10.10.10.1 1/8
# put only the slot_number and pon_number before and after slash /
#
#
# In nagios service.cfg use:
# check_command:        check_pon_fiberhome!10.10.10.1!1/8
#-----------------------------------------------------------------------
import sys
import subprocess

# Recebe os argumentos da linha de comando
olt_ip = sys.argv[1]
olt_port = sys.argv[2]

# Executa o comando snmpwalk para obter o nome da porta PON correspondente
pon_name = subprocess.getoutput(f"snmpwalk -Os -c adsl -v 1 {olt_ip} 1.3.6.1.4.1.5875.800.3.9.3.4.1.2")
pon_name_list = pon_name.split()

# Extrai o indice da porta na lista e determina o valor MIB correspondente
indice = None
for i, elem in enumerate(pon_name_list):
    if olt_port in elem:
        indice = i
        break
if indice is None:
    print("Porta nao encontrada")
    sys.exit(1)
mib = pon_name_list[indice-4]

# Define uma lista com os prefixos das portas a serem verificadas
port_prefixes = ["2","3","4","7"]

# Verifica se o número da porta começa com algum dos prefixos na lista
num_elements = 10 if any(olt_port.startswith(prefix) for prefix in port_prefixes) else 9

# Usa o valor de "num_elements" para obter os últimos elementos da lista
mib_port = mib[-num_elements:]

# Obtem o status atual da porta PON usando o valor MIB
mib_status = "1.3.6.1.4.1.5875.800.3.9.3.4.1.5"
readport = subprocess.getoutput(f"snmpwalk -Os -c adsl -v 1 {olt_ip} {mib_status}{mib_port}")

# Obtém o último caractere da string "readport" e converte em um inteiro
status = int(readport[-1])

if status == 0:
    print("PON is Down")
    sys.exit(2)

if status == 1:
    print("PON is Up")
    sys.exit(0)