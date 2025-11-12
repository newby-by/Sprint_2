"""The third task.

Using a static method in a class.
"""

RATE_0_5 = 0.5

points = 0

class PointsForPlace:

    @staticmethod
    def get_points_for_place(place: int) -> int:
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return points
        if place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return points
        
        points = 101 - place
        return points


class PointsForMeters:

    @staticmethod
    def get_points_for_meters(meters: int) -> int:
        if meters < 0:
            print('Количество метров не может быть отрицательным')
            return points
                
        points = meters * RATE_0_5
        return points


class TotalPoints(PointsForPlace, PointsForMeters):
    total = 0

    def get_total_points(self, meters, place):
        self.total = (super().get_points_for_place(place) +
                             super().get_points_for_meters(meters))
        return self.total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
