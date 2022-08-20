def simplify(numerator, denominator):
    divided = False
    while divided == False:
        for i in range(2, 10):
            if numerator%i == denominator%i:
                newnumerator //= i
                newdenominator //= 1
                divided = True
                break

def simplify(numerator, denominator):
    divided = False
    for i in range(2, 10):
        if numerator%i == denominator%i:
            numerator1 //= i
            denominator1 //= i
        else
            divided = True
            
### ^ OUR ATTEMPTS AT MAKING A FUNCTION ^ ###

class Fraction():
  def __init__(self,numerator,denominator):
    self.numerator = numerator
    self.denominator = denominator

  def __repr__(self):
    return "{0}/{1}".format(self.numerator,self.denominator)

  def __add__(self, other):
    if self.denominator == other.denominator:
      newnumerator = self.numerator + other.numerator
      return Fraction(newnumerator, self.denominator)
    else:
      numerator1 = self.numerator * other.denominator
      denominator1 = self.denominator * other.denominator
      numerator2 = other.numerator * self.denominator
      denominator2 = other.denominator * self.denominator
      numerator3 = numerator1 + numerator2
      for i in range(2, 10):
            if numerator3%i == denominator1%i:
                numerator3 //= i
                denominator1 //= i
                break
      return Fraction(numerator3, denominator1)

  def __sub__(self, other):
    if self.denominator == other.denominator:
      newnumerator = self.numerator + other.numerator
      return Fraction(newnumerator, self.denominator)
    else:
      numerator1 = self.numerator * other.denominator
      denominator1 = self.denominator * other.denominator
      numerator2 = other.numerator * self.denominator
      denominator2 = other.denominator * self.denominator
      numerator3 = numerator1 - numerator2
      for i in range(2, 10):
          if numerator3%i == denominator1%i:
              numerator3 //= i
              denominator1 //= i
              break
      return Fraction(numerator3, denominator1)

  def __mul__(self, other):
    newnumerator = self.numerator * other.numerator
    newdenominator = self.denominator * other.denominator
    for i in range(2, 10):
          if newnumerator%i == newdenominator%i:
              newnumerator //= i
              newdenominator //= i
              break
    return Fraction(newnumerator, newdenominator)

  def __floordiv__(self, other):
    newnumerator = self.numerator * other.denominator
    newdenominator = self.denominator * other.numerator
    for i in range(2, 10):
        if newnumerator%i == newdenominator%i:
            newnumerator //= i
            newdenominator //= i
            break
    return Fraction(newnumerator, newdenominator)

  def getter(self):
      return self.numerator / self.denominator

  def setter(self, newnumerator, newdenominator):
      self.numerator = newnumerator
      self.denominator = newdenominator

a = Fraction(4, 4)
b = Fraction(1, 2)
c = a + b