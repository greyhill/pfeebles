class Effect(object):
  def __init__(self, name, description):
    self._name = name
    self._description = description

  @property
  def name(self): return self._name

  def str(self): return 0
  def dex(self): return 0
  def con(self): return 0
  def int(self): return 0
  def wis(self): return 0
  def cha(self): return 0

  def hp(self): return 0
  def touch_ac(self): return 0
  def flat_ac(self): return 0

  def initiative(self): return 0
  def base_attack(self): return 0

  def fortitude_save(self): return 0
  def reflex_save(self): return 0
  def will_save(self): return 0

  def melee_bonus(self): return 0
  def ranged_bonus(self): return 0

class Character(object):
  def __init__(self, name):
    self._name = name
    self._effects = []
    self.hit_dice = []
    self._wounds = 0

  @property
  def effects(self):
    return self._effects

  @property
  def name(self): return self._name

  def injure(self, damage):
    self._wounds += damage

  def heal(self, damage):
    self._wounds -= damage
    self._wounds = min(0, self._wounds)

  @property
  def max_hp(self):
    return sum(self.hit_dice) + sum([x.hp() for x in self.effects])

  @property
  def str(self): return 10 + sum([x.str() for x in self.effects])
  @property
  def dex(self): return 10 + sum([x.dex() for x in self.effects])
  @property
  def con(self): return 10 + sum([x.con() for x in self.effects])
  @property
  def int(self): return 10 + sum([x.int() for x in self.effects])
  @property
  def wis(self): return 10 + sum([x.wis() for x in self.effects])
  @property
  def cha(self): return 10 + sum([x.cha() for x in self.effects])

  @property
  def hp(self): return self.max_hp - self._wounds
  @property
  def touch_ac(self): return sum([x.touch_ac() for x in self.effects]) + 10
  @property
  def flat_ac(self): return sum([x.touch_ac() for x in self.effects]) + 10

  @property
  def initiative(self): return sum([x.initiative() for x in self.effects])
  @property
  def base_attack(self): return sum([x.base_attack() for x in self.effecs])

  @property
  def fortitude_save(self): return \
      sum([x.fortitude_save() for x in self.effects])
  @property
  def reflex_save(self): return \
      sum([x.reflex_save() for x in self.effects])
  @property
  def will_save(self): return \
      sum([x.will_save() for x in self.effects])

  @property
  def melee_bonus(self): return sum([x.melee_bonus() for x in self.effects])
  @property
  def ranged_bonus(self): return sum([x.ranged_bonus() for x in self.effects])

