class SettingsManager(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.theme = 'Dark'
            cls.__instance.language = 'en'
            cls.__instance.config = '/config/SettingsManager'
        return cls.__instance

    def set_theme(self, theme):
        self.theme = theme

    def get_theme(self):
        return self.theme

    def set_language(self, language):
        self.language = language

    def get_language(self):
        return self.language

    def set_config_path(self, config):
        self.config = config

    def get_config_path(self):
        return self.config


a = SettingsManager()
b = SettingsManager()
a.set_theme('Light')
a.set_language('ru')
print(b.get_theme())
print(b.get_language())
print(a is b)
