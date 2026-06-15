from dataclasses import dataclass
import random


@dataclass
class DroneState:
    location: str
    battery: int


class HyderabadEnvironment:

    def __init__(self):

        # =========================
        # HYDERABAD LOCATIONS
        # =========================

        self.locations = {

            1: "Hitech City",
            2: "Madhapur",
            3: "Gachibowli",
            4: "Begumpet",
            5: "Secunderabad",
            6: "LB Nagar",
            7: "Uppal",
            8: "Kukatpally",
            9: "Banjara Hills",
            10: "Shamshabad",
            11: "Ameerpet",
            12: "Mehdipatnam",
            13: "Jubilee Hills",
            14: "Kondapur",
            15: "Miyapur",
            16: "Charminar",
            17: "Dilsukhnagar",
            18: "Tolichowki",
            19: "Manikonda",
            20: "Nampally"
        }

        # =========================
        # CITY GRAPH CONNECTIONS
        # =========================

        self.city_map = {

            "Hitech City": {

                "Madhapur": 5,
                "Gachibowli": 7,
                "Kondapur": 4,
                "Ameerpet": 8

            },

            "Madhapur": {

                "Hitech City": 5,
                "Kukatpally": 6,
                "Ameerpet": 8

            },

            "Gachibowli": {

                "Hitech City": 7,
                "Shamshabad": 15,
                "Manikonda": 5

            },

            "Begumpet": {

                "Secunderabad": 4,
                "Ameerpet": 3

            },

            "Secunderabad": {

                "Begumpet": 4,
                "Uppal": 7

            },

            "LB Nagar": {

                "Dilsukhnagar": 4

            },

            "Kukatpally": {

                "Madhapur": 6,
                "Miyapur": 5

            },

            "Banjara Hills": {

                "Jubilee Hills": 3

            },

            "Ameerpet": {

                "Begumpet": 3,
                "Hitech City": 8,
                "Madhapur": 8,
                "Nampally": 8

            },

            "Mehdipatnam": {

                "Tolichowki": 4,
                "Nampally": 6

            },

            "Manikonda": {

                "Gachibowli": 5,
                "Tolichowki": 6

            },

            "Charminar": {

                "Nampally": 5

            },

            "Dilsukhnagar": {

                "LB Nagar": 4

            },

            "Tolichowki": {

                "Manikonda": 6,
                "Mehdipatnam": 4

            },

            "Miyapur": {

                "Kukatpally": 5

            },

            "Jubilee Hills": {

                "Banjara Hills": 3

            },

            "Kondapur": {

                "Hitech City": 4

            },

            "Nampally": {

                "Ameerpet": 8,
                "Charminar": 5,
                "Mehdipatnam": 6

            },

            "Shamshabad": {

                "Gachibowli": 15

            },

            "Uppal": {

                "Secunderabad": 7

            }

        }

        # =========================
        # NO FLY ZONES
        # =========================

        self.no_fly_zones = [

            "Shamshabad"

        ]

    # =========================
    # TRAFFIC SYSTEM
    # =========================

    def get_traffic(self):

        traffic_levels = {

            "Low": 2,
            "Medium": 5,
            "High": 10

        }

        traffic = random.choice(
            list(traffic_levels.keys())
        )

        return traffic, traffic_levels[traffic]

    # =========================
    # DISPLAY LOCATIONS
    # =========================

    def display_locations(self):

        print(
            "\n===== AVAILABLE HYDERABAD LOCATIONS =====\n"
        )

        for number, place in self.locations.items():

            print(f"{number}. {place}")

    # =========================
    # VALIDATE LOCATION
    # =========================

    def validate_location(self, user_input):

        user_input = user_input.strip()

        # NUMBER INPUT

        if user_input.isdigit():

            number = int(user_input)

            if number in self.locations:

                return self.locations[number]

        # TEXT INPUT

        else:

            for place in self.locations.values():

                if (
                    place.lower()
                    ==
                    user_input.lower()
                ):

                    return place

        return None