import pfeebles

level0_spells = [ 'acid splash', 'bleed', 'brand', 'create water', 'daze',
    'detect magic', 'detect poison', 'disrupt undead', 'guidance', 'light', 
    'read magic', 'resistant', 'sift', 'stabilize', 'virtue' ]
level1_spells = [ 'alarm', 'bane', 'bless', 'bless water', 'burst bonds',
    'cause fear', 'command', 'comprehend languages', 'cure light wounds',
    'curse water', 'detect chaos', 'detect evil', 'detect good', 'detect law',
    'detect undead', 'disguise self', 'divine favor', 'doom', 
    'expeditious retreat', 'hide from undead', 'inflight light wounds',
    'magic weapon', 'protection from chaos', 'protection from evil',
    'protection from good', 'protection from law', 'remove fear',
    'sanctuary', 'shield of faith', 'tireless pursuit', 'true strike',
    'wrath' ]

class Inquisitor(object):
  def __init__(self):
    self.level = 0

    self.hit_dice = []

    self._l0_spells = []
    self._l1_spells = []

    self.level_up()

  def __str__(self): return "Inquisitor (level %d)" % self.level

  @property
  def name(self): return "Inquisitor"

  def level_up(self):
    self.level += 1
    if self.level == 1:
      # level 1
      self.hit_dice.append(pfeebles.get_int('Inquisitor hit dice (d8)', 1, 8))
      while len(self._l0_spells) < 4: self._l0_spells.append(\
          pfeebles.get_choice('Level 0 spell',
          level0_spells))
      while len(self._l1_spells) < 1: self._l1_spells.append(\
          pfeebles.get_choice('Level 1 spell', 
          level1_spells))

    elif self.level == 2:
      self.hit_dice.append(pfeebles.get_int('Inquisitor hit dice (d8)', 1, 8))
      while len(self._l0_spells) < 5: pfeebles.get_choice('Level 0 spell', 
          level0_spells)
      while len(self._l1_spells) < 3: pfeebles.get_choice('Level 1 spell', 
          level1_spells)

    elif self.level == 3:
      self.hit_dice.append(pfeebles.get_int('Inquisitor hit dice (d8)', 1, 8))
      while len(self._l0_spells) < 6: pfeebles.get_choice('Level 0 spell',
          level0_spells)
      while len(self._l1_spells) < 4: pfeebles.get_choice('Level 1 spell',
          level1_spells)

  def mod_base_attack_bonus(self, c):
    bonuses = [ 0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, \
        9, 10, 11, 12, 12, 13, 14, 15 ]
    return bonuses[self.level - 1]

  def mod_fortitude_save(self, c):
    bonuses = [ 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8,
        9, 9, 10, 10, 11, 11, 12 ]
    return bonuses[self.level - 1]

  def mod_reflex_save(self, c):
    bonuses = [ 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,
        5, 5, 5, 6, 6, 6]
    return bonuses[self.level - 1]

  def mod_will_save(self, c):
    bonuses = [ 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,
        10, 10, 11, 11, 12 ]
    return bonuses[self.level - 1]

  def mod_hit_dice(self, c):
    return sum(self.hit_dice)

  @property
  def attribute_mods(self):
    return []

