# ForestFight
This is a text-based adventure game, made to test Python classes.

## General Info
A - Attack, this is your basic hit which deals damage equal to `your attack * (1 - the enemy's defense)`. If you have more than a certain amount of mana (this starts at 5.0 mana and is halved every level), the attack is considered a **critical hit**, meaning the enemy's defense is not applied.
U - Use an Item, this does NOT take your turn, it uses the item you chose and gives you the effect
Mana - Currently unimplemented, this does nothing but give you critical hits. Once the Spellbook is implemented, Mana will be used to activate skills.
Work - Type back a five-character string to get 5 gold. Much more inefficient than the fighting, but a lot easier.
