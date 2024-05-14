from datetime import datetime, timedelta


def timedelta_to_str(t: timedelta):
    """
    Convert timedelta to str.
    :param t: timedelta to convert
    :return: string
    """
    if isinstance(t, datetime):
        return t.strftime('%M:%S')
    else:
        total_seconds = int(t.total_seconds())
        minutes, seconds = divmod(total_seconds, 60)
        return f'{minutes:02}:{seconds:02}'


class Track:
    """
    This class represents a Track unit.
    """
    def __init__(
            self,
            title: str,
            duration: str,
            artist: list,
            release_year: int
    ):
        """
        Initialize track.

        :param title: Name of the track.
        :param duration: Duration of the track.
        :param artist: An artist of the track.
        :param release_year: Release year of the track.
        """
        self.__title = title
        self.__duration_str = duration
        m, s = duration.split(':')
        self.__duration = timedelta(minutes=int(m), seconds=int(s))
        self.__artist = artist
        self.__release_year = release_year
        self.__start_time = None
        self.__paused_time = None
        self.__playingStatus = 'Стоп'

    @property
    def title(self) -> str:
        """
        :return: Title of the track.
        """
        return self.__title

    @property
    def duration(self) -> str:
        """
        :return: Duration of the track.
        """
        return str(self.__duration)

    @property
    def artist(self) -> list:
        """
        :return: An artists of the track.
        """
        return self.__artist

    @property
    def release_year(self) -> int:
        """
        :return: Release year of the track.
        """
        return self.__release_year

    @property
    def isPlaying(self) -> str:
        """
        :return: Status of playing of the track.
        """
        return self.__playingStatus

    def play(self) -> None:
        """
        Start playing of the track.
        :return: None
        """
        if self.__playingStatus == 'Стоп':
            self.__playingStatus = 'Воспроизводится'
            self.__start_time = datetime.now()
            print(f'Воспроизводится: {self.__title}')
        elif self.__playingStatus == 'Пауза':
            self.__playingStatus = 'Воспроизводится'
            self.__start_time = datetime.now() - self.__paused_time
            print(f'Воспроизводится: {self.__title}')

    def pause(self) -> None:
        """
        Pause playing of the track.
        :return: None
        """
        if self.__playingStatus == 'Воспроизводится':
            self.__playingStatus = 'Пауза'
            if self.__start_time - datetime.now() < self.__duration:
                self.__paused_time = datetime.now() - self.__start_time
                self.__start_time = None
            else:
                self.__start_time = None
                self.__paused_time = None
            print(f'Пауза: {self.__title}')

    def stop(self) -> None:
        """
        Stop playing of the track.
        :return: None
        """
        if self.__playingStatus:
            self.__playingStatus = False
            self.__start_time = None
            self.__paused_time = None
            print(f'Остановлен: {self.__title}')

    def __str__(self):
        return f'{", ".join(self.__artist)} -- {self.__title}'

    def __repr__(self):
        if self.__playingStatus == 'Воспроизводится':
            if self.__start_time - datetime.now() < self.__duration:
                self.stop()
                tm = '0:00'
            else:
                playing_time = datetime.now() - self.__start_time
                tm = timedelta_to_str(playing_time)
        elif self.__playingStatus == 'Пауза':
            tm = timedelta_to_str(self.__paused_time)
        else:
            tm = '0:00'

        return (f'Название: {self.__title}\n'
                f'Исполнитель: {', '.join(self.__artist)}\n'
                f'Длительность: {self.__duration_str}\n'
                f'Год выпуска: {self.__release_year}\n'
                f'Статус воспроизведения: {self.__playingStatus}\n'
                f'Время воспроизведения: {tm}')


class Album:
    """
    This class represents a Album unit.
    """
    def __init__(
            self,
            title: str,
            release_year: int,
            artist: str,
            tracks: list
    ):
        """
        Initialize album class.
        :param title: Title of the class.
        :param release_year: Release year of the album.
        :param artist: An artist of the album.
        :param tracks: List of tracks of the album.
        """
        self.__title = title
        self.__release_year = release_year
        self.__artist = artist
        self.__tracks = tracks

    @property
    def tracks(self) -> list:
        """
        :return: List of tracks.
        """
        return self.__tracks

    def __str__(self):
        return f'{self.__artist} -- {self.__title}, {self.__release_year}'

    def __repr__(self):
        res = (f'Название: {self.__title}\n'
               f'Год выпуска: {self.__release_year}\n'
               f'Исполнитель: {self.__artist}\n'
               f'Список треков:\n')

        for track in self.__tracks:
            res += (f'[{self.__tracks.index(track)}] - {track}\n')
        return res
