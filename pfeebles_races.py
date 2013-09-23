import pfeebles

class HalfOrc(object):
  def __init__(self, bonus=None):
    bonus_to = [ 'str', 'con', 'dex', 'wis', 'int', 'cha' ]
    if bonus is None or bonus not in bonus_to:
      b = pfeebles.get_choice("Half-orc racial bonus:",
          ['STR', 'CON', 'DEX', 'WIS', 'INT', 'CHA'])
      self.bonus = bonus_to[b]

  def __str__(self): return 'Half-orc bonus'

  def mod_str(self, char): return 2 if self.bonus == 'str' else 0
  def mod_con(self, char): return 2 if self.bonus == 'con' else 0
  def mod_dex(self, char): return 2 if self.bonus == 'dex' else 0
  def mod_wis(self, char): return 2 if self.bonus == 'wis' else 0
  def mod_int(self, char): return 2 if self.bonus == 'int' else 0
  def mod_cha(self, char): return 2 if self.bonus == 'cha' else 0

