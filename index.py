def depositar(saldo, valor):
  """
  Realiza um depósito na conta.

  Args:
      saldo: Saldo atual da conta.
      valor: Valor a ser depositado.

  Returns:
      O novo saldo da conta após o depósito.
  """
  return saldo + valor

def sacar(saldo, valor):
  """
  Realiza um saque na conta.

  Args:
      saldo: Saldo atual da conta.
      valor: Valor a ser sacado.

  Returns:
      O novo saldo da conta após o saque.
  """
  if valor <= saldo:
    return saldo - valor
  else:
    return "Saldo insuficiente!"

def extrato(saldo):
  """
  Exibe o extrato da conta.

  Args:
      saldo: Saldo atual da conta.

  Returns:
      Uma string com o extrato da conta.
  """
  return f"Saldo: R${saldo:.2f}"

# Simulando operações bancárias
saldo = 1000.00

valor_deposito = 500.00
saldo = depositar(saldo, valor_deposito)

valor_saque = 300.00
novo_saldo = sacar(saldo, valor_saque)

extrato_conta = extrato(novo_saldo)

# Imprimindo resultados
print(f"Depósito: R${valor_deposito:.2f}")
print(f"Saque: R${valor_saque:.2f}")
print(extrato_conta)
