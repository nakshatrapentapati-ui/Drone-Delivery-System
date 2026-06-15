class DecisionSystem:

    def utility_function(
        self,
        distance,
        weather_score,
        traffic_penalty,
        battery
    ):

        utility = (
            battery
            + weather_score
            - distance
            - traffic_penalty
        )

        return utility


    def evaluate_delivery(
        self,
        utility_score
    ):

        if utility_score >= 100:
            return "Delivery Approved"

        return "Delivery Rejected"