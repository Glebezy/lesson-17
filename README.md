## Проект API автотестов reqres.in

<!-- Технологии -->

### Используемые технологии

<p style="text-align: center;">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Requests" src="images/logo/requests.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>


<!-- Тест кейсы -->

### Что проверяем

* Регистрация пользователя с валидными данными
* Удаление пользователя
* Получение данных существующего пользователя
* Получение данных несуществующего пользователя
* Регистрация пользователя с невалидными данными
* Изменение данных ресурса

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/16-glebezy-python-unit17/)

##### При нажатии на "Build Now" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.

![This is an image](images/screenshots/jenkins.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/logo/allure_report.png"> Allure report

##### После прохождения тестов, результаты можно посмотреть в Allure отчете

![This is an image](images/screenshots/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритизации, по времени прохождения и др.

![This is an image](images/screenshots/allure_graphs.png)

##### Во вкладке Behaviors находятся собранные тест кейсы, у которых описаны шаги и приложены логи о прохождении теста

![This is an image](images/screenshots/allure_suites.png)



<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/logo/tg.png"> Интеграция с Telegram

##### После прохождения тестов, в Telegram-бот приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](images/screenshots/tg_bot.png)
