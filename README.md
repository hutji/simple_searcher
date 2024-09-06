## Запуск проекта из исходников GitHub

Клонируем себе репозиторий: 

```bash 
git clone git@github.com:hutji/simple_searcher.git
```
Создаем файл .env в корневой директории:
```
ELASTICSEARCH_URL=http://localhost:9200
DATABASE_URL=sqlite+aiosqlite:///documents.db
```


## Запуск локально:

```
poetry run python -m app.main
```

## Запуск через docker-compose:

```
docker compose up --build
```
## Документация:
```
data/docs.json
```

## Тестирование:
Получение постов из CSV:
```
curl "http://localhost:8080/posts"
```
Поиск документов:
```
curl "http://localhost:8080/search?q=your_query"
```
Удаление документа:
```
curl -X DELETE "http://localhost:8080/documents/1"
```
## Технологии:
* #### python 3.11
* #### aiohttp
* #### aiohttp-swagger
* #### aiosqlite
* #### aiosqlite
* #### sqlalchemy
* #### elasticsearch
* #### poetry
* #### docker