from player import Player


class Team:
    """A class representing a dodgeball team"""
    # All methods in Python include arguments representing the object
    # itself. In the method definition, this is represented by the
    # `self` parameter.

    def __init__(self):
        """Initialize the Team object"""
        self.name = "Anonymous Team"
        self.players = []
        self.position = {
            "catcher": 0,
            "corner": 0,
            "sniper": 0,
            "thrower": 0
        }

    # Another example of self. The method call only passes one argument,
    # the 'name; value. But the method definition must always include the
    # self parameter.
    def set_team_name(self, name):
        """set the team name"""
        self.name = name

    # Note again that `self` is the first parameter.
    def add_player(self, player_name, player_number, player_position):
        """
        call the Player class constructor with the appropriate
        values to create a new player object, then add that
        player object to the team's players list.
        """
        self.player = Player(player_name,player_number, player_position)
        self.players.append(self.player)
        self.position[self.player.player_position] += 1

    def cut_player(self, player_name):
        """Remove the player with the name player_name from the players list."""
        for self.player in self.players:
            if self.player.player_name==player_name:
                self.players.remove(self.player)
        self.position[self.player.player_position] -= 1


    def is_position_filled(self, position):
        """
        checks whethers there is currently at least one player on the team
        occupying the requested position
        """
        if self.position[position] > 0:
            print("Yes, the", position, "is filled")
        else:
            print("No, the", position, "is not filled")

    # TODO: Write any necessary methods to support the methods
    # above, and write the method that will 
    def show_roster(self):
        """
        display (print to screen)
        the full team roster in the following format:

        The lineup for Seattle Scorpions is:
        15       Garcia          catcher
        55       Wiggins         corner
        99       McCann          sniper 
        """
        for self.player in self.players:
            print(self.player.player_number,"\t",self.player.player_name,"\t",self.player.player_position)