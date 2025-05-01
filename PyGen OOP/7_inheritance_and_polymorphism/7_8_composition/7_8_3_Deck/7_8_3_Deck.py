'''
TODO:
    Implement a Card class that describes a playing card.

    When instantiated, the class must accept two arguments in the following
    order:
        suit — the suit of the playing card, represented by one of
               the following symbols:
            ♣, ♢, ♡, ♠
        rank — the rank of the playing card, represented by one of
               the following symbols or pairs of symbols:
            2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

    An instance of the Card class must have the following informal string
    representation:
        <playing card suit><playing card rank>

    Also implement a Deck data class that describes a classic deck of
    52 playing cards.

    The cards in the deck must be arranged first in ascending suit order,
    and then in ascending rank order.

    When instantiated, the class must not accept any arguments.

    The Deck class must have two instance methods:
        shuffle() — a method that shuffles all the cards in the deck.
                    The deck can only be shuffled if the deck currently
                    contains all 52 cards.
                    If the deck contains fewer than 52 cards, a ValueError
                    exception must be raised with the text:
            You can only shuffle a full deck
        deal() — a method that removes the last card from the deck and returns
                 it.
                 If the deck is empty, a ValueError exception should be raised
                 with the text:
            All cards have been played

    An instance of the Deck class should have the following informal string
    representation:
        Cards in the deck: <current number of cards in the deck>

NOTE:
    The order of seniority of card ranks from lowest to highest:
        2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

    The order of seniority of card suits from lowest to highest:
        ♣, ♢, ♡, ♠

    No additional data validation is required.

    It is guaranteed that the implemented classes are used only with correct
    data.

    There are no restrictions regarding the implementation of classes,
    they can be arbitrary.
'''
import random


class Card:
    """
    Playing card.
    """

    def __init__(self, suit: str, rank: str) -> None:
        """
        Init card.

        Args:
            suit: Card suit (♣, ♢, ♡, ♠).
            rank: Card rank (2-10, J, Q, K, A).
        """
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        """
        Get string representation.

        Returns:
            str: Format <suit><rank>.
        """
        return f"{self.suit}{self.rank}"


class Deck:
    """
    Deck of 52 playing cards.
    """

    _SUITS = "♣♢♡♠"
    _RANKS = (*map(str, range(2, 11)), "J", "Q", "K", "A")

    def __init__(self) -> None:
        """
        Init full deck.
        """
        self._deck = [Card(s, r) for s in self._SUITS for r in self._RANKS]

    def shuffle(self) -> None:
        """
        Shuffle full deck.

        Raises:
            ValueError: If deck is not full.
        """
        if len(self._deck) != 52:
            raise ValueError("You can only shuffle a full deck")
        random.shuffle(self._deck)

    def deal(self) -> Card:
        """
        Deal last card.

        Returns:
            Card: Last card in deck.

        Raises:
            ValueError: If deck is empty.
        """
        if not self._deck:
            raise ValueError("All cards have been played")
        return self._deck.pop()

    def __str__(self) -> str:
        """
        Get string representation.

        Returns:
            str: Format 'Cards in the deck: <number>'.
        """
        return f"Cards in the deck: {len(self._deck)}"
