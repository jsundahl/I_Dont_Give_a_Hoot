from chemspipy import ChemSpider
import time
import requests

cs = ChemSpider('6baf6039-5c36-49ae-a756-f2d0f8267c37')
time.sleep(5)


def get_mm(compound_name):
    c1 = cs.search(compound_name)
    print(c1)
    time.sleep(5)
    print(c1)
    return c1._results[0].molecular_weight


def g2m(grams, compound_name):
    molar_mass = get_mm(compound_name)
    return grams / molar_mass


def m2g(mols, compound_name):
    molar_mass = get_mm(compound_name)
    return mols * molar_mass


r = g2m(30.1, 'phosphoric acid ')
print(r)