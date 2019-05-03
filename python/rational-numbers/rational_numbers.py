from __future__ import division
import math as m

class Rational(object):
    def __init__(self, numer, denom):
        denomSign = m.copysign(1, denom)
        gdc = m.gcd(numer, denom)
        self.numer = int(numer / gdc * denomSign)
        self.denom = int(denom / gdc * denomSign) 

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        resultNumer = self.numer * other.denom + self.denom * other.numer
        resultDenom = 1
        if resultNumer != 0 :
            resultDenom = self.denom * other.denom
        return Rational(resultNumer, resultDenom)

    def __sub__(self, other):
        resultNumer = self.numer * other.denom - self.denom * other.numer
        resultDenom = 1
        if resultNumer != 0 :
            resultDenom = self.denom * other.denom
        return Rational(resultNumer, resultDenom)

    def __mul__(self, other):
        resultNumer = self.numer * other.numer
        resultDenom = 1
        if resultNumer != 0 :
            resultDenom = self.denom * other.denom
        return Rational(resultNumer, resultDenom)

    def __truediv__(self, other):
        resultNumer = self.numer * other.denom
        resultDenom = 1
        if resultNumer != 0 :
            resultDenom = self.denom * other.numer
        return Rational(resultNumer, resultDenom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power > 0:
            resultNumer = pow(self.numer, power)
            resultDenom = pow(self.denom, power)
        else:
            resultNumer = pow(self.denom, power)
            resultDenom = pow(self.numer, power)
        return Rational(resultNumer, resultDenom)

    def __rpow__(self, base):
        return pow(base, self.numer / self.denom)
