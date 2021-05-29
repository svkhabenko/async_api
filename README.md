# Шаблон бэкэнд сервисов Python 3.9

## Подготовительные действия
Установка pre-commit-hook и создание локального файла .env
```shell
make init
```

## Запуск в докере
При необходимости поменять в .env конфиги, и выполнить  
```shell
make start
```
Проверить, что сервис живой, и потыкать запросы можно тут - http://localhost:8000/api/openapi.

Чтобы отдельно поднять зависимости выполнить
```shell
make infra
```