# Лабораторная по очередям

## Обозначения
- **λ** - новых клиентов/единицу времени
- **k** - корличество обработчиков
- S1...Sk - обработчики
- **μ** - скорость обработки, клиентов/единицу времени
- **n** - кол-во клиентов в системе
- **L** - среднее кол-во клиентов в системе
- **w** == 1/μ - время обработки одного клиента
- **r** == λ/μ - среднее число занятых обработчиков

## Известные условия
- Система является системой с потерями - если все обработчики заняты, клиенту отказывают в обработке (выбрасывает из системы)

## Задачи лабораторной
- Найти:
    - Среднее время обработки (обозначим за **t**)
    - Среднее количство людей в системе (**L**)
    - Вероятность отказа (обозначим за **z**)
- Построить графики (по x - время, по y - кол-во клиентов):
    - Зависимость кол-ва клиентов от времени
    - Среднее кол-во клиентов в системе в момент времени

## Части проекта
### Формулы
Математические формулы, в текстовом виде, описывающие систему, включаяющие в себя все необходимые гиперпараметры и позволяющие вычислять целевые параметры. Некоторые должны принимать на вход время (для построения графиков).
### Программа
Формулы из пункта выше в виде функций на одном из языков программирования.
### Программная обработка результатов
Проверка корректности формул и их программной записи, вычисление целевых параметров, построение графиков, проверка работы с разными гиперпараметрами.
### Презентация
Наглядное представление всех результатов, полученных после выполнения шагов, описанных выше. Визуальная презентация + доклад. Время - 5 минут.
