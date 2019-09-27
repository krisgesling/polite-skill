from mycroft import MycroftSkill, intent_file_handler


class Polite(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('polite.intent')
    def handle_polite(self, message):
        self.speak_dialog('polite')


def create_skill():
    return Polite()

