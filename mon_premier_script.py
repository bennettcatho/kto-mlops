
import unittest

class TestNamesMethod(unittest.TestCase):
     def test_saluer(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = names(first_names=prenoms)
        self.assertEqual(more_than_seven, 4)

def names(first_names):
    long_names_amount = 0
    for first_name in first_names:
        if len(first_name) > 7:
            long_names_amount += 1
            print(first_name + " est un prénom avec un nombre de lettres supérieur à 7")
        else:
            print(first_name + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
    return long_names_amount

if __name__ == '__main__':
    prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
    print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(names(first_names=prenoms)))
    unittest.main()