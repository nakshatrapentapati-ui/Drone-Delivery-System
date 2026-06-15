import heapq


class SearchAlgorithms:

    def heuristic(self, current, goal):

        heuristic_values = {

            "Hitech City": 10,
            "Madhapur": 9,
            "Gachibowli": 8,
            "Begumpet": 7,
            "Secunderabad": 6,
            "LB Nagar": 5,
            "Uppal": 0,
            "Kukatpally": 8,
            "Banjara Hills": 7,
            "Shamshabad": 10,
            "Ameerpet": 6,
            "Mehdipatnam": 5,
            "Jubilee Hills": 6,
            "Kondapur": 8,
            "Miyapur": 9,
            "Charminar": 4,
            "Dilsukhnagar": 3,
            "Tolichowki": 5,
            "Manikonda": 7,
            "Nampally": 4

        }

        return heuristic_values.get(current, 0)

    def astar(self, graph, start, goal):

        open_set = []

        heapq.heappush(
            open_set,
            (0, start)
        )

        came_from = {}

        g_score = {
            start: 0
        }

        while open_set:

            current = heapq.heappop(
                open_set
            )[1]

            if current == goal:

                path = []

                while current:

                    path.append(current)

                    current = came_from.get(
                        current
                    )

                path.reverse()

                return path

            for neighbor, distance in graph[current].items():

                tentative_g = (
                    g_score[current]
                    + distance
                )

                if (
                    neighbor not in g_score
                    or tentative_g < g_score[neighbor]
                ):

                    came_from[neighbor] = current

                    g_score[neighbor] = tentative_g

                    f_score = (
                        tentative_g
                        + self.heuristic(
                            neighbor,
                            goal
                        )
                    )

                    heapq.heappush(
                        open_set,
                        (f_score, neighbor)
                    )

        return [start]