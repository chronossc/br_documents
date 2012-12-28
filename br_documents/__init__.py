# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, unicode_literals)

__version__ = '0.0.1-p1'

import random

try:
    basestring
except NameError:
    # Python 3
    # basestring = str
    # long = int
    basestring = str
    long = int

class InvalidCPF(ValueError):
    pass


class CPF(object):
    """
    This object represents a valid CPF number.

    CPF number is portuguese for Natural Persons Register, a unique number
    attributed by Brazillian revenue agency to both Brazillias and resident
    aliens who pay taxes or take part in activities that provide revenue.

    CPF number is formed by XXX.XXX.XXX-XX where two last digits are validation
    digits. Some examples of CPF can be found on doctests.

    You can learn more about CPF at:
        - http://en.wikipedia.org/wiki/Cadastro_de_Pessoas_F%C3%ADsicas
        - http://www.python.org.br/wiki/VerificadorDeCpf

    >>> a = CPF(87234238115)
    >>> a
    <CPF: 87234238115>
    >>> str(a) == '87234238115'
    True
    >>> b = CPF('29057139332')
    >>> c = CPF(29057139332)
    >>> d = CPF('290.571.393-32')
    >>> b == c, b == d
    (True, True)
    >>> c.formated == '290.571.393-32'
    True
    >>> c[0]
    2
    """

    error_messages = {
        'invalid_cpf': 'This CPF is invalid.',
        'only_digits': 'CPF requires only digits. You can use \'.\' and \'-\''
                        'in long format values.',
        'max_digits': 'CPF requires 11 digits or 14 characters'
    }

    cpf = None

    def __init__(self, cpf):

        # is better handle all stuff as string, because we have CPFs starting
        # with zeros at left
        if isinstance(cpf, CPF):
            self.cpf = str(cpf)  # in case something send a CPF instance as value
        elif isinstance(cpf,(list, tuple, basestring)):
            self.cpf = ''.join([str(x) for x in cpf if x not in ('-', '.')])
        elif isinstance(cpf, (int, long)):
            self.cpf = str(int(cpf))

        if not self.cpf.isdigit():
            raise InvalidCPF(self.error_messages['only_digits'])

        if len(self.cpf) != 11:
            raise InvalidCPF(self.error_messages['max_digits'])

        # turn into a list of integers for validation
        self.cpf = list(map(int, self.cpf))

        if not self.is_valid:
            raise InvalidCPF(self.error_messages['invalid_cpf'])

    @property
    def is_valid(self):

        if not self.cpf:
            raise ValueError("Where is the cpf?")

        # by calculation, cpfs with same number in all size is valid, but it
        # isnt :)
        invalid_cpfs = list(map(lambda x: str(x)*11, range(0,10)))

        if str(self.cpf) in invalid_cpfs:
            raise InvalidCPF(self.error_messages['invalid_cpf'])

        cpf = self.cpf[:9]

        # lets create verification digits, exactly like
        # http://www.python.org.br/wiki/VerificadorDeCpf @line 125 does


        while len(cpf) < 11:
            r = sum(
                    # in python3, map give us a mapobject
                    list(map(lambda x: (len(cpf) + 1 - x[0]) * x[1],
                                                                enumerate(cpf)))
                ) % 11

            if r > 1:
                f = 11 - r
            else:
                f = 0

            cpf.append(f)

        return cpf == self.cpf

    def __repr__(self):
        return "<CPF: %s>" % self.__str__()

    def __unicode__(self):
        return ''.join(list(map(str,self.cpf)))

    def __str__(self):
        return self.__unicode__()

    def __int__(self):
        raise ValueError("CPF cant be represented as integer because of leading"
                                                                    " zeroes")

    def __getitem__(self, i):
        return self.cpf[i]


    def __eq__(self, other):
        return isinstance(other, CPF) and self.cpf == other.cpf

    def __len__(self):
        return 11  # len(self.cpf) always is 11

    def __nonzero__(self):
        return True  # Invalid CPFs raise InvalidCPF at __init__

    @property
    def formated(self):
        cpf = self.__str__()
        return ''.join([cpf[:3], '.', cpf[3:6], '.', cpf[6:9], '-', cpf[9:]])


def CPFGenerator():
    """
    returns a Valid CPF, based on http://www.python.org.br/wiki/GeradorDeCpf

    >>> cpf = CPFGenerator()
    >>> len(cpf) == 11
    True
    >>> CPF(cpf).is_valid
    True

    """

    ns = [random.randrange(10) for i in range(9)]
    ns.reverse()

    digits = list(map(lambda n: n[0] * n[1], enumerate(ns,2)))
    vd1 = 11 - round(sum(digits) % 11)
    if vd1 >= 10:
        vd1 = 0

    digits = list(map(lambda n: n[0] * n[1], enumerate([vd1]+ns,2)))
    vd2 = 11 - round(sum(digits) % 11)
    if vd2 >= 10:
        vd2 = 0

    ns.reverse()

    return str(CPF(list(map(int,ns+[vd1,vd2]))))



if __name__ == "__main__":

    import doctest, sys
    doctest.testmod(sys.modules[__name__])
