class GameBrain:

    def __init__(self,description):

        self.description = description

        self.settings = {
            "vr":False,
            "multiplayer":False,
            "magic":False,
            "open_world":False
        }

        self.project_folder="generated_game"


class DesignInterpreter:

    def __init__(self,brain):
        self.brain=brain

    def analyze(self):

        text=self.brain.description.lower()

        if "vr" in text:
            self.brain.settings["vr"]=True

        if "multiplayer" in text:
            self.brain.settings["multiplayer"]=True

        if "magic" in text:
            self.brain.settings["magic"]=True

        if "open world" in text:
            self.brain.settings["open_world"]=True
