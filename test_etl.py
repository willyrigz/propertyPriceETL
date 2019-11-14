import unittest
from etl import PropertyData

class TestPropertyData(unittest.TestCase):

    def setUp(self):
        self.data1 = PropertyData('Apartment 12, 1st floor, Parnell street, Dublin 1. Dublin,')
        self.data2 = PropertyData('10 Cove Walk Avenue, Kinsale Manor, Kinsale')
        self.data3 = PropertyData('183 DOORADOYLE PARK, DOORADOYLE ROAD, LIMERICK')
        self.data4 = PropertyData('APARTMENT, THE 19TH COURT, GOREY')
        self.data5 = PropertyData('Lï¿½NA NA HEAGLAISE, DAMHLIAG, CONTAE NA Mï¿½')


    def tearDown(self):
        pass

    def test_transformText(self):

        self.assertEqual(self.data1.transformText().all() , 'apartment 12 first floor parnell street dublin 1')
        self.assertEqual(self.data2.transformText().all() , '10 cove walk avenue kinsale manor')
        self.assertEqual(self.data3.transformText().all() , '183 dooradoyle park dooradoyle road limerick')
        self.assertEqual(self.data4.transformText().all() , 'apartment nineteenth court gorey')
        self.assertEqual(self.data5.transformText().all() , 'lna na heaglaise damhliag contae na m')

if __name__ == '__main__':
    unittest.main()
