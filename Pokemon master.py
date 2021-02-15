#class Pokemon

class Pokemon:
  def __init__(self, name, level, experience, typ, maximum_health, current_health, is_knockout):
    self.name = name
    self.level = level
    self.experience = experience
    self.typ = typ
    self.maximum_health = maximum_health
    self.current_health = current_health
    self.is_knockout = is_knockout
    
  def lose_health(self, health):
    self.health = health
    self.current_health = self.current_health - self.health
    if self.current_health == 0 or self.current_health < 0:
      self.is_knockout += 1
      return "{name} pokemon is knocked out".format(name = self.name)
    elif self.current_health < self.maximum_health:
      return "{name} now has {new_health}".format(name=self.name, new_health=self.current_health)
    elif self.current_health == self.maximum_health:
      return "{name} now has {new_health}".format(name=self.name, new_health=self.new_health)
    elif self.current_health > self.maximum_health:
      new_new_health = self.maximum_health - self.health
      self.current_health = new_new_health
      return "{name} now has {new_new_health}".format(name = self.name, new_new_health = new_new_health)
    
  def gain_health(self, health):
    self.health = health
    new_health = self.current_health + self.health
    self.current_health = new_health
    if new_health < self.maximum_health:
      return "{name} now has {new_health}".format(name=self.name, new_health=new_health)
    elif new_health == self.maximum_health:
      return "{name} now has {new_health}".format(name=self.name, new_health=new_health)
    elif new_health > self.maximum_health:
      new_health = self.maximum_health
      return "{name} now has {max_health}".format(name = self.name, max_health = self.maximum_health)
  
  def knockout(self, health):
    self.health = health
    if self.health == 0:
      self.is_knockout += 1
    return "{name} was knockout {knockout} times".format(name = self.name, knockout = self.is_knockout)
  
  def revive_after_knockout(self, knockout):
    if knockout == True:
      self.current_health = self.maximum_health
      return "Your pokemon {name} was revived and has now {health} health".format(name = self.name, health = self.maximum_health)
  
  def attack(self, enemy):
    self.enemy = enemy
    
    if self.current_health == 0:
      return "{name} is not able to attack another Pokemon".format(name = self.name)
    
    if enemy.typ == 'Grass' and self.typ == 'Fire': #first type of fighters
      extra_damage = self.level * 2
      current_enemy_health = enemy.lose_health(extra_damage)
      if enemy.current_health <= 0 and self.experience < 100:
        self.experience = self.experience + 10
        return "{cur_health}. You got new experience +{exp}".format(enemy_name = enemy.name, cur_health = current_enemy_health,exp = self.experience)
      elif self.experience >= 100 :
        self.experience = self.experience % 100
        self.level += 1
        return "{cur_health}. You increased your level! Now you have level {level}".format(cur_health = current_enemy_health, level=self.level)
    else:
      return "{enemy_name} has received {damage} damage and {cur_health} health".format(enemy_name = enemy.name, damage = extra_damage, cur_health = current_enemy_health)
      
    if enemy.typ == 'Fire' and self.typ =='Grass': #second type of fighters
      half_damage = self.level * 0.5
      current_enemy_health = enemy.lose_health(half_damage)
      if enemy.current_health <= 0 and self.experience < 100:
        self.experience = self.experience + 10
        return "{cur_health}. You got new experience +{exp}".format(enemy_name = enemy.name, cur_health = current_enemy_health,exp = self.experience)
      elif self.experience >= 100 :
        self.experience = self.experience % 100
        self.level += 1
        return "{cur_health}. You increased your level! Now you have level {level}".format(cur_health = current_enemy_health, level=self.level)
    else:
      half_damage = self.level * 0.5
      return "{enemy_name} has received {damage} damage and {cur_health} health".format(enemy_name = enemy.name, damage = half_damage, cur_health = current_enemy_health)
    
    if enemy.typ == 'Fire' and self.typ == 'Water':
      normal_damage = self.level * 1
      current_enemy_health = enemy.lose_health(normal_damage)
      if enemy.current_health < 0 and self.experience < 100:
        enemy.is_knockout += 1
        self.experience = self.experience + 10
        return "{name} pokemon is knocked out. Your increased your experience +{exp}".format(name = enemy.name, exp=self.experience)
      elif self.experience >= 100 :
        self.experience = 0
        self.level += 1
        return "You increased your level! Now you have level {level}".format(level=self.level)
    else:
      return "{enemy_name} has received {damage} damage and {cur_health} health".format(enemy_name = enemy.name, damage = normal_damage, cur_health = current_enemy_health)
    
  def evolution(self, level):
    if self.level == 10:
      self.maximum_health = 300
      return "{name} has evolved and has now {max_health}".format(name = self.name, max_health = self.maximum_health)
  
  def __repr__(self):
    return self.name
    
#class Trainer

class Trainer:
  def __init__(self, name, num_potions, pokemons, active_pokemon):
    self.name = name
    self.num_potions = num_potions
    self.pokemons = pokemons
    self.active_pokemon = active_pokemon
    
  def heal(self, active_pokemon):
    self.num_potions = self.num_potions - 1
    cur_health = active_pokemon.gain_health(50)
    if active_pokemon.current_health >= active_pokemon.maximum_health:
      active_pokemon.current_health = active_pokemon.maximum_health
      return "You used 1 potion, now have {num_potions} and you healed {active_pokemon} pokemon. They now has {cur_health}".format(num_potions = self.num_potions, active_pokemon = self.active_pokemon, cur_health = active_pokemon.current_health)
    else:
      return "You used 1 potion, now have {num_potions} and you healed {active_pokemon} pokemon. They now has {cur_health}".format(num_potions = self.num_potions, active_pokemon = self.active_pokemon, cur_health = active_pokemon.current_health)
  
  def attack_another_trainer(self, trainer):
    self.trainer = trainer.name
    attack = self.active_pokemon.attack(trainer.active_pokemon)
    return "{trainer_name} was attacked and their pokemon {trainer_active_pokemon} got damage from {self_active_pokemon}. {attack}".format(trainer_name = trainer.name, attack = attack, trainer_active_pokemon = trainer.active_pokemon, self_active_pokemon = self.active_pokemon)
  
  def switch_active_pokemon(self, new_pokemon):
    for new_pokemon in self.pokemons:
      if new_pokemon.current_health < 0 or new_pokemon.current_health == 0:
        return "{new} is not avaiable. {old} is still your active pokemon".format(new=new_pokemon.name, old = self.active_pokemon)
      else:
        return "{new_active} is now active pokemon".format(new_active = self.active_pokemon)
    
#class Charmander

class Charmander(Pokemon):
  def __init__(self, level):
    pass
    
#Pokemons

charmander = Pokemon("Charmander", 1, 0, "Fire", 100, 100, 0)
oddish = Pokemon("Oddish", 1, 0, 'Grass', 100, 100, 0)
charizard = Pokemon("Charizard", 4, 0, "Fire", 150, 150, 0)

#Trainers

Teodor = Trainer("Teodor", 4, [charmander, oddish], charmander)

Luisa = Trainer("Luisa", 3, [charizard], charizard)

#Print it out!


