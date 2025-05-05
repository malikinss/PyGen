'''
TODO:
    Let's assume that we have a game.

    For each game session, the player gets a certain number of points
    depending on their result.

    Your task is to implement the HighScoreTable class - a high score table
    that can be updated based on the player's final results.

    The high score table is initially empty.

    The maximum number of records is specified when creating the table:
        high_score_table = HighScoreTable(3)

    The table should allow viewing current records and adding new results:
        print(high_score_table.scores) # []
        high_score_table.update(10)
        high_score_table.update(8)
        high_score_table.update(12)
        print(high_score_table.scores) # [12, 10, 8]

    Current records should always be in descending order.

    Since the table contains records, after filling the table, only those
    results that are better than the current ones should be added:
        high_score_table.update(6)
        high_score_table.update(7)
        print(high_score_table.scores) # [12, 10, 8]
        high_score_table.update(9)
        print(high_score_table.scores) # [12, 10, 9]

    The table should support resetting all results:
        high_score_table.reset()
        print(high_score_table.scores) # []
'''
from typing import List


class HighScoreTable:
    """
    Class to manage a high score table with limited entries.
    """
    def __init__(self, max_len: int) -> None:
        """
        Initialize table with maximum number of scores.

        Args:
            max_len: Maximum number of scores to store.
        """
        self.max_len = max_len
        self.scores: List[int] = []

    def update(self, score: int) -> None:
        """
        Add score if it ranks in top max_len scores.

        Args:
            score: Score to add.
        """
        new_scores = []
        new_scores.extend(self.scores)
        new_scores.append(score)
        # Sort in descending order and limit to max_len
        length = min(self.max_len, len(new_scores))
        self.scores[:] = sorted(new_scores, reverse=True)[:length]

    def reset(self) -> None:
        """
        Clear all scores in the table.
        """
        self.scores = []
