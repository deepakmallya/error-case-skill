from mycroft import MycroftSkill, intent_file_handler


class ErrorCase(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('case.error.intent')
    def handle_case_error(self, message):
        self.speak_dialog('case.error')


def create_skill():
    return ErrorCase()

