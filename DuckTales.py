import random
import time


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def final_fantasy():
    print('''\nНачалась буря.
Утка поняла, где она сейчас должны быть.
Бар был отложен на другой день.
Утка стояла на краю девятиэтажки очередного спального района и думала:\n
Этот город любит меня. Я видел его истинное лицо.
Улицы - продолжение свежепроложенных дорог - дорог, сделанных с душой...
И когда стройки будут окончательно завершены, \
все эти граждане начнут радоваться...
Когда скопившееся благоустройствао и удобства вспенятся им до пояса,
Все айтишники и зумеры посмотрят наверх и воскликнут:
"Спасибо", а я прошепчу: "на здоровье...".
Теперь весь мир стоит на краю, глядя вперед в светлое будущее, \
все эти ДСники, тимлиды, успешные люди...
И от чего-то, вдруг, никто не знает, что сказать.
Подо мной этот волшебный город. \
Он звучит, как бабочки в поле где-то под Ростовом.
А ночь отдает свежестью и озоном после дождя...''')


def rain():
    if random.random() >= 0.6:
        return True
    else:
        return False


def step2_umbrella():
    print('Утка взяла зонтик и направилась в бар.')
    time.sleep(2)

    if rain():
        print('На улице начался дождь 🌧️, и Утка воспользовалась зонтиком!')
        time.sleep(2)
        print(
            'В баре Утку встретил старый друг - бармен. \
Он знает, что ей нужно, он ей как брат.')
        time.sleep(2)
        return step3()
    else:
        print('На улице нет дождя. Утка, волоча зонтик за собой, \
добралась до бара.')
        time.sleep(2)
        return step3()


def step2_no_umbrella():
    print('Утка решила не брать зонтик и направилась в бар.')
    time.sleep(2)

    if rain():
        print('По дороге начался ливень 🌧️, и Утка промокла до нитки.')
        time.sleep(2)
        print('Придя в бар, Утка была мокрой и зябкой. \
Она рассказала бармену про свои неудачи.')
        time.sleep(2)
        print('Бармен понимающе кивнул и протяну полный стакан Утке.')
        time.sleep(2)
        return step3()
    else:
        print('На улице нет дождя. Утка знакомой дорогой добралась до бара.')
        time.sleep(2)
        return step3()


def step3():
    print('Что утка хочет сделать дальше?')
    options = {'подойти к официанту ': 'step4_waiter_at_my_favorite_bar',
               ' заказать бутылочку лимонада': 'step4_bottle_at_the_bottom'}
    choice = make_choice(options)
    return globals()[options[choice]]()


def make_choice(options):
    option = ''
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return option


def step4_waiter_at_my_favorite_bar():
    print('Утка спотыкается. Полный стакан летит, она падает за ним. \
Официант держит ее - спасибо. Снизу он так красив!')
    time.sleep(2)
    print('Жалко немного даже, что он на 7 лет младше.')
    time.sleep(2)
    return next_morning()


def step4_bottle_at_the_bottom():
    print('Утка обратилась к бармену.')
    time.sleep(2)
    print('Он ответил кратко: Осень кончилась, бери сразу две.')
    time.sleep(2)
    return final_fantasy()


def next_morning():
    print('На следущее утро Утка проснулась у себя дома. \
Что она сделает первым?')
    options = {'проверить сообщения ': 'end_check_messenger',
               ' позвонить друзьям': 'get_a_call'}
    choice = make_choice(options)
    return globals()[options[choice]]()


def end_check_messenger():
    print('Привет. Ну как ты?')
    time.sleep(2)
    return get_a_call()


def get_a_call():
    print('Звоню друзьям из пруда: Женюсь! \
На официанте в моем любимом баре...')


if __name__ == '__main__':
    step1()
