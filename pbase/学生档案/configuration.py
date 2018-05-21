class Configuration:
    def __init__(self, src):
        self.load_config(src)

    def load_config(self, src):
        with open(src) as file_obj:
            config_list = file_obj.readlines()
            for config in config_list:
                _ = config.split(':')
                config_key = _[0]
                config_value = _[1].rstrip()
                self.__dict__[config_key] = config_value


    def get_class(self,class_type):

        m = __import__(self.__dict__[class_type])
        return getattr(m,self.__dict__[class_type])
  

    def get_database(self):
        return self.database
