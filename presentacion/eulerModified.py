class EulerModified ():
  def __init__ (self, A, B, C, D, x, u, DT):
    self.A = A
    self.B = B
    self.C = C
    self.D = D
    self.xk = x
    self.uk = u
    self.DT = DT

  def iteration (self):
    self.xpkk = self.xk + self.DT * (self.A * self.xk + self.B * self.uk)
    self.ukk = self.uk
    self.xkk = self.xk + 0.5 * self.DT * (self.A*(self.xk + self.xpkk) + self.B*(self.uk + self.ukk))
    self.xk = self.xkk
    self.uk = self.ukk
    self.yk = self.C * self.xk + self.D * self.uk



