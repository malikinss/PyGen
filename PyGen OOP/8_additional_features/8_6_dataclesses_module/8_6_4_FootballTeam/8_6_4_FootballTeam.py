'''
TODO:
    Implement a FootballPlayer data class that describes a football player.

    When instantiating the class, it must accept three arguments in
    the following order:
        name — the player's name (type str)
        surname — the player's surname (type str)
        value — the player's market value in euros (type int)

    An instance of the FootballPlayer class must have three attributes:
        name — the player's name
        surname — the player's surname
        value — the player's market value in euros

    Also, an instance of the FootballPlayer class must have the following
    formal string representation:
    FootballPlayer(
        name='<player's name>', surname='<player's surname>'
    )

    Finally, instances of the FootballPlayer class must support all comparison
    operations between themselves using the operators ==, !=, >, <, >=, <=.

    Two football players are considered equal if their market values match.

    A football player is considered greater than another football player if
    his market value is greater.

    Implement a FootballTeam data class that describes a football team.

    When instantiated, the class must accept one argument:
        name — the name of the team (type str)

    An instance of the FootballTeam class must have two attributes:
        name — the name of the team (type str)
        players — an initially empty list containing the players of the team
                  (type list)

    The FootballTeam class must have one instance method:
        add_players() — a method that accepts an arbitrary number of
        positional arguments, each representing a football player, and adds
        them to the team

    Also, an instance of the FootballTeam class must have the following formal
    string representation:
    FootballTeam(name='<name of the football team>')

    Finally, instances of the FootballTeam class must support comparison
    operations between themselves using the == and != operators.

    Two football teams are considered equal if their names are the same.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented classes are used only with correct
    data.

    There are no restrictions regarding class implementations, they can be
    arbitrary.
'''
from dataclasses import dataclass, field
from typing import List


@dataclass(order=True)
class FootballPlayer:
    """
    A data class for a football player with name, surname, and market value.
    """
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


@dataclass
class FootballTeam:
    """
    A data class for a football team with name and list of players.
    """
    name: str
    players: List['FootballPlayer'] = field(
        default_factory=list,  # Initialize empty list for players
        init=False,
        repr=False,
        compare=False
    )

    def add_players(self, *args: 'FootballPlayer') -> None:
        """
        Add players to the team.

        Args:
            *args: FootballPlayer instances to add.
        """
        self.players.extend(args)
