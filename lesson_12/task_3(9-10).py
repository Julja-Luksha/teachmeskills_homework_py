# Задание 9. Класс «Музыкальный плейлист»
# Цель: много методов для управления коллекцией и сортировки.
# Описание:
# Создай класс Playlist.
# Требования:
# 1. Атрибуты: название плейлиста, список треков (название, исполнитель, длительность в секундах).
# 2. Методы:
# o add_track(name, artist, duration) — добавить трек.
# o remove_track(name) — удалить трек.
# o total_duration() — общая длительность всех треков.
# o find_by_artist(artist) — найти все треки исполнителя.
# o longest_track() — найти самый длинный трек.
# o shortest_track() — найти самый короткий трек.
# o shuffle() — перемешать треки в случайном порядке.
# o sort_by_duration(reverse=False) — сортировать треки по длительности.
import random
from typing import Optional


class MusicPlaylist:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tracks = []

    def add_track(self, name: str, artist: str, duration: int) -> None:
        track = {
            "name": name,
            "artist": artist,
            "duration": duration
        }
        self.tracks.append(track)
        print("Трек успешно добавлен")

    def remove_track(self, name: str) -> None:
        for track in self.tracks:
            if track["name"] == name:
                self.tracks.remove(track)
                print("Трек был удален")

    def total_duration(self) -> int:
        print("Длительность плейлиста, с:")
        duration = 0
        for track in self.tracks:
            duration += track["duration"]
        return duration

    def find_by_artist(self, artist: str) -> list:
        print(f"Треки {artist}:")
        return [track for track in self.tracks if track["artist"] == artist]

    def longest_track(self) -> str:
        print("Самый длинный трек:")
        return max(self.tracks, key=lambda x: x["duration"])

    def shortest_track(self) -> str:
        print("Самый короткий трек:")
        return min(self.tracks, key=lambda x: x["duration"])

    def sort_by_duration(self) -> list:
        print("Сортировка по длительности, с:")
        return sorted(self.tracks, key=lambda x: x["duration"], reverse=True)

    def shuffle(self) -> None:
        print("Песни были перемешаны")
        random.shuffle(self.tracks)


pl = MusicPlaylist("Мой плейлист")
print(pl.name)
pl.add_track("song1", "artist1", 350)
pl.add_track("song2", "artist2", 392)
pl.add_track("song3", "artist3", 415)

print(pl.total_duration())
pl.remove_track("song1")
print(pl.total_duration())
print(pl.find_by_artist("artist1"))
print(pl.find_by_artist("artist2"))
print(pl.longest_track())
print(pl.shortest_track())
pl.shuffle()
print(pl.tracks)
print(pl.sort_by_duration())


# Задание 10. Класс «Учебная группа»
# Цель: объединение нескольких объектов в один класс-менеджер.
# Описание:
# Создай класс Student и класс StudyGroup.
# Student:
# • Атрибуты: имя, оценки (список чисел).
# • Методы:
# o add_grade(grade) — добавить оценку.
# o average_grade() — вернуть среднюю оценку.
# o info() — вывести информацию об ученике.
# StudyGroup:
# • Атрибуты: название группы, список студентов.
# • Методы:
# o add_student(student) — добавить ученика.
# o remove_student(name) — удалить ученика по имени.
# o find_best_student() — найти ученика с лучшей средней оценкой.
# o group_average() — средняя оценка по группе.
# o list_students() — вывести список всех студентов.


class Student:
    def __init__(self, name: str) -> None:
        self.name = name
        self.grades = []

    def add_grade(self, grade: int) -> None:
        self.grades.append(grade)

    def average_grade(self) -> Optional[float]:
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def info(self) -> str:
        avg = self.average_grade()
        if avg is None:
            return f"Имя студента: {self.name}, другие данные отсутствуют"
        return f"Оценки студента {self.name}: {self.grades}, средний балл: {avg}"


st1 = Student("Алексей")
st2 = Student("Анна")
st3 = Student("Кирилл")
print(st1.info())
st1.add_grade(5)
st1.add_grade(6)
st1.add_grade(7)
st1.add_grade(8)
st2.add_grade(9)
print(st1.average_grade())


class StudyGroup:
    def __init__(self, name: str) -> None:
        self.name = name
        self.students = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)
        print(f"Студент {student.name} успешно добавлен в группу")

    def remove_student(self, name: str) -> None:
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Студент {name} удален из группы")
                return

    def find_best_student(self) -> Optional[str]:
        students_with_grades = [s for s in self.students if s.average_grade() is not None]
        if not students_with_grades:
            return "Нет списка оценок ни у одного студента"
        best = max(students_with_grades, key=lambda s: s.average_grade())
        return f"Высший средний балл имеет {best.name}: {best.average_grade()}"

    def group_average(self) -> Optional[float]:
        grades = [s.average_grade() for s in self.students if s.average_grade() is not None]
        if not grades:
            print("Нет данных для оценки")
            return None
        print("Средняя оценка по группе:")
        return sum(grades) / len(grades)

    def list_students(self) -> list:
        print("Список учеников группы:")
        return [s.name for s in self.students]


sg = StudyGroup("A")
sg.add_student(st1)
sg.add_student(st2)
sg.add_student(st3)
print(sg.find_best_student())
print(sg.list_students())
print(sg.group_average())
