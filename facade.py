class Projector:
    def on(self):
        print("Проектор включен.")

    def off(self):
        print("Проектор выключен.")

    def set_input(self, input_source):
        print(f"Вход установлен на: {input_source}")


# Класс для Звуковой системы
class SoundSystem:
    def on(self):
        print("Звуковая система включена.")

    def off(self):
        print("Звуковая система выключена.")

    def set_volume(self, level):
        print(f"Уровень громкости установлен на: {level}")


# Класс для DVD-проигрывателя
class DVDPlayer:
    def on(self):
        print("DVD-проигрыватель включен.")

    def off(self):
        print("DVD-проигрыватель выключен.")

    def play(self, movie):
        print(f"Воспроизведение фильма: {movie}")


class HomeTheaterFacade:
    def __init__(self, projector, sound_system, dvd_player):
        self.projector = projector
        self.sound_system = sound_system
        self.dvd_player = dvd_player

    def watch_movie(self, movie):
        print("Подготовка к просмотру фильма...")
        self.projector.on()
        self.projector.set_input("DVD")
        self.sound_system.on()
        self.sound_system.set_volume(5)
        self.dvd_player.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("Завершение просмотра фильма...")
        self.dvd_player.off()
        self.sound_system.off()
        self.projector.off()


if __name__ == "__main__":
    projector = Projector()
    sound_system = SoundSystem()
    dvd_player = DVDPlayer()

    home_theater = HomeTheaterFacade(projector, sound_system, dvd_player)

    home_theater.watch_movie("Inception")
    home_theater.end_movie()
