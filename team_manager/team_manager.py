from team import Team
from bench import Bench


def main():
    print("Welcome to the team manager.")
    # Here's where we create objects for the team and the bench. These
    # objects will be able to call the methods we've defined in their
    # respective classes. When the constructor functions are called here,
    # the classes' __init__() method is called with these values
    # passed to it. In both of these cases no arguments are passed, here.
    # However, the `self` argument is always implicitly passed with any
    # method call.
    the_team = Team()
    the_bench = Bench()

    while True:
        # Immediately converting the input to lower() lets the user enter
        # any kind of capitalization, so it's a little less strict.
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return  # this return statement exits main, ending the session.
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            # call a function that calls
            # the appropriate method on the team
            # object to cut the player (you need
            # to write the function below)
            do_cut_player(the_team, the_bench)
        elif command == "show bench":
            # call a function to call the necessary
            # bench method to show the names of the players
            # who are currently on the bench.
            do_show_bench(the_bench)
        else:
            do_not_understand()


def do_set_team_name(the_team):
    """set the team name"""
    name = input("What do you want to name the team?\n")
    while True:
        if all(x.isalpha() or x.isspace() for x in name):
            break
        else:
            name = input("What do you want to name the team?\n")
    the_team.set_team_name(name)


def do_show_team_roster(the_team):
    """display the roster"""
    if the_team.players == []:
        print("The lineup for", the_team.name, "has no players")
    else:
        the_team.show_roster()


def do_check_position_filled(the_team):
    """ 
    determines whether a given position has at least one player filling it,
    then print the appropriate message:
    "Yes, the", position, "position is filled"
    or "No, the", position, "position is not filled"
    """
    position = input("What position are you checking for?\n")
    list = ["catcher", "corner", "sniper", "thrower"]
    while True:
        if position in list:
            break
        else:
            position = input("What position are you checking for?\n")
    the_team.is_position_filled(position)


def do_add_player_to_team(the_team):
    """creates a new player and adds the player to the team"""
    # check if name is alphanumeric and space
    # check if number is numeric
    # check if position is one of the positions
    list = ["catcher", "corner", "sniper", "thrower"]
    player_name = input("What's the player's name?\n")
    while True:
        if all(x.isalpha() or x.isspace() for x in player_name):
            break
        else:
            player_name = input("What's the player's name?\n")
    player_number = input("What's " + player_name + "'s number?\n")
    while True:
        if player_number.isdigit():
            break
        else:
            player_number = input("What's " + player_name + "'s number?\n")
    player_position = input("What's " + player_name + "'s position?\n")
    while True:
        if player_position in list:
            break
        else:
            player_position = input("What's " + player_name + "'s position?\n")
    the_team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", the_team.name)


def do_send_player_to_bench(the_team, the_bench):
    """
    make sure that the player is actually on the team first,
    and then call a method on the bench object to place the player
    "on the bench". If this is accomplished successfully, print
    "Sent", name, "to bench." otherwise print
    name, "isn't on the team."
    """
    name = input("Who do you want to send to the bench?\n")
    while True:
        if name.isalnum():
            break
        else:
            name = input("Who do you want to send to the bench?\n")
    for player in the_team.players:
        if player.player_name == name:
            the_bench.send_to_bench(name)
            return
    print(name, "isn't on the team.")


def do_get_player_from_bench(the_bench):
    """get the best-rested player by name from the bench """
    the_bench.get_from_bench()


def do_cut_player(the_team, the_bench):
    """cut the player (also remove from the bench)"""
    name = input("Who do you want to cut?\n")
    while True:
        if all(x.isalpha() or x.isspace() for x in name):
            break
        else:
            name = input("Who do you want to cut?\n")
    for player in the_team.players:
        if player.player_name == name:
            the_team.cut_player(name)
            the_bench.cut_from_bench(name)
            return
    print("No such player in the team")


def do_show_bench(the_bench):
    """show the names of the players who are currently on the bench."""
    the_bench.bench_list()


def do_not_understand():
    """undefined situation"""
    print("I didn't understand that command")


main()
