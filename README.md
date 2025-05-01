# Annotations Nightmare


### Описание
Скрипты для отработки аннотациий.


### Технологии в проекте
	pre-commit 4.2.0

### Установка
1. Склонируйте проект
```bash
git clone git@github.com:bluesprogrammer-Python/annotations_nightmare.git
cd annotations_nightmare
```
2. Установите пакеты make и uv, если они отсутствуют на ВМ
```bash
sudo apt install make # Ubuntu
pip install uv
pip install --upgrade uv
```

### Запуск проверки mypy
```bash
make typing
```
