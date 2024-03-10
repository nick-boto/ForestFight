from game import *
import time, outpost

print(' ___  __   __   ___  __  ___     ___    __       ___ ')
print('|__  /  \ |__) |__  /__`  |     |__  | / _` |__|  |  ')
print('|    \__/ |  \ |___ .__/  |     |    | \__> |  |  |  ')

try:
  with open('Player.txt', 'r') as f:
    textLine = f.readlines()
    playerName = textLine[0].rstrip()
    player = Player('player')
    inventory = {
      'gold': int(textLine[24].strip('Gold: ').rstrip()),
      'sword': textLine[22].rstrip(),
      'armor': textLine[23].rstrip(),
      'spellbook': False,
    }
    inventoryConsumables = {
      'healing': int(textLine[25].strip('Rations: ').rstrip()),
      'attack': int(textLine[27].strip('Darts: ')),
      'mana': int(textLine[26].strip('Mana Scrolls: ').rstrip()),
    }
    player.update(playerName, textLine[3].rstrip(), textLine[4].rstrip(), textLine[7].rstrip(), textLine[8].rstrip(), textLine[11].rstrip(), textLine[14].rstrip(), textLine[15].rstrip(), textLine[18].rstrip(), textLine[19].rstrip(), inventory, inventoryConsumables)
    print(f'Welcome back, {playerName}!')
    print('You wake up from your nap in the Outpost, feeling fully energized!')
    playerLocation = 'outpost'
  
except:
  player = Player(input('Welcome, brave explorer! Enter your name. >>> '))
  print(f'{player.name}, welcome to the Forest!')
  print('There is a great treasure hidden somewhere within the Forest, but you must find it before the Outpost is destroyed!')
  print('You must now fight your way through the forest to start mapping it. Return to the Outpost if you need to rest!')
  print('You enter the Forest, ready to start your journey.')
  player.save()
  playerLocation = 'forest'

print('\n\n')
action = ''

while True:
  while playerLocation == 'forest':
    enemy = player.hunt()
    print(f'You have encountered a {enemy.name}!')
  
    while player.hp > 0:
      player.mana += 1
      player.hp = float(int(player.hp))
      print(f'You have {player.hp} health left and {player.mana} mana ready.')
      action = input('Enter \'a\' to attack, \'u\' to use an item, or \'r\' to run away. >>> ')
      print()
      
      if action == 'a':
        print(f'You hit the {enemy.name}, dealing {player.attackOther(enemy)} damage!')
        if enemy.hp <= 0:
          break
      
      elif action == 'u' and player.inventory['spellbook']:
        action = input(f'Your items list consists of {player.inventoryConsumables["healing"]} rations (\'r\'), {player.inventoryConsumables["mana"]} mana scrolls (\'m\'), and {player.inventoryConsumables["attack"]} darts (\'d\'). Which would you like to use? >>> ')
        print()
        if action == 'r' and player.inventoryConsumables['healing'] > 0:
          print('You eat 1 pack of rations and regain 5 health.')
          player.hp += 5
          player.inventoryConsumables['healing'] -= 1
        elif action == 'm' and player.inventoryConsumables['mana'] > 0 and player.inventory['spellbook']:
          print('You read out the incantation on 1 mana scroll, causing the scroll to disappear and you to gain 2 mana.')
          player.mana += 2
          player.inventoryConsumables['mana'] -= 1
        elif action == 'd' and player.inventoryConsumables['attack'] > 0:
          print(f'You throw 1 dart at the {enemy.name}, dealing 1 damage.')
          enemy.hp -= 1
          player.inventoryConsumables['attack'] -= 1
        elif action == 'r' or action == 'm' or action == 'd':
          print('You don\'t have that item!')
        else:
          print('You get confused and decide not to use an item.')
        player.mana -= 1
        print()
        continue
      
      elif action == 'u':
        action = input(f'Your items list consists of {player.inventoryConsumables["healing"]} rations (\'r\') and {player.inventoryConsumables["attack"]} darts (\'d\'). Which would you like to use?')
        print()
        if action == 'r' and player.inventoryConsumables['healing'] > 0:
          print('You eat 1 pack of rations and regain 5 health.')
          player.hp += 5
          player.inventoryConsumables['healing'] -= 1
        elif action == 'd' and player.inventoryConsumables['attack'] > 0:
          print(f'You throw 1 dart at the {enemy.name}, dealing 1 damage.')
          enemy.hp -= 1
          player.inventoryConsumables['attack'] -= 1
        elif action == 'r' or action == 'm' or action == 'd':
          print('You don\'t have that item!')
        else:
          print('You get confused and decide not to use an item.')
        player.mana -= 1
        print()
        continue
      
      elif action == 'r':
        break
      
      else:
        print('You get confused and decide not to do anything.')
        print(f'Fortunately, your confusion seems to effect the {enemy.name}, and they do nothing on their turn.')
        player.mana -= 1
        print()
        continue
      
      player.save()
      print()
      
      if enemy.hasCrit and enemy.mana < enemy.critReq:
        print(f'The {enemy.name} charges up a critical hit!')
        enemy.mana += 1
      print(f'The {enemy.name} hits you, dealing {enemy.attackOther(player)} damage!')

      print()
  
    if enemy.hp <= 0:
      rewards = enemy.die()
      player.exp += rewards['exp']
      player.inventory['gold'] += rewards['gold']
      player.levelUp()
      print('\n\n')
      
      if enemy.name == "Dragon":
        print('You have reached the heart of the Forest, where you see a huge diamond, the fabled treasure of the Forest! You have won the game!')
        print('Thanks for playing! ForestFight made by Nick')
        break
  
      player.save()
    
    elif player.hp <= 0:
      print(f'You are struck down by the fearsome {enemy.name}, and the world goes out of focus...')
      time.sleep(5)
      print('.')
      time.sleep(1)
      print('..')
      time.sleep(1)
      print('...')
      print('\n\n')
      print('...you wake up back at the Outpost, unsure how you got there but happy to be alive. You seem to have lost all your gold and prepared mana, though.')
      player.inventory['gold'] = 0
      player.mana = 0
      playerLocation = 'outpost'

    elif action == 'r':
      print(f'You decide to make a run for the outpost, the {enemy.name} is not worth the trouble.')
      print('You get there safely, and are able to recover from your wounds after about half an hour. You\'ve spent all your mana casting healing spells, though.')
      print('\n\n')
      player.mana = 0
      playerLocation = 'outpost'

  while playerLocation == 'outpost':
    player.hp = player.maxHp
    print('At the Outpost, the shop is open, and you are able to buy things or work.')
    action = input('Enter \'s\' to shop, \'w\' to work, \'q\' to save and quit, \'t\' to use the computer terminal, or \'v\' to venture out into the forest. >>> ')
    print()
    if action == 's':
      outpost.shop(player)
      player.save()
    elif action == 'w':
      outpost.work(player, action)
      player.save()
    elif action == 'v':
      playerLocation = 'forest'
    elif action == 'q':
      player.save()
      print('You decide to lie down for a nap, and fade into a dreamless sleep.')
      quit()
    elif action == 't':
      outpost.terminal(player)
    print('\n\n')