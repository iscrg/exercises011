class Teacher:
    """
    This class represents a Teacher unit.

    teachers - list of all teachers.
    """
    teachers = []

    def __init__(
            self,
            last_name: str,
            first_name: str,
            patronymic: str,
    ):
        """
        Initialize teacher.
        :param last_name: Last name of the teacher.
        :param first_name: First name of the teacher.
        :param patronymic: Patronymic of the teacher.
        """
        self.__last_name = last_name
        self.__first_name = first_name
        self.__patronymic = patronymic
        self.__lessons = []

    @property
    def last_name(self) -> str:
        """
        :return: Last name of the teacher.
        """
        return self.__last_name

    @property
    def first_name(self) -> str:
        """
        :return: First name of the teacher.
        """
        return self.__first_name

    @property
    def patronymic(self) -> str:
        """
        :return: Patronymic of the teacher.
        """
        return self.__patronymic

    @property
    def lessons(self) -> list:
        """
        :return: List of the teacher's lessons
        """
        return self.__lessons

    def add_lesson(self, lesson) -> None:
        """
        Add lesson to the teacher.
        :param lesson: Current lesson.
        :return: None
        """
        self.__lessons.append(lesson)

    def __repr__(self):
        return f'{self.__last_name} {self.__first_name} {self.__patronymic}'


class Group:
    """
    This class represents a Group unit.

    groups - list of all groups.
    """
    groups = []

    def __init__(
            self,
            title: str,
    ):
        """
        Initialize of group class.
        :param title: Title of the group.
        """
        self.__title = title
        self.__lessons = []

    @property
    def title(self) -> str:
        """
        :return: Title of the group.
        """
        return self.__title

    @property
    def lessons(self) -> list:
        """
        :return: List of lessons of the group.
        """
        return self.__lessons

    def add_lesson(self, lesson):
        """
        Add lesson to the group.
        :param lesson: Lesson to add
        :return: None
        """
        self.__lessons.append(lesson)

    def __repr__(self):
        return self.__title


class Lesson:
    """
    This class represents a Lesson unit.
    """
    lessons = []

    def __init__(
            self,
            group: Group,
            day_of_week: str,
            title: str,
            auditorium: str,
            start_time: str,
            end_time: str,
            teacher: Teacher
    ):
        """
        Initialize lesson class.
        :param group: Group which have the lesson.
        :param day_of_week: Day of week of the lesson.
        :param title: Title of the lesson.
        :param auditorium: Auditorium of the lesson.
        :param start_time: Time when the lesson starts.
        :param end_time: Time when the lesson ends.
        :param teacher: Teacher of the lesson.
        """
        self.__group = group
        self.__day_of_week = day_of_week
        self.__title = title
        self.__auditorium = auditorium
        self.__start_time = start_time
        self.__end_time = end_time
        self.__teacher = teacher

    @property
    def group(self):
        """
        :return: Group which have the lesson.
        """
        return self.__group

    @property
    def day_of_week(self):
        """
        :return: Day of week of the lesson.
        """
        return self.__day_of_week

    @property
    def title(self):
        """
        :return: Title of the lesson.
        """
        return self.__title

    @property
    def auditorium(self):
        """
        :return: Auditorium of the lesson.
        """
        return self.__auditorium

    @property
    def start_time(self):
        """
        :return: Time when the lesson starts.
        """
        return self.__start_time

    @property
    def end_time(self):
        """
        :return: Time when the lesson ends.
        """
        return self.__end_time

    @property
    def teacher(self):
        """
        :return: Teacher of the lesson.
        """
        return self.__teacher

    def __repr__(self):
        return self.__title


class Loader:
    """
    Class loads data to the classes.
    """
    @staticmethod
    def load(filename):
        """
        Load data to the classes.
        :param filename: The file with data.
        :return: None
        """
        with open(filename, encoding='UTF-8') as f:
            f.readline()
            for line in f.readlines():
                line = line.rstrip('\n')
                group, day_of_week, lesson, auditorium, start_time, \
                    end_time, last_name, first_name, patronymic = line.split(';')

                if f'{last_name} {first_name} {patronymic}' not in map(str, Teacher.teachers):
                    Teacher.teachers.append(Teacher(last_name, first_name, patronymic))

                if group not in map(str, Group.groups):
                    Group.groups.append(Group(group))

                for teacher in Teacher.teachers:
                    if str(teacher) == f'{last_name} {first_name} {patronymic}':
                        l_teacher = teacher
                        break

                for g_group in Group.groups:
                    if str(g_group) == group:
                        l_group = g_group
                        break

                class_lesson = Lesson(
                    group=l_group,
                    day_of_week=day_of_week,
                    title=lesson,
                    auditorium=auditorium,
                    start_time=start_time,
                    end_time=end_time,
                    teacher=l_teacher
                )

                Lesson.lessons = class_lesson
                for g_group in Group.groups:
                    if str(g_group) == group:
                        g_group.add_lesson(class_lesson)
                for teacher in Teacher.teachers:
                    if str(teacher) == f'{last_name} {first_name} {patronymic}':
                        teacher.add_lesson(class_lesson)

        Group.groups.sort()
        Teacher.teachers = sorted(Teacher.teachers, key=lambda obj: repr(obj))
