from mycroft import MycroftSkill, intent_file_handler


class Polite(MycroftSkill):
    def __init__(self):
        super().__init__()
        # Keep track of how many impolite utterances have been made.
        # This is only to change dialog later in the Skill.
        self.impolite_count = 0

    def initialize(self):
        """ Call make_active each time the wakeword is heard.
            converse() can only trigger if a Skill is active. """
        self.add_event("recognizer_loop:wakeword", self.make_active)

    def converse(self, utterances, lang=None):
        """ The converse method is able to inspect utterances before
            they are passed to the normal intent handling service. """
        self.log.debug("Impolite utterance detected")
        utt = utterances[0]
        # Check if utt contains any words in vocab/lang-code/RudeWords.voc
        if self.voc_match(utt, "RudeWords"):
            self.impolite_count += 1
            self.log.debug("counter: " + str(self.impolite_count))
            # Speak different dialog based on the state of this Skill
            if self.impolite_count < 3:
                self.speak_dialog("not.polite")
            else:
                self.speak_dialog("you.have.detention")
            # return True to tell Mycroft that we have handled the utterance
            return True
        else:
            # If no RudeWord found, return False to pass this utterance on
            # to the normal intent handling process.
            return False


def create_skill():
    return Polite()
