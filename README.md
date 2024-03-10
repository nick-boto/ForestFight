# ForestFight
This is a text-based adventure game, made to test Python classes.

## General Info
*Attack* - This is the basic attack which deals damage equal to `attacker's Damage Base * (1 - defender's IDR / 100)`. If you have more than a certain amount of mana (this starts at 5.0 mana and is halved every level), the attack is considered a *critical hit*, meaning the enemy's defense is not applied.
 - **Sword** - This determines your attack base, which starts at 2.0 but increases by *1.5 for every *sword level* you have. An **Iron Sword** is worth 1 *sword level*, a **Steel Sword** is worth 3, and a **Gold Sword** is worth 5.
 - **Armor** - This determines your incoming damage reduction (*IDR*), which starts at 5.0% but increases by *1.5 for each *armor level* you have. A **Leather Tunic** is worth 2 *armor levels*, and an **Iron Chestplate** is worth 5.

*Use an Item* - Use a consumable item from your inventory. This does NOT take your turn, it uses the item you chose and gives you the effect
 - **Rations** - Eating a pack of rations regenerates 5 health.
 - **Dart** - Throwing a dart deals 1 damage.
 - **Mana Scroll** (Requires **Spellbook**) - Reading a mana scroll gives you 2 *Mana*.

*Mana* - Used to meet the *critical hit requirement* (see *Attack*) and to cast spells with the **Spellbook** (see below). It is passively gained at a rate of 1/every turn, and can be gained from **Mana Scrolls** (see *Use an Item*).

*Work* - Type back a five-character string to get 5 *gold*. Much more inefficient than fighting, but a lot easier.

*Shop* - Using *gold*, you can buy better swords to upgrade your attack (see **Sword**), better armor to upgrade your defense (see **Armor**), and consumable items like rations and darts to use during fights (see *Use an Item*).

**Spellbook** - This unlocks two spells, *Fireball* (which deals damage equal to your *Mana*, ignoring damage reduction, requiring 2 *Mana*) and Lightning Bolt (which lowers the enemy's *IDR* by 1.0%, requiring 3 *Mana*). Casting a spell uses all your *Mana*, no matter what the spell's *Mana* requirement is.
