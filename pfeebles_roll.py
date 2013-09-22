import pfeebles

class RolledAbilities(object):
  def __init__(self, str=None, dex=None, con=None, 
      int=None, wis=None, cha=None):
    self.str = str if str is not None else pfeebles.get_int('Rolled STR')
    self.dex = dex if dex is not None else pfeebles.get_int('Rolled DEX')
    self.con = con if con is not None else pfeebles.get_int('Rolled CON')
    self.wis = wis if wis is not None else pfeebles.get_int('Rolled WIS')
    self.int = int if int is not None else pfeebles.get_int('Rolled INT')
    self.cha = cha if cha is not None else pfeebles.get_int('Rolled CHA')

  def __str__(self): return "Rolled ability scores"

  def mod_str(self, c): return self.str
  def mod_dex(self, c): return self.dex
  def mod_con(self, c): return self.con
  def mod_int(self, c): return self.int
  def mod_wis(self, c): return self.wis
  def mod_cha(self, c): return self.cha

