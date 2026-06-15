class ConstraintSystem:

    def __init__(self):

        self.no_fly_zones = [
            "Airport"
        ]

        self.max_battery_usage = 30

    def validate_route(self, path, total_distance):

        for location in path:

            if location in self.no_fly_zones:

                return False, (
                    f"Constraint Failed: "
                    f"{location} is Restricted"
                )

        if total_distance > self.max_battery_usage:

            return False, (
                "Constraint Failed: "
                "Battery Limit Exceeded"
            )

        return True, "All Constraints Satisfied"