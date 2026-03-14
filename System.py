import os

class WorldGenerator:

    def __init__(self,brain):
        self.brain=brain

    def generate(self):

        print("Generating terrain")

        os.makedirs(self.brain.project_folder,exist_ok=True)


class AssetGenerator:

    def __init__(self,brain):
        self.brain=brain

    def generate(self):

        print("Generating models, textures, and animations")
