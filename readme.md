# Умный сервис прогноза погоды
Сервис призван помогать пользователю быстро определить погоду в 
своем населенном пункте и советовать, а что необходимо надеть 
сегодня на улицу, чтобы чувствовать себя комфортно.

**Уровень сложности: со звездочкой**

## Проектирование сервиса

### Технологии
Использовал Python, Django на сервере. Страницы верстал на 
HTML, используя Bootstrap

### Пользовательский интерфейс
Это сайт. На первой странице сайта человек указывает страну и
город. На следующей ему показывается погода в заданной локации.

### Формат ответа
Данные о температуре, скорости ветра и вероятности дождя, 
полученные с API подставляются в HTML страницу. Также в соответствии
с прогнозом добавляется текстовая рекомандация о том, что стоит
одеть на улицу. 

Затем эта HTML страница отправляется пользователю.

## Демонстрация работы

## Процесс работы программы пошагово
Сервис - сайт, который по заданной локации пользователя присылает
ему ответ.

Данные о стране и городе приходят из формы на первой странице сайта.

После отправки формы на сервере происходят следующие действия:
* Запрос к API с данной страной и городом. Если API не может 
отдать прогноз по такой локации, пересылаем пользователя на
специальную страницу. Со специальной страницы можно вернуться
обратно к форме.
* Данные о погоде передаются анализатору. Анализатор говорит, что
стоит одеть на улицу при такой погоде.
* Пользователю возвращается прогноз, где указана температура, 
скорость ветра и вероятность дождя. А также - рекомендация по одежде.

## Установка
```shell script
pip3 install requirements.txt
```

## Запуск
```shell script
python manage.py runserver 8080
```

## Тесты
```shell script
python manage.py test
```