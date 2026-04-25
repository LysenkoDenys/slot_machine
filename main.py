def spin_row():
  pass

def print_row():
  pass

def get_payout():
  pass

def main():
  balance=100
  print('**************************')
  print( 'Welcome to Python slots  ')
  print('Symbols: 🍒 🍉 🍋 🔔 ⭐ ')
  print('**************************')

  while balance>0:
    print(f"Current balance: ${balance}") 

    bet=input('Place your bet amount: ')

    if not bet.isdigit():
      print('please enter a valid number')
      continue

    bet=int(bet)

    if bet>balance:
      print('insufficient funds')
      continue

    if bet<=0:
      print('bet must be greater than 0')
      continue

    balance-=bet

main()
if __name__=='main__':
  main()