class CombatSystem:

    def __init__(self,brain):
        self.brain=brain

    def generate(self):

        print("Building combat system")


class MagicSystem:

    def __init__(self,brain):
        self.brain=brain

    def generate(self):

        if not self.brain.settings["magic"]:
            return

        print("Generating magic and power system")


class MultiplayerSystem:

    def __init__(self,brain):
        self.brain=brain

    def generate(self):

        print("Creating multiplayer networking")


class VRSystem:

    def __init__(self,brain):
        self.brain=brain

    def generate(self):

        print("Adding VR support")
