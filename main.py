from environment import HyderabadEnvironment
from search_algorithms import SearchAlgorithms
from csp import ConstraintSystem
from probabilistic import ProbabilitySystem
from decision_logic import DecisionSystem

print("\n===== AVAILABLE HYDERABAD LOCATIONS =====\n")

env = HyderabadEnvironment()

search = SearchAlgorithms()

csp = ConstraintSystem()

probability = ProbabilitySystem()

decision = DecisionSystem()


print("Available Locations:\n")

for location in env.city_map.keys():
    print("-", location)



# SOURCE INPUT

while True:

    source_input = input(
        "\nEnter Source "
        "(Number or Name): "
    ).strip()

    if source_input == "":
        print("Source cannot be empty.")
        continue

    start = None

    # NUMBER INPUT

    if source_input.isdigit():

        source_number = int(source_input)

        if source_number in env.locations:
            start = env.locations[source_number]

    else:

        # TEXT INPUT

        for place in env.locations.values():

            if place.lower() == source_input.lower():

                start = place
                break

    if start is None:

        print("Invalid source location.")
        continue

    break


# DESTINATION INPUT

while True:

    dest_input = input(
        "Enter Destination "
        "(Number or Name): "
    ).strip()

    if dest_input == "":
        print("Destination cannot be empty.")
        continue

    goal = None

    if dest_input.isdigit():

        dest_number = int(dest_input)

        if dest_number in env.locations:
            goal = env.locations[dest_number]

    else:

        for place in env.locations.values():

            if place.lower() == dest_input.lower():

                goal = place
                break

    if goal is None:

        print("Invalid destination.")
        continue

    if goal == start:

        print(
            "Source and Destination "
            "cannot be same."
        )

        continue

    break


# BATTERY VALIDATION

while True:

    battery_input = input("Enter Battery Percentage (1-100): ").strip()

    if battery_input == "":
        print("Battery value required.")
        continue

    if not battery_input.isdigit():
        print("Enter numeric battery value.")
        continue

    battery = int(battery_input)

    if battery <= 0 or battery > 100:
        print("Battery must be between 1 and 100.")
        continue

    break

packages = {

    1: ("Medicine", 1, 5),
    2: ("Electronics", 1, 10),
    3: ("Food", 1, 7),
    4: ("Clothes", 1, 12),
    5: ("Books", 1, 8)

}


print("\n===== AVAILABLE PACKAGE TYPES =====\n")

for number, details in packages.items():

    print(f"{number}. {details[0]}")


while True:

    package_input = input(
        "\nEnter Package "
        "(Number or Name): "
    ).strip()

    if package_input == "":

        print("Package cannot be empty.")
        continue

    package_type = None

    # NUMBER INPUT

    if package_input.isdigit():

        number = int(package_input)

        if number in packages:

            package_type = packages[number][0]

            min_weight = packages[number][1]

            max_weight = packages[number][2]

    else:

        # TEXT INPUT

        for details in packages.values():

            if details[0].lower() == package_input.lower():

                package_type = details[0]

                min_weight = details[1]

                max_weight = details[2]

                break

    if package_type is None:

        print("Invalid package type.")
        continue

    break


print(
    f"\nAllowed Weight for "
    f"{package_type}: "
    f"{min_weight}kg to {max_weight}kg"
)


while True:

    weight_input = input(
        "Enter Package Weight (kg): "
    ).strip()

    if weight_input == "":

        print("Weight cannot be empty.")
        continue

    if not weight_input.isdigit():

        print("Enter numeric value.")
        continue

    package_weight = int(weight_input)

    if (
        package_weight < min_weight
        or
        package_weight > max_weight
    ):

        print(
            f"Weight must be between "
            f"{min_weight}kg and "
            f"{max_weight}kg"
        )

        continue

    break


# WEATHER PREDICTION

weather = probability.weather_prediction()

weather_score = probability.weather_score(
    weather
)

print("\nWeather Condition:", weather)


# TRAFFIC ANALYSIS

traffic_name, traffic_penalty = env.get_traffic()

print("Traffic Level:", traffic_name)


# ROUTE GENERATION

path = search.astar(
    env.city_map,
    start,
    goal
)

print("\nGenerated Route:")

print(path)

# CALCULATE TOTAL DISTANCE FROM ROUTE

total_distance = 0
for i in range(len(path) - 1):
    current = path[i]
    next_node = path[i + 1]
    total_distance += env.city_map[current][next_node]

print(f"\nTotal Distance: {total_distance} KM")


# =========================
# DELIVERY TIME CALCULATION
# =========================

# Drone speed assumptions

if traffic_name == "Low":

    drone_speed = 60

elif traffic_name == "Medium":

    drone_speed = 40

else:

    drone_speed = 25


# TIME = DISTANCE / SPEED

estimated_time = (
    total_distance / drone_speed
) * 60


print(
    f"Estimated Delivery Time: "
    f"{estimated_time:.2f} Minutes"
)


# CONSTRAINT CHECKING

valid, message = csp.validate_route(
    path,
    total_distance
)

print("\nConstraint Status:")

print(message)


# UTILITY CALCULATION

utility_score = decision.utility_function(
    total_distance,
    weather_score,
    traffic_penalty,
    battery
)

print("\nFinal Utility Score:")

print(utility_score)


# FINAL DECISION

result = decision.evaluate_delivery(
    utility_score
)

print("\n===== FINAL DECISION =====")

print(result)


# EXPLAINABLE AI TRACE

print("\n===== AI REASONING TRACE =====")

print("1. User inputs validated")

print("2. Environment loaded")

print("3. Weather predicted dynamically")

print("4. Traffic analyzed")

print("5. A* search generated route")

print("6. CSP checked constraints")

print("7. Utility function evaluated route")

print("8. Final intelligent decision generated")