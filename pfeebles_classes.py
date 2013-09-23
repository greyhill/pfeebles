import pfeebles

inq_level0_spells = ( 'acid splash', 'bleed', 'brand', 'create water', 'daze',
    'detect magic', 'detect poison', 'disrupt undead', 'guidance', 'light', 
    'read magic', 'resistant', 'sift', 'stabilize', 'virtue' )
inq_level1_spells = ( 'alarm', 'bane', 'bless', 'bless water', 'burst bonds',
    'cause fear', 'command', 'comprehend languages', 'cure light wounds',
    'curse water', 'detect chaos', 'detect evil', 'detect good', 'detect law',
    'detect undead', 'disguise self', 'divine favor', 'doom', 
    'expeditious retreat', 'hide from undead', 'inflight light wounds',
    'magic weapon', 'protection from chaos', 'protection from evil',
    'protection from good', 'protection from law', 'remove fear',
    'sanctuary', 'shield of faith', 'tireless pursuit', 'true strike',
    'wrath' )

inq_spell_list = ( inq_level0_spells, inq_level1_spells )

class Inquisitor(object):
  base_attack_bonuses = [ 0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, \
        9, 10, 11, 12, 12, 13, 14, 15 ]
  fortitude_save_bonuses = [ 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8,
      9, 9, 10, 10, 11, 11, 12 ]
  reflex_save_bonuses = [ 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,
      5, 5, 5, 6, 6, 6]
  will_save_bonuses = [ 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,
      10, 10, 11, 11, 12 ]

  spell_list = inq_spell_list

  def __init__(self):
    self.level = 0

    self.hit_dice = []

    self._known_spells = [ [], [], [], [], [], [] ]

    self.level_up()

  def __str__(self): return "Inquisitor (level %d)" % self.level

  @property
  def name(self): return "Inquisitor"

  def level_up(self):
    self.level += 1

    if self.level == 1:
      # level 1
      self.hit_dice.append(pfeebles.get_int('Inquisitor hit dice (d8)', 1, 8))
      while len(self._known_spells[0]) < 4: self._learn_spell(0)
      while len(self._known_spells[1]) < 1: self._learn_spell(1)

    elif self.level == 2:
      self.hit_dice.append(pfeebles.get_int('Inquisitor hit dice (d8)', 1, 8))
      while len(self._known_spells[0]) < 5: self._learn_spell(0)
      while len(self._known_spells[1]) < 3: self._learn_spell(1)

    elif self.level == 3:
      self.hit_dice.append(pfeebles.get_int('Inquisitor hit dice (d8)', 1, 8))
      while len(self._known_spells[0]) < 6: self._learn_spell(0)
      while len(self._known_spells[1]) < 4: self._learn_spell(1)
 
  def _learn_spell(self, level):
    while True:
      choice = pfeebles.get_choice('Select level %d spell' % level,
          self.spell_list[level])
      if choice not in self._known_spells[level]:
        self._known_spells[level].append(choice)
        return

  def mod_base_attack_bonus(self, c):
    return self.base_attack_bonuses[self.level - 1]

  def mod_fortitude_save(self, c):
    return self.fortitude_save_bonuses[self.level - 1]

  def mod_reflex_save(self, c):
    return self.reflex_save_bonuses[self.level - 1]

  def mod_will_save(self, c):
    return self.will_save_bonuses[self.level - 1]

  def mod_hit_dice(self, c):
    return sum(self.hit_dice)

  @property
  def attribute_mods(self):
    return []

