import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.api_key)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        # animal = request.form["animal"]
        age1 =request.form["age1"]
        age2 =request.form["age2"]
        prof1 =request.form["prof1"]
        prof2 =request.form["prof2"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(age1,age2,prof1,prof2),
            temperature=0.6,
            max_tokens=256,
            n=1
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    print(result)
    return render_template("index.html", result=result)


def generate_prompt(age1,age2,prof1,prof2):
    return """Write vows for a marriage
Age of first partner: {}
Age of second partner: {}
Profession of first partner :{}
Profession of second partner :{}
Names:""".format(
        age1.capitalize(),
        age2.capitalize(),
        prof1.capitalize(),prof2.capitalize()
    )
