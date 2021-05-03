# flask app
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from temperature import Temperature
from calorie import Calorie

app = Flask(__name__)


class CaloriePage(MethodView):
    def get(self):
        calorie_form = CalorieForm()
        return render_template("calorie_form.html",
                               calorie_form=calorie_form)

    def post(self):
        calorie_form = CalorieForm(request.form)

        temperature = Temperature(country=calorie_form.country.data,
                                  city=calorie_form.city.data)

        calories = Calorie(weight=calorie_form.weight.data,
                           height=calorie_form.height.data,
                           age=calorie_form.age.data,
                           temperature=temperature.get())

        return render_template("calorie_form.html",
                               result=True,
                               calorie_form=calorie_form,
                               weight=calories.weight,
                               height=calories.height,
                               age=calories.age,
                               temperature=calories.temperature,
                               tkcal=round(calories.calculate()))


class CalorieForm(Form):
    weight = StringField("Weight:", default=150)
    height = StringField("Height:", default=68)
    age = StringField("Age:", default=29)
    city = StringField("City:", default="Worcester")
    country = StringField("Country:", default="usa")

    button = SubmitField("Calculate")


app.add_url_rule("/",
                 view_func=CaloriePage.as_view("calorie_form.html"))


app.run(debug=True)
