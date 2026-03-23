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