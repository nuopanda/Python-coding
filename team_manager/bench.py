from collections import deque


class Bench:
    """A class representing a sidelines bench"""

    def __init__(self):
        """Initialize the bench object"""
        self.bench_queue = deque()

    def send_to_bench(self, player_name):
        """Put the player "onto the bench" """
        if player_name in self.bench_queue:
            print(player_name, "is already at bench.")
        else:
            self.bench_queue.append(player_name)
            print("Sent", player_name, "to bench")

    def get_from_bench(self):
        """
        Return the name of the player who has
        been on the bench longest.
        """
        if self.bench_queue:
            print("Got",self.bench_queue[0],"from bench")
            self.bench_queue.popleft()
        else:
            print("The bench is empty.")

    def cut_from_bench(self, name):
        """
        if a player has been removed from the team,
        the bench list should also remove the player
        """
        self.bench_tem = deque()
        while self.bench_queue:
            name_tem = self.bench_queue.popleft()
            if name_tem != name:
                self.bench_tem.append(name_tem)
        self.bench_queue = self.bench_tem

    def bench_list(self):
        """
        display the current list of players on the bench
        """
        if self.bench_queue:
            for player in list(self.bench_queue):
                print(player, end=" ")
                print()
        else:
            print("the bench is empty.")
