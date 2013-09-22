class RolledAbilities(object):
  def __init__(self, str=0, dex=0, con=0, int=0, wis=0, cha=0):
    self.str = str
    self.dex = dex
    self.con = con
    self.int = int
    self.wis = wis
    self.cha = cha

  def __str__(self): return "Rolled ability scores"

  def mod_str(self, c): return self.str
  def mod_dex(self, c): return self.dex
  def mod_con(self, c): return self.con
  def mod_int(self, c): return self.int
  def mod_wis(self, c): return self.wis
  def mod_cha(self, c): return self.cha

