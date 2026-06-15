import random


class ProbabilitySystem:

    def __init__(self):

        self.weather_probabilities = {

            "Clear": 0.6,
            "Windy": 0.3,
            "Heavy Rain": 0.1

        }

    def weather_prediction(self):

        weather = random.choices(

            population=list(
                self.weather_probabilities.keys()
            ),

            weights=list(
                self.weather_probabilities.values()
            ),

            k=1

        )[0]

        return weather

    def weather_score(self, weather):

        if weather == "Clear":

            return 100

        elif weather == "Windy":

            return 70

        else:

            return 30

    def bayesian_weather_risk(self, weather):

        if weather == "Clear":

            return (
                "Low Risk",
                0.60
            )

        elif weather == "Windy":

            return (
                "Medium Risk",
                0.30
            )

        else:

            return (
                "High Risk",
                0.10
            )