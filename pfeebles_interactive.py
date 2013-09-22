class ConsoleEngine(object):
  def get_int(self, prompt, min=-9999, max=9999):
    d = int(raw_input("%s: " % prompt))
    while d < min or d > max:
      d = int(raw_input("%s: " % prompt))

  def get_choice(self, prompt, options):
    while True:
      print prompt
      for n, opt in enumerate(options):
        print "[%d] %s" % (n+1, opt)
      v = int(raw_input("Choice: "))
      if v >= 1 and v <= len(opt):
        return v-1

engine = [ConsoleEngine(),]

def set_engine(eng):
  engine[0] = eng

def get_int(prompt, min=-9999, max=9999):
  return engine[0].get_int(prompt)

def get_choice(prompt, options):
  return engine[0].get_choice(prompt, options)

