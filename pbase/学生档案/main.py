from configuration import Configuration

class Main():
    def __init__(self,config):
        self.config = config
        self.model= self.config.get_class('model')
        self.view = self.config.get_class('view')(self.model)
        
        self.controller = self.config.get_class('controller')(self.model,self.view)
    def run(self):
        while True:
            self.view.show_menu()
            user_choice = input('请输入以上选项：')
            if user_choice == '1':
                self.controller.add_student()
            elif user_choice == '2':
                self.controller.list_student()
            elif user_choice == '3':
                self.controller.remove_student()
            elif user_choice == '4':
                self.controller.modify_student()
            elif user_choice == '5':
                self.controller.sort_student(list_key='score', high2low=True)
            elif user_choice == '6':
                self.controller.sort_student(list_key='score', high2low=False)
            elif user_choice == '7':
                self.controller.sort_student(list_key='age', high2low=True)
            elif user_choice == '8':
                self.controller.sort_student(list_key='age', high2low=False)
            elif user_choice == '9':
                self.controller.save_students_list()
            elif user_choice == '10':
                self.controller.load_student_list()
            elif user_choice == 'q':
                break
            else:
                print('您的输入有误，请重新输入。')    


m = Main(Configuration('configuration.jc'))
m.run()
