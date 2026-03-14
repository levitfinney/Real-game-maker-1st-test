from flask import Flask, render_template, request

from ai.core_ai import GameBrain, DesignInterpreter
from ai.generation_systems import WorldGenerator, AssetGenerator
from ai.gameplay_systems import CombatSystem, MagicSystem, MultiplayerSystem, VRSystem
from ai.deployment_systems import PlaytestAI, BalanceAI, SaveSystem

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    logs=""

    if request.method=="POST":

        description=request.form["description"]

        brain = GameBrain(description)

        DesignInterpreter(brain).analyze()

        WorldGenerator(brain).generate()
        AssetGenerator(brain).generate()

        CombatSystem(brain).generate()
        MagicSystem(brain).generate()

        if brain.settings["multiplayer"]:
            MultiplayerSystem(brain).generate()

        if brain.settings["vr"]:
            VRSystem(brain).generate()

        PlaytestAI(brain).run()
        BalanceAI(brain).run()

        folder,zipfile = SaveSystem(brain).save()

        logs=f"Game generated! Saved at {folder}"

    return render_template("index.html",logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
