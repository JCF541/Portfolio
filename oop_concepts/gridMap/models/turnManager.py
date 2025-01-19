import heapq

class TurnManager:
    def __init__(self):
        self.priority_queue = []

    def add_unit(self, unit):
        """Add a unit to the turn queue."""
        heapq.heappush(self.priority_queue, (-unit.speed, unit))

    def next_turn(self):
        """Pop the next unit based on the highest speed."""
        if self.priority_queue:
            _, unit = heapq.heappop(self.priority_queue)
            return unit
        return None
