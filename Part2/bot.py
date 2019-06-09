import vk_api
import random
import time
import json

token = "токен группы"


vk = vk_api.VkApi(token=token)
vk._auth_token()

#file = open("data.txt" , "r")
#data = json.load(file)


#print(dz)
#file.close()

dz = "Пусто. Для нового дз введите: обновить дз <задача>"

#def save():
#    saves = []
#    saves.append(dz)
#    file = open("data.txt" , "w")
#    json.dump(saves, file)
#    file.close()


def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }
keyboard = {
    "one_time": False,
    "buttons": [
    [get_button(label="привет", color="primary"),get_button(label="дз", color="positive")],
    [get_button(label="Автор", color="default")]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

#У кнопок может быть один из 4 цветов:
#1. primary — синяя кнопка, обозначает основное действие. #5181B8
#2. default — обычная белая кнопка. #FFFFFF
#3. negative — опасное действие, или отрицательное действие (отклонить, удалить и тд). #E64646
#4. positive — согласиться, подтвердить. #4BB34B

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "кто я?":
                vk.method("messages.send", {"peer_id": id, "message": "ты хороший человек", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "дз":
                vk.method("messages.send", {"peer_id": id, "message": str(dz), "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "кнопки":
                vk.method("messages.send", {"peer_id": id, "keyboard": keyboard,"message": "вот и они", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "что ты умеешь?" or body.lower() == "что умеешь?":
                vk.method("messages.send", {"peer_id": id, "message": "храню дз и отвечаю на некоторые вопросы", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "на какие?" or body.lower() == "на какие":
                vk.method("messages.send", {"peer_id": id, "message": "на некоторые", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "ты тупой":
                vk.method("messages.send", {"peer_id": id, "message": "я не тупой, просто неопытный =)", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "автор":
                vk.method("messages.send", {"peer_id": id, "message": "Руленко Никита Романович, студент группы П-41", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "что поставить руленко?" or body.lower() == "что ставить руленко?" or body.lower() == "что поставить руленко" or body.lower() == "что ставить руленко":
                vk.method("messages.send", {"peer_id": id, "message": "Да тройки ему точно хватит =) Скока можно уже в техе 10 лет торчит, пусть забирает диплом и валит уже.", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "1":
                vk.method("messages.send", {"peer_id": id, "message": "ну 1 и?", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "123":
                vk.method("messages.send", {"peer_id": id, "message": "это тест? окей, 123", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "расскажи анекдот":
                vk.method("messages.send", {"peer_id": id, "message": "так я ж чат-бот, а не тамада =)", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "погода на завтра":
                vk.method("messages.send", {"peer_id": id, "message": "понятия не имею, я ж не погодный бот", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "что нового?":
                vk.method("messages.send", {"peer_id": id, "message": "да особо ничего. сижу тут в группе, жду когда руленко сдаст диплом.", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "как дела?":
                vk.method("messages.send", {"peer_id": id, "message": "ну так. в группе пустовато.", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "какие планы?":
                vk.method("messages.send", {"peer_id": id, "message": "да я чат-бот, какие у меня могут быть планы?", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "возможности":
                vk.method("messages.send", {"peer_id": id, "message": "да какие в этой стране возможности?", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "помощь":
                vk.method("messages.send", {"peer_id": id, "message": "мне бы тоже не помешала)", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "выход":
                vk.method("messages.send", {"peer_id": id, "message": "а выхода нет)", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "завершить":
                vk.method("messages.send", {"peer_id": id, "message": "ничего нельзя завершить. жизнь это бесконечный процесс!)", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "функции":
                vk.method("messages.send", {"peer_id": id, "message": "мои чтоль? да вот, сижу тут, отвечаю)", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "пока":
                vk.method("messages.send", {"peer_id": id, "message": "ну пока. приходи еще, вдруг поумнею)", "random_id": random.randint(1, 2147483647)})

            else:
                a = list(body)
                b = 10
                data = ""
                while b>=0:
                    b = b - 1
                    data = str(data) + str(a[0])
                    a.pop(0)
                if data == "обновить дз":
                    b = len(a)
                    zap = ""
                    if b >=1:
                        for i in a:
                            zap = str(zap) + str(i)
                        dz = zap
                    else:
                        vk.method("messages.send", {"peer_id": id, "message": "нет задач", "random_id": random.randint(1, 2147483647)})

               # save()
    except Exception as E:
        time.sleep(1)
