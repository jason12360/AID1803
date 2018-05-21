import student_view 
from student_info_controller import *
import configuration


def main():
    config = configuration.Configuration('configuration.jc').get_config()
    view = student_view.StudnetView(config[view])
    view.show()
    
    # #import 
    # while True:
    #     show_menu()
    #     user_choice = input('请输入以上选项：')
    #     if user_choice == '1':
    #         input_student()
    #     elif user_choice == '2':
    #         output_student()
    #     elif user_choice == '3':
    #         remove_student()
    #     elif user_choice == '4':
    #         modify_student()
    #     elif user_choice == '5':
    #         sort_student(list_key='score', high2low=True)
    #     elif user_choice == '6':
    #         sort_student(list_key='score', high2low=False)
    #     elif user_choice == '7':
    #         sort_student(list_key='age', high2low=True)
    #     elif user_choice == '8':
    #         sort_student(list_key='age', high2low=False)
    #     elif user_choice == '9':
    #         save_students_list()
    #     elif user_choice == '10':
    #         load_student_list()
    #     elif user_choice == 'q':
    #         break
    #     else:
    #         print('您的输入有误，请重新输入。')


main()
