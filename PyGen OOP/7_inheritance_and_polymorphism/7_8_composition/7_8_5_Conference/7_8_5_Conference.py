'''
TODO:
    Implement a Lecture class that describes a talk.

    When instantiated, the class must accept three arguments in the following
    order:
        topic — the topic of the talk
        start_time — the start time of the talk as a string in HH:MM format
        duration — the duration of the talk as a string in HH:MM format

    Also implement a Conference class that describes a conference that lasts
    one day.

    A conference is a set of consecutive talks.

    When instantiated, the class must not accept any arguments.

    The Conference class must have four instance methods:
        add() — a method that takes a talk as an argument and adds it to
                the conference.
                If the talk overlaps with other talks, a ValueError exception
                should be raised with the text:
                    It is impossible to hold a talk at this time
        total() — method returning the total duration of all talks in
                  the conference as a string in HH:MM format
        longest_lecture() — method returning the duration of the longest talk
                            in the conference as a string in HH:MM format
        longest_break() — method returning the duration of the longest break
                          between talks in the conference as a string in HH:MM
                          format

NOTE:
    The break between talks can be zero.

    In other words, one talk can end, for example, at 12:00, and another start
    at 12:00.

    Additional data validation is not required.

    It is guaranteed that the implemented classes are used only with correct
    data.

    There are no restrictions regarding class implementations, they can be
    arbitrary.
'''
from datetime import datetime, timedelta


class Lecture:
    """
    Lecture with topic and timing.
    """

    def __init__(
        self, topic: str, start_time: str, duration: str
    ) -> None:
        """
        Init lecture.

        Args:
            topic: Lecture topic.
            start_time: Start time (HH:MM).
            duration: Duration (HH:MM).
        """
        self.topic = topic
        self.start = datetime.strptime(start_time, "%H:%M")
        h, m = map(int, duration.split(":"))
        self.duration = timedelta(hours=h, minutes=m)
        self.end = self.start + self.duration


class Conference:
    """
    One-day conference of lectures.
    """

    def __init__(self) -> None:
        """
        Init empty conference.
        """
        self.lectures = []

    def add(self, lecture: Lecture) -> None:
        """
        Add lecture if no overlap.

        Args:
            lecture: Lecture to add.

        Raises:
            ValueError: If lecture overlaps.
        """
        for existing in self.lectures:
            if existing.start < lecture.end and lecture.start < existing.end:
                raise ValueError(
                    "It is impossible to hold a talk at this time"
                )
        self.lectures.append(lecture)

    @staticmethod
    def _format_time(minutes: float) -> str:
        """
        Format minutes to HH:MM.

        Args:
            minutes: Total minutes.

        Returns:
            str: Time in HH:MM format.
        """
        return f"{int(minutes // 60):02}:{int(minutes % 60):02}"

    def total(self) -> str:
        """
        Get total duration.

        Returns:
            str: Total duration (HH:MM).
        """
        total = sum((lec.duration for lec in self.lectures), timedelta())
        minutes = total.total_seconds() // 60
        return self._format_time(minutes)

    def longest_lecture(self) -> str:
        """
        Get longest lecture duration.

        Returns:
            str: Longest duration (HH:MM).
        """
        if not self.lectures:
            return "00:00"
        max_dur = max(lec.duration for lec in self.lectures)
        minutes = max_dur.total_seconds() // 60
        return self._format_time(minutes)

    def longest_break(self) -> str:
        """
        Get longest break duration.

        Returns:
            str: Longest break (HH:MM).
        """
        if len(self.lectures) < 2:
            return "00:00"
        sorted_lecs = sorted(self.lectures, key=lambda x: x.start)
        max_break = timedelta()
        for i in range(len(sorted_lecs) - 1):
            break_dur = sorted_lecs[i + 1].start - sorted_lecs[i].end
            max_break = max(max_break, break_dur)
        minutes = max_break.total_seconds() // 60
        return self._format_time(minutes)
