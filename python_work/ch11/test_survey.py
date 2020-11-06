
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def test_store_single_response(self):

        # 创建实例
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)

        # 使用类中方法
        my_survey.store_response("English")

        # 测试是否符合要求
        self.assertIn("English", my_survey.responses)

    def test_three_survey(self):    # 前面加 'test_' 是默认写法

        # 创建实例
        question = 'What is your favorite language?'
        my_survey = AnonymousSurvey(question)
        
        # 使用类中方法
        responses = ['English', 'Chinese', 'Jpanese']
        for response in responses:
            my_survey.store_response(response)
        
        # 测试是否符合要求
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == "__main__":
    unittest.main()


