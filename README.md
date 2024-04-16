## Настройка переменных окружения

Для работы с проектом необходимо создать файл `.env` и настроить переменные окружения. Пример содержания файла (`.env.example`):

```
APP_PORT=5000
LOGIN=login
PASSWORD=password
```

## Сборка и запуск контейнеров

1. Для того, чтобы собрать образы контейнеров `ci-cd-app` и `ci-cd-tester` необходимо выполнить следующую команду в директории с `docker-compose.yml` файлом:

```shell
docker compose build
```

2. Для создания и запуска контейнеров из собранных образов необходимо выполнить следующую команду:

```shell
docker compose up
```

## Работа с app-контейнером

При сборке контейнера `ci-cd-app` устанавливается SSH-клиент и запускается веб-приложение из репозитория https://github.com/moevm/devops-examples.git.

* Публичный ключ, используемый в контейнере для внешнего доступа по SSH: `./ssh-keys/id-rsa.pub` 
* Порт хост-машины, в который пробрасывается порт веб-приложения настраивается путем изменением соответствующей переменной окружения `APP_PORT`

Для получения доступа к контейнеру по SSH необходимо воспользоваться приватным ключом (`./ssh-keys/id-rsa`) и выполнить следующую команду:

```shell
ssh root@127.0.0.1 -p 2222 -i <path-to-private-key>
```

## Работа с tester-контейнером

При сборке контейнера `ci-cd-tester` в образ копируется директория `./tests` с тестирующими скриптами.

Для запуска тестов необходимо воспользоваться скриптом `./tests/run_tests.sh`:
* Для запуска **всех** этапов тестирования необходимо выполнить следующую команду:
    ```shell
    docker exec ci-cd-tester bash ./tests/run_tests.sh
    ```
* Для запуска **отдельных** этапов тестирования необходимо указать соответствующий аргумент при запуске скрипта:

  * Форматирование(yapf):
  
    `docker exec ci-cd-tester bash ./tests/run_tests.sh code_style_tests` 
  * Статический анализ (pylint):

    `docker exec ci-cd-tester bash ./tests/run_tests.sh pylint_tests`
  * Интеграционные тесты:

    `docker exec ci-cd-tester bash ./tests/run_tests.sh integration_tests`
  * Selenium тесты (используются переменные окружения `LOGIN` и `PASSWORD` из `.env`-файла):

    `docker exec ci-cd-tester bash ./tests/run_tests.sh selenium_tests`

Этапы `code_style_tests`, `pylint_tests`, `integration_tests` выполняют тестирование веб-приложения из репозитория https://github.com/moevm/devops-examples.git. 

Этап `selenium_tests` используется для автотестирования ИС ИОТ: https://dev.digital.etu.ru/trajectories-test/. Сценарий - *"Создание ОПОП, заполнение вкладок 4, 5, 6"*

В процессе выполнения тестирования формируются файлы, в которых отображаются результаты выполнения тестов. При сборке контейнера определяется монтирование файлов для возможности дальнейшей работы с ними на хост-машине: 
1. `./tests/test_results/stderr.log` - стандартный вывод ошибок
2. `./tests/test_results/stdout.log` - стандартный вывод
3. `./tests/test_results/selenium_screenshots` - скриншоты, сделанные в процессе выполнения selenium-тестов

