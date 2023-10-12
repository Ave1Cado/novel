import random

# Определение персонажей и событий
class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Player(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.inventory = []

class NonPlayerCharacter(Character):
    def __init__(self, name, description):
        super().__init__(name, description)

class Event:
    def __init__(self, description, dialogue=None):
        self.description = description
        self.dialogue = dialogue

class Dialogue:
    def __init__(self, character, text):
        self.character = character
        self.text = text

# Создание персонажей и событий
player = Player("Олег", "Молодой хакер")
vasilisa = NonPlayerCharacter("Василиса", "Талантливая разработчица игр")
dimdimich = NonPlayerCharacter("Димдиымч", "Эксперт по кибербезопасности")
andryxa = NonPlayerCharacter("Андрюха", "Лидер клуба 'Кибермир'")

dialogue1 = Dialogue(vasilisa, "Привет, Олег! Рада видеть тебя снова.")
dialogue2 = Dialogue(andryxa, "Мы должны спасти 'Кибермир'! Это наш дом.")
event1 = Event("Олег возвращается в город и узнает о кризисе 'Кибермира'.", dialogue1)
event2 = Event("Олег знакомится с Василисой, Димдимычем и Андрюхой.", dialogue2)
event3 = Event("С Олегом и его друзьями начинают происходить странные события в клубе.")

# Определение игрового цикла
def game_loop():
    events = [event1, event2, event3]
    player_location = 0

    while player_location < len(events):
        current_event = events[player_location]
        print(current_event.description)

        if current_event.dialogue:
            print(f"{current_event.dialogue.character.name}: {current_event.dialogue.text}")

        input("Нажмите Enter для продолжения...")
        player_location += 1

# Запуск игрового цикла
if __name__ == "__main__":
    game_loop()
# Создание дополнительных персонажей и событий
dmitriy = NonPlayerCharacter("Дмитрий", "Старший разработчик")
tanya = NonPlayerCharacter("Таня", "Кибер-активистка")
event4 = Event("Олег обращается к Дмитрий за помощью в восстановлении клуба.", Dialogue(dmitriy, "Я помогу восстановить 'Кибермир'."))
event5 = Event("Таня предлагает Олегу искать поддержку у кибер-активистов.", Dialogue(tanya, "Мы готовы поддержать вас в этой борьбе."))

# Дополнительные события и диалоги можно добавить по мере необходимости.

# Определение игрового цикла
def game_loop():
    events = [event1, event2, event3, event4, event5] # Добавьте остальные события по мере продвижения сюжета
    player_location = 0

    while player_location < len(events):
        current_event = events[player_location]
        print(current_event.description)

        if current_event.dialogue:
            print(f"{current_event.dialogue.character.name}: {current_event.dialogue.text}")

        input("Нажмите Enter для продолжения...")
        player_location += 1

# Запуск игрового цикла
if __name__ == "__main__":
    game_loop()
# Создание дополнительных персонажей и событий
event6 = Event("Дмитрий предлагает провести собрание клуба для обсуждения будущего.", Dialogue(dmitriy, "Давайте соберем всех и расскажем им о наших планах."))
event7 = Event("Таня предлагает организовать сбор средств для клуба.", Dialogue(tanya, "Мы можем собрать деньги и восстановить 'Кибермир'!"))

# Дополнительные события и диалоги можно добавить по мере необходимости.

# Определение игрового цикла
def game_loop():
    events = [event1, event2, event3, event4, event5, event6, event7] # Добавьте остальные события по мере продвижения сюжета
    player_location = 0

    while player_location < len(events):
        current_event = events[player_location]
        print(current_event.description)

        if current_event.dialogue:
            print(f"{current_event.dialogue.character.name}: {current_event.dialogue.text}")

        input("Нажмите Enter для продолжения...")
        player_location += 1

# Запуск игрового цикла
if __name__ == "__main__":
    game_loop()
# Создание дополнительных персонажей и событий
event8 = Event("Собрание клуба проходит успешно, и участники поддерживают идею восстановления клуба.")
event9 = Event("Команда начинает организацию мероприятия для сбора средств.")
event10 = Event("Олег и его друзья работают в ночи, готовясь к мероприятию.")
event11 = Event("Мероприятие проводится успешно, и 'Кибермир' получает дополнительные средства.")
event12 = Event("Димдимыч обнаруживает новые следы хакеров и предупреждает об угрозе.")

# Дополнительные события и диалоги можно добавить по мере необходимости.

# Определение игрового цикла
def game_loop():
    events = [event1, event2, event3, event4, event5, event6, event7, event8, event9, event10, event11, event12] # Добавьте остальные события по мере продвижения сюжета
    player_location = 0

    while player_location < len(events):
        current_event = events[player_location]
        print(current_event.description)

        if current_event.dialogue:
            print(f"{current_event.dialogue.character.name}: {current_event.dialogue.text}")

        input("Нажмите Enter для продолжения...")
        player_location += 1

# Запуск игрового цикла
if __name__ == "__main__":
    game_loop()
# Создание дополнительных персонажей и событий
event13 = Event("Таня предлагает создать команду для разоблачения хакеров.", Dialogue(tanya, "Давайте найдем этих хакеров и прекратим их действия."))
event14 = Event("Олег и его команда начинают исследование следов и попытки выявления хакеров.")
event15 = Event("Олег находит ключевой след, который может привести к хакерам.")
event16 = Event("Друзья собираются для обсуждения следов и планов действий.")
event17 = Event("А Адрюха расказывает Олегу о своем прошлом, связанном с клубом 'Кибермир'.")
event18 = Event("Раскол внутри команды угрожает их успеху в поисках хакеров.")
event19 = Event("После долгих усилий, Олегу и его друзья раскрывают истинного врага.")
event20 = Event("Судьба 'Кибермира' зависит от решений игроков и их команды.")

# Дополнительные события и диалоги можно добавить по мере необходимости.

# Определение игрового цикла
def game_loop():
    events = [event1, event2, event3, event4, event5, event6, event7, event8, event9, event10, event11, event12, event13, event14, event15, event16, event17, event18, event19, event20]
    player_location = 0

    while player_location < len(events):
        current_event = events[player_location]
        print(current_event.description)

        if current_event.dialogue:
            print(f"{current_event.dialogue.character.name}: {current_event.dialogue.text}")

        input("Нажмите Enter для продолжения...")
        player_location += 1

# Запуск игрового цикла
if __name__ == "__main__":
    game_loop()
# Создание дополнительных персонажей и событий
event21 = Event("Олег и его команда разрабатывают план по поимке хакеров.")
event22 = Event("Поиск хакеров приводит к серии захватывающих событий и обнаружений.")
event23 = Event("Олег обнаруживает масштаб атак хакеров и глубоко личные мотивы.")
event24 = Event("Решение Олега и его команды приводит к заключительной конфронтации.")
event25 = Event("Судьба 'Кибермира' решается в последней битве с хакерами.")

# Дополнительные события и диалоги можно добавить по мере необходимости.

# Определение игрового цикла
def game_loop():
    events = [event1, event2, event3, event4, event5, event6, event7, event8, event9, event10, event11, event12, event13, event14, event15, event16, event17, event18, event19, event20, event21, event22, event23, event24, event25]
    player_location = 0

    while player_location < len(events):
        current_event = events[player_location]
        print(current_event.description)

        if current_event.dialogue:
            print(f"{current_event.dialogue.character.name}: {current_event.dialogue.text}")

        input("Нажмите Enter для продолжения...")
        player_location += 1

# Запуск игрового цикла
if __name__ == "__main__":
    game_loop()
# Создание дополнительных персонажей и событий
event26 = Event("Олегу и хакеры вступают в заключительную битву.")
event27 = Event("Битва достигает своего пика, и решение игроков имеет большое значение.")
event28 = Event("Судьба клуба 'Кибермир' зависит от исхода битвы.")
event29 = Event("В зависимости от решений игроков, клуб 'Кибермир' возрождается или погибает.")
event30 = Event("Завершение игры и развитие истории в соответствии с решениями игроков.")

# Дополнительные события и диалоги можно добавить по мере необходимости.

# Определение игрового цикла
def game_loop():
    events = [event1, event2, event3, event4, event5, event6, event7, event8, event9, event10, event11, event12, event13, event14, event15, event16, event17, event18, event19, event20, event21, event22, event23, event24, event25, event26, event27, event28, event29, event30]
    player_location = 0

    while player_location < len(events):
        current_event = events[player_location]
        print(current_event.description)

        if current_event.dialogue:
            print(f"{current_event.dialogue.character.name}: {current_event.dialogue.text}")

        input("Нажмите Enter для продолжения...")
        player_location += 1

# Запуск игрового цикла
if __name__ == "__main__":
    game_loop()
# Создание дополнительных персонажей и событий
event31 = Event("После финальной битвы, клуб 'Кибермир' возрождается с новыми силами.")
event32 = Event("Олег и его команда становятся героями клуба и города.")
event33 = Event("Таня предлагает провести кибер-мероприятие в честь победы.")
event34 = Event("Димдимыч продолжает укреплять кибербезопасность клуба.")
event35 = Event("Андрюха рассказывает историю клуба и его будущие планы.")
event36 = Event("Игроки видят результаты своих решений и их влияние на клуб и персонажей.")
event37 = Event("Завершение игры с завершающими словами и возможностью переиграть.")

# Дополнительные события и диалоги можно добавить по мере необходимости.

# Определение игрового цикла
def game_loop():
    events = [event1, event2, event3, event4, event5, event6, event7, event8, event9, event10, event11, event12, event13, event14, event15, event16, event17, event18, event19, event20, event21, event22, event23, event24, event25, event26, event27, event28, event29, event30, event31, event32, event33, event34, event35, event36, event37]
    player_location = 0

    while player_location < len(events):
        current_event = events[player_location]
        print(current_event.description)

        if current_event.dialogue:
            print(f"{current_event.dialogue.character.name}: {current_event.dialogue.text}")

        input("Нажмите Enter для продолжения...")
        player_location += 1

# Запуск игрового цикла
if __name__ == "__main__":
    game_loop()
# Создание завершающих событий
event38 = Event("Клуб 'Кибермир' проводит кибер-мероприятие, собирая множество участников.")
event39 = Event("Андрюха выступает с памятным словом о значении солидарности и сообщества.")
event40 = Event("Олег и его команда ощущают гордость за восстановление клуба и общности.")
event41 = Event("Игроки видят конечные результаты своих действий и их влияние на историю.")

# Дополнительные события и диалоги можно добавить по мере необходимости.

# Определение игрового цикла
def game_loop():
    events = [event1, event2, event3, event4, event5, event6, event7, event8, event9, event10, event11, event12, event13, event14, event15, event16, event17, event18, event19, event20, event21, event22, event23, event24, event25, event26, event27, event28, event29, event30, event31, event32, event33, event34, event35, event36, event37, event38, event39, event40, event41]
    player_location = 0

    while player_location < len(events):
        current_event = events[player_location]
        print(current_event.description)

        if current_event.dialogue:
            print(f"{current_event.dialogue.character.name}: {current_event.dialogue.text}")

        input("Нажмите Enter для продолжения...")
        player_location += 1

# Завершение игры и развитие истории
def finish_game():
    print("Поздравляю! Вы завершили игру 'Кибермир' и спасли клуб от хакеров.")
    print("Спасибо за вашу роль в восстановлении клуба и создании легенды.")
    input("Нажмите Enter для завершения...")

# Запуск игрового цикла и завершение игры
if __name__ == "__main__":
    game_loop()
    finish_game()