from solution4 import Loader, Teacher, Group, Lesson


def day_of_week_filter(day_of_week):
    def filter_func(obj):
        return obj.day_of_week == day_of_week
    return filter_func


DAYS_OF_WEEK = [
    'Понедельник',
    'Вторник',
    'Среда',
    'Четверг',
    'Пятница',
    'Суббота',
    'Воскресенье'
]


Loader.load('schedule.txt')

while True:
    print(
        '[0] - Расписание групп\n'
        '[1] - Расписание преподавателей'
    )
    choice = int(input('Выберите действие: '))
    print()

    if choice == 0:
        print('Список групп:')
        for group in Group.groups:
            print(f'[{Group.groups.index(group)}] - {group}')
        print(f'[{len(Group.groups)}] - Выход')
        print()

        choice = int(input('Выберите пункт: '))
        if choice != len(Group.groups):
            for day_of_week in DAYS_OF_WEEK:
                print(f"{'-'*10}{day_of_week}{'-'*10}")
                lessons_a_day = filter(day_of_week_filter(day_of_week), Group.groups[choice].lessons)
                for lesson in lessons_a_day:
                    print(f'{lesson.title}\n'
                          f'{lesson.auditorium}\n'
                          f'{lesson.start_time}-{lesson.end_time}\n'
                          f'{lesson.teacher}\n')
            print()
        else:
            print()
            continue

    else:
        print('Список преподавателей:')
        for teacher in Teacher.teachers:
            print(f'[{Teacher.teachers.index(teacher)}] - {teacher}')
        print(f'[{len(Teacher.teachers)}] - Выход')
        print()

        choice = int(input('Выберите пункт: '))
        if choice != len(Teacher.teachers):
            for day_of_week in DAYS_OF_WEEK:
                print(f"{'-'*10}{day_of_week}{'-'*10}")
                lessons_a_day = filter(day_of_week_filter(day_of_week), Teacher.teachers[choice].lessons)
                for lesson in lessons_a_day:
                    print(f'{lesson.title}\n'
                          f'{lesson.group}\n'
                          f'{lesson.auditorium}\n'
                          f'{lesson.start_time}-{lesson.end_time}\n')
            print()
        else:
            print()
            continue
