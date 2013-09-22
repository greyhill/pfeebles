class AttributeScore(object):
  def __init__(self, name, reasons):
    self._name = name
    self._reasons = reasons

  @property
  def name(self): return self._name

  @property
  def value(self): return sum([ r[0] for r in self._reasons ])

  @property
  def reasons(self): 
    if len(self._reasons) == 1:
      return [self._reasons[:],]
    else:
      return self._reasons[:]

class Stats(object):
  def __init__(self, char):
    self._char = char

  @property
  def char(self):
    return self._char

  def __getattr__(self, name):
    reasons = []
    for r in self.char.attribute_mods:
      if hasattr(r, 'mod_%s' % name):
        mod = getattr(r, 'mod_%s' % name)(self.char)
        reasons.append((mod, r))
    return AttributeScore(name, reasons)

class BaseModifier(object):
  def __str__(self): return "Base"

  def mod_touch_ac(self, char): return 10

class AbilityModifier(object):
  def __str__(self): return 'Ability modifier'

  def mod_str_bonus(self, char): return (char.str - 10) // 2
  def mod_dex_bonus(self, char): return (char.dex - 10) // 2
  def mod_con_bonus(self, char): return (char.con - 10) // 2
  def mod_int_bonus(self, char): return (char.int - 10) // 2
  def mod_wis_bonus(self, char): return (char.wis - 10) // 2
  def mod_cha_bonus(self, char): return (char.cha - 10) // 2

  def mod_fortitude_save(self, char):
    return char.con_bonus
  def mod_reflex_save(self, char):
    return char.dex_bonus
  def mod_will_save(self, char):
    return char.will_bonus
  def mod_melee_attack_bonus(self, char):
    return char.str_bonus
  def mod_ranged_attack_bonus(self, char):
    return char.dex_bonus
  def mod_touch_ac(self, char):
    return char.dex_bonus
  def mod_initiative(self, char):
    return char.dex_bonus

class Character(object):
  def __init__(self, name, roll):
    self._name = name
    self._roll = roll
    self._wounds = 0
    self.classes = []

  @property
  def name(self): return self._name

  @property
  def roll(self): return self._roll

  @property
  def stats(self):
    return Stats(self)

  @property
  def attribute_mods(self):
    return [self.roll, BaseModifier(), AbilityModifier()] + self.classes

  def __getattr__(self, name):
    return getattr(self.stats, name).value

