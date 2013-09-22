class Inquisitor(object):
  def __init__(self, level=1):
    self.level = level

  def __str__(self): return "Inquisitor (level %d)" % self.level

  def hit_dice(self): return self.level

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

