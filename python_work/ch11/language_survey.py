
from survey import AnonymousSurvey

# 创建实例
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)
my_survey.show_results()






