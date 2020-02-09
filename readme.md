## Описание

Создает DRF API Views и Serializers для Django приложений


## Установка

0. Поставить venv (опционально)

1. `pip install --upgrade pip setuptools`

2. `pip install -r requirements.txt`


## Использование

0. Создать Django проект 

1. Создать модель и зарегистрировать ее в `INSTALLED_APPS`

2. `python manage.py mycmd %apps% %options%`

```
options:

  -f FORMAT, --format FORMAT
                        view format: viewset(default), apiview, function,
                        modelviewset
  -d DEPTH, --depth DEPTH
                        serialization depth
  --force               force overwrite files
  --serializers         generate serializers only
  --views               generate views only
  --urls                generate urls only
  --verbose             Print out logs of file generation
```
