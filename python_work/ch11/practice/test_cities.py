import unittest
from cities_function_t import get_formatted_city

class testCityCase(unittest.TestCase):
    
    def test_city_country(self):    # 函数无法执行是Error 运行未达到预期是Faliure
        formatted_info = get_formatted_city('new york', 'america')
        self.assertEqual(formatted_info, 'New York America')

    def test_city_country_population(self):
        formatted_info = get_formatted_city('peking', 'china', '4000')
        self.assertEqual(formatted_info, 'Peking China - 4000')

if __name__ == "__main__":
    unittest.main()
