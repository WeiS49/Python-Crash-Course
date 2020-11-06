import unittest
from survey import AnonymousSurvey

class testSurvey(unittest.TestCase):

    def test_store_single_response(self):

        # 使用类中方法
        self.my_survey.store_response(self.responses[0])

        # 测试是否符合要求
        self.assertIn("English", self.my_survey.responses)


    
    def setUp(self):    # 这也是固定写法 初始化测试类的值
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "Mandarin"]

    def test_three_survey(self):

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == "__main__":
    unittest.main()