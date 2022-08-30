import json
from flask import Flask

app = Flask(__name__)   # Точка входа в наш файл app-имя файла


@app.route("/")  # Маршрут к странице. В скобках прописываем адрес страницы
def page_index():
    with open('candidates.json', encoding='utf8') as f:  # Создаем ссылку на файл в виде переменной f
        candidates = json.load(f)  # Загружаем данные файла в переменную candidates
        persons = []               # Новый список, где будут хранится необходимые данные о кандидатах
        for candidate in candidates:
            persons.append(        # Добавляем в новый список при помощи функции page
                page(candidate)
            )
    t = '\n'

    return f'<!DOCTYPE html> <html land="ru"><head><meta charset="UTF-8"/></head><body><pre>{t.join(persons)}</pre></body></html>'   # Возвращаем html страницу с выводом данных(выводит список persons)


@app.route("/candidates/<id_cand>")
def get_candidates_by_id(id_cand):  # параметр при get запросе всегда передается в виде строки
    with open('candidates.json', encoding='utf8') as f:
        candidates = json.load(f)
        persons_id = []
        for candidate in candidates:
            if int(id_cand) == candidate['id']:  # Здесь необходимо добавить int, так как изначально тип id_cand == str
                persons_id.append(
                    page(candidate)
                )
    t = '\n'

    return f'<!DOCTYPE html> <html land="ru"><head><meta charset="UTF-8"/></head><body><img src="{candidate["picture"]}"><pre>{t.join(persons_id)}</pre></body></html>'


@app.route("/skills/<skills_person>")
def find_skill(skills_person):   # Функция фильтрования по скиллам
    skills_person.lower()        # Функция lower переводит вводимые в строке данные в нижний регистр
    with open('candidates.json', encoding='utf8') as f:
        candidates = json.load(f)
        candidates_skills = []
        for candidate in candidates:
            if skills_person in candidate['skills'].lower():  # Переводит все значения ключа skills в нижний регистр
                candidates_skills.append(
                    page(candidate)
                )
    t = '\n'

    return f'<!DOCTYPE html> <html land="ru"><head><meta charset="UTF-8"/></head><body><pre>{t.join(candidates_skills)}</pre></body></html>'

def page(candidate):
    return f"Имя кандидата - {candidate['name']}\nПозиция кандидата - {candidate['position']}\nНавыки - {candidate['skills']}\n"  # Формируем строку



app.run()
