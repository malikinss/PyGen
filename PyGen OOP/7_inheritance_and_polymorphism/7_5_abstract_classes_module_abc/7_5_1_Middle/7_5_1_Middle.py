'''
TODO:
    You have access to the Average, Median, and Harmonic classes, which have
    a similar interface.

    All three classes are used to process user ratings and critic ratings of
    some media content on a 100-point scale and calculate the average values
    of these ratings.

    The Average class is designed to find the arithmetic mean of user ratings
    or critic ratings, and the Median and Harmonic classes are designed
    to find the median and harmonic mean, respectively.

    Study the classes given, implement the abstract base class Middle,
    and build a correct inheritance scheme.

    When implementing, try to avoid duplicating code.

NOTE:
    The functionality of the Average, Median, and Harmonic classes should
    remain the same, you just need to combine them into a hierarchy by
    defining a single abstract base class Middle for them.
'''
from abc import ABC, abstractmethod
from typing import List, Union, Callable


class Middle(ABC):
    """
    Abstract base class for calculating average ratings from votes.

    Provides methods to filter user and expert votes and requires subclasses
    to implement average calculation.
    """

    def __init__(
        self,
        user_votes: List[Union[int, float]],
        expert_votes: List[Union[int, float]]
    ) -> None:
        """
        Initialize with user and expert votes.

        Args:
            user_votes: List of user ratings.
            expert_votes: List of critic ratings.
        """
        self.user_votes = user_votes
        self.expert_votes = expert_votes

    def _filter_votes(
        self,
        data: List[Union[int, float]],
        condition: Callable[[Union[int, float]], bool]
    ) -> List[Union[int, float]]:
        """
        Filter votes based on a condition.

        Args:
            data: List of votes to filter.
            condition: Function to check each vote.

        Returns:
            List of votes satisfying the condition.
        """
        return [vote for vote in data if condition(vote)]

    def get_correct_user_votes(self) -> List[Union[int, float]]:
        """
        Return filtered user votes between 10 and 90.

        Returns:
            List of valid user votes.
        """
        return self._filter_votes(self.user_votes, lambda x: 10 < x < 90)

    def get_correct_expert_votes(self) -> List[Union[int, float]]:
        """
        Return filtered expert votes between 5 and 95.

        Returns:
            List of valid expert votes.
        """
        return self._filter_votes(self.expert_votes, lambda x: 5 < x < 95)

    def _get_correct_votes(
        self, users: bool = True
    ) -> List[Union[int, float]]:
        """
        Return filtered user or expert votes based on users flag.

        Args:
            users: If True, return user votes; otherwise, expert votes.
                   Defaults to True.

        Returns:
            List of valid votes.
        """
        if users:
            return self.get_correct_user_votes()
        return self.get_correct_expert_votes()

    @abstractmethod
    def get_average(self, users: bool = True) -> float:
        """
        Calculate average of user or expert votes.

        Args:
            users: If True, use user votes; otherwise, use expert votes.
                   Defaults to True.

        Returns:
            Average value of the votes.
        """
        pass


class Average(Middle):
    """
    Class for calculating arithmetic mean of ratings.
    """

    def get_average(self, users: bool = True) -> float:
        """Return arithmetic mean of user or expert votes.

        Args:
            users: If True, use user votes; otherwise, use expert votes.
                   Defaults to True.

        Returns:
            Arithmetic mean of the votes or 0.0 if no valid votes.
        """
        votes = self._get_correct_votes(users)
        return sum(votes) / len(votes) if votes else 0.0


class Median(Middle):
    """
    Class for calculating median of ratings.
    """

    def get_average(self, users: bool = True) -> float:
        """
        Return median of user or expert votes.

        Args:
            users: If True, use user votes; otherwise, use expert votes.
                   Defaults to True.

        Returns:
            Median of the votes or 0.0 if no valid votes.
        """
        votes = sorted(self._get_correct_votes(users))
        return votes[len(votes) // 2] if votes else 0.0


class Harmonic(Middle):
    """
    Class for calculating harmonic mean of ratings.
    """

    def get_average(self, users: bool = True) -> float:
        """
        Return harmonic mean of user or expert votes.

        Args:
            users: If True, use user votes; otherwise, use expert votes.
                   Defaults to True.

        Returns:
            Harmonic mean of the votes or 0.0 if no valid votes.
        """
        votes = self._get_correct_votes(users)
        return len(votes) / sum(1 / vote for vote in votes) if votes else 0.0
