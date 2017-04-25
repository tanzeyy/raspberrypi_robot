#!/usr/bin/env python

import pyttsx


class Voice(object):
    def __init__(self):
        self.speaker = pyttsx.init()

    def speak(self, words_to_say):
        self.speaker.say("I'm gonna" + words_to_say)
        self.speaker.runAndWait()


if __name__ == '__main__':
    voice = Voice()
    obj_name = raw_input("Obj_name:")
    voice.speak('place '+obj_name)
