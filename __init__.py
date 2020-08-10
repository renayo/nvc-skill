from mycroft import MycroftSkill, intent_file_handler


class Nvc(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nvc.intent')
    def handle_nvc(self, message):
        self.speak_dialog('nvc')


def create_skill():
    return Nvc()

