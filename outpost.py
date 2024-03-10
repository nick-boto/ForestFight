import random

def shop(player):
  print('You can buy the following things at the shop:')
  itemsList = ['Rations', 'Dart']
  itemsListCosts = [20, 25]

  print(' - Rations. This pack of rations can heal you in a battle. Cost: 20 gold.')
  print(' - Dart. This dart is extremely accurate, but doesn\'t do much damage. Cost: 25 gold.')

  if player.inventory['sword'] == 'Stone Knife':
    itemsList += ['Metal Sword']
    itemsListCosts += [150]
    print(' - Metal Sword. A better sword to swing, and a sharper one, too. Cost: 150 gold.') #3
  elif player.inventory['sword'] == 'Metal Sword':
    itemsList += ['Steel Sword']
    itemsListCosts += [450]
    print(' - Steel Sword. Even sharper than the last, this will cut through all but the strongest foes. Cost: 450 gold.') #4
  elif player.inventory['sword'] == 'Steel Sword':
    itemsList += ['Gold Sword']
    itemsListCosts += [1350]
    print(' - Gold Sword. The pinnacle of melee weapon technology for this age, its strong edge can slay even dragons. Cost: 1350 gold.') #5

  if player.inventory['armor'] == 'Cotton Shirt':
    itemsList += ['Leather Tunic']
    print(' - Leather Tunic. A tunic made from leather, protecting against cold wind and sharp claws alike. Cost: 300 gold.')
    itemsListCosts += [300]
  elif player.inventory['armor'] == 'Leather Tunic':
    itemsList += ['Metal Chestplate']
    print(' - Metal Chestplate. A chestplate, much stronger than your previous armor. Cost: 900 gold.')
    itemsListCosts += [900]

  if player.inventory['spellbook']:
    print(' - Mana Scroll. This scroll will give you more mana when read. Cost: 100 gold.')
    itemsListCosts += [100]
  action = input('Enter the name of the item you would like to buy:')

  for x in itemsList:
    if x == action:
      if player.inventory['gold'] >= itemsListCosts[itemsList.index(x)]:
        print('You bought a ' + action.lower() + '!')
        player.inventory['gold'] -= itemsListCosts[itemsList.index(x)]
        if action.endswith('Sword'):
          player.atk *= 1.5
          if action.startswith('Gold') or action.startswith('Steel'):
            player.atk *= 1.5

        if action == 'Leather Tunic':
          player.prot *= 1.5625
          player.inventory['armor'] = 'Leather Tunic'
        elif action == 'Leather Tunic':
          player.prot *= 1.953125
          player.inventory['armor'] = 'Leather Tunic'

        if action == 'Rations':
          player.inventoryConsumables['healing'] += 1
        elif action == 'Dart':
          player.inventoryConsumables['attack'] += 1
        elif action == 'Mana Scroll':
          player.inventoryConsumables['mana'] += 1

      else:
        print('You don\'t have enough gold!')

def work(player, action):
  while action != 's':
    print('You are working. Enter the sequence of characters below to gain 1 gold, or enter \'s\' to stop working.')
    lettersAvailable = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',   'v', 'w', 'x', 'y', 'z']
    numbersAvailable = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbolsAvailable = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '~', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?']
    sequence = ''

    for x in range(5):
      type = random.choice(['lowerLetters', 'upperLetters', 'numbers', 'symbols'])
      if type == 'lowerLetters':
        sequence += random.choice(lettersAvailable)
      elif type == 'upperLetters':
        sequence += random.choice(lettersAvailable).upper()
      elif type == 'numbers':
        sequence += random.choice(numbersAvailable)
      elif type == 'symbols':
        sequence += random.choice(symbolsAvailable)
    
    print(sequence)
    action = input('>>>')

    while action != 's' and action != sequence:
      print('Try again.')
      action = input('>>>')
    
    if action == sequence:
      print('Gold +1')
      player.inventory['gold'] += 1