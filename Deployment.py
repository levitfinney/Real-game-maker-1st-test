import os
import zipfile
import datetime


class PlaytestAI:

    def __init__(self,brain):
        self.brain=brain

    def run(self):

        print("Running AI playtests")


class BalanceAI:

    def __init__(self,brain):
        self.brain=brain

    def run(self):

        print("Balancing gameplay")


class SaveSystem:

    def __init__(self,brain):
        self.brain=brain

    def save(self):

        timestamp=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        folder=f"archives/game_{timestamp}"

        os.makedirs(folder,exist_ok=True)

        zipfile_path=folder+".zip"

        with zipfile.ZipFile(zipfile_path,"w") as zipf:
            pass

        return folder,zipfile_path
