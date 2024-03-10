import random
import time

class Entity:
  
  def __init__(self, name, atk, prot, hp, maxHp, mana, critReq, hasCrit):
    self.name = str(name)
    self.atk = float(atk)
    self.prot = float(prot)
    self.hp = float(hp)
    self.maxHp = float(maxHp)
    self.mana = float(mana)
    self.critReq = float(critReq)
    self.hasCrit = bool(hasCrit)
    self.type = 'Entity'

  def save(self):
    with open(f'{self.type}.txt', 'w') as f:
      f.write(str(self.name))
      f.write('\n')
      f.write('\n')
      f.write("Attack and Protection Stats:\n")
      f.write(str(self.atk))
      f.write('\n')
      f.write(str(self.prot))
      f.write('\n')
      f.write('\n')
      f.write("Health Points and Health Point Maximum:\n")
      f.write(str(self.hp))
      f.write('\n')
      f.write(str(self.maxHp))
      f.write('\n')
      f.write('\n')
      f.write('Mana Points:\n')
      f.write(str(self.mana))
      f.write('\n')
      f.write('\n')
      f.write('Critical Hit Information:\n')
      f.write(str(self.hasCrit))
      f.write('\n')
      f.write(str(self.critReq))

  def update(self, name, atk, prot, hp, maxHp, mana, critReq, hasCrit):
    self.name = str(name)
    self.atk = float(atk)
    self.prot = float(prot)
    self.hp = float(hp)
    self.maxHp = float(maxHp)
    self.mana = float(mana)
    self.critReq = bool(critReq)
    self.hasCrit = float(hasCrit)
      
  def attackOther(self, other):
    if self.mana >= self.critReq and self.hasCrit == True:
      other.hp -= self.atk
      damage = self.atk
    else:
      other.hp -= self.atk * (1 - other.prot)
      damage = self.atk * (1 - other.prot)
    if other.hp <= 0:
      other.hp = 0
    return damage

class Enemy(Entity):
  
  def __init__(self, name, atk, prot, hp, maxHp, mana, critReq, hasCrit, level):
    super().__init__(name, atk, prot, hp, maxHp, mana, critReq, hasCrit)
    self.level = level
    self.type = 'Enemy'

  def update(self, name, atk, prot, hp, maxHp, mana, critReq, hasCrit, level):
    super().__init__(name, atk, prot, hp, maxHp, mana, critReq, hasCrit)
    self.level = level
  
  def die(self):
    print(f'You have slain the {self.name}!')
    rewards = {'exp': 0, 'gold': 0}
    rewards['gold'] = random.randint(self.level * 2, self.level * 5) * 10
    rewards['exp'] = random.randint(self.level, self.level * 2) * 10
    return rewards

class Goblin(Enemy):

  def __init__(self):
    super().__init__('Goblin', 2, 0.0625, 10, 10, 0, 0, False, 1)

class Wolf(Enemy):

  def __init__(self):
    super().__init__('Wolf', 2.5, 0.125, 25, 25, 0, 0, False, 2)

class GiantSpider(Enemy):

  def __init__(self):
    super().__init__('Giant Spider', 5, 0.25, 32.5, 32.5, 0, 0, False, 3)

class Skeleton(Enemy):

  def __init__(self):
    super().__init__('Skeleton', 6.25, 0.5, 25, 25, 0, 0, False, 3)

class Knight(Enemy):

  def __init__(self):
    super().__init__('Knight', 7.5, 0.625, 50, 50, 0, 3, True, 4)

class Dragon(Enemy):

  def __init__(self):
    super().__init__('Dragon', 10, 0.75, 100, 100, 0, 2, True, 5)

class Player(Entity):

  maxLevel = 10

  def __init__(self, name):
    super().__init__(name, 2, 0.05, 25, 25, 0, 5, True)
    self.exp = 0.0
    self.level = 1.0
    self.nextLevel = 100.0
    self.inventory = {
      'gold': 0,
      'sword': 'Stone Knife',
      'armor': 'Cotton Shirt',
      'spellbook': False,
    }
    self.inventoryConsumables = {
      'healing': 0,
      'mana': 0,
      'attack': 0,
    }
    self.type = 'Player'

  def save(self):
    super().save()
    with open(f'{self.type}.txt', 'w') as f:
      f.write('\n')
      f.write('\n')
      f.write('Level and Experience Points:\n')
      f.write(str(self.exp))
      f.write('\n')
      f.write(str(self.level))
      f.write('\n')
      f.write('Inventory:\n')
      f.write(str(self.inventory['sword']))
      f.write('\n')
      f.write(str(self.inventory['armor']))
      f.write('\nGold: ' + str(self.inventory['gold']))
      f.write('\nRations: ' + str(self.inventoryConsumables['healing']))
      f.write('\nMana Scrolls: ' + str(self.inventoryConsumables['mana']))
      f.write('\nDarts: ' + str(self.inventoryConsumables['attack']))
      if self.inventory['spellbook']:
        f.write('\nSpellbook')
  
  def update(self, name, atk, prot, hp, maxHp, mana, critReq, hasCrit, exp, level):
    super().update(name, atk, prot, hp, maxHp, mana, critReq, hasCrit)
    self.exp = float(exp)
    self.level = int(level)
    self.nextLevel = 100
    for i in range(int(self.level)):
      self.nextLevel *= 1.25

  def heal(self):
    if self.mana >= 2:
      self.hp += self.mana
      if self.hp >= self.maxHp:
        self.hp = self.maxHp
      self.mana = float(0)
    else:
      print('You don\'t have enough mana to heal!')

  def levelUp(self):
    if self.exp >= self.nextLevel and self.level < self.maxLevel:
      self.level += 1.0
      self.nextLevel *= 1.25
      self.exp = 0.0
      self.maxHp *= 1.5
      self.hp = self.maxHp
      self.critReq /= 2.0
      self.hasCrit = True
      print(f'You have reached level {self.level}!')
    else:
      print(f'You need {self.nextLevel - self.exp} more experience to level up!')

  def hunt(self):
    enemies = [Goblin()]
    if self.level >= 2:
      enemies += [Wolf()]
    if self.level >= 3:
      enemies += [GiantSpider(), Skeleton()]
    if self.level >= 4:
      enemies += [Knight()]
    if self.level >= 5:
      enemies += [Dragon()]
    other = random.choice(enemies)
    for x in range(random.randint(1, 5)):
      print('You are venturing through the forest...')
      time.sleep(1)
    return other