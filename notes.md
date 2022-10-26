Шпаргалка Selenium
____
## Оглавление

- Поиск элемента
  - [Методы поиска элементов](#Методы-поиска-элементов)
  - [Поиск элемента по тексту в ссылке](#Поиск-элемента-по-тексту-в-ссылке)
  - [Поиск элемента по XPATH](#Поиск-элемента-по-XPATH)
- Веб элементы
    - [Checkbox, Radiobutton](#Checkbox,-Radiobutton)
    - [Список (select, option)](#Список-(select,-option))
    - [Вызвать javascript код](#Вызвать-javascript-код)
- Уровень списка 1. Пункт 3.

## Методы поиска элементов

- **find_element(By.ID, value)** — поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
- **find_element(By.CSS_SELECTOR, value)** — поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;
- **find_element(By.XPATH, value)** — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
- **find_element(By.NAME, value)** — поиск по атрибуту name элемента;
- **find_element(By.TAG_NAME, value)** — поиск элемента по названию тега элемента;
- **find_element(By.CLASS_NAME, value)** — поиск по значению атрибута class;
- **find_element(By.LINK_TEXT, value)** — поиск ссылки на странице по полному совпадению;
- **find_element(By.PARTIAL_LINK_TEXT, value)** — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.

____

## Поиск элемента по тексту в ссылке

```python
link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")  # по полному соответствию текста
link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")  #  по подстроке
```
____
## Поиск элемента по XPATH

```python
button = browser.find_element(By.XPATH, "//button[@type='submit']")
button = browser.find_element(By.XPATH, "//button[text()='Submit']")
button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
```
____
## Checkbox, Radiobutton
По label
```html
<input type="checkbox" id="coding" name="interest" value="coding" checked />
<label for="coding">Coding</label>
```
```html
<input type="radio" id="coding" name="language">
<label for="coding">Java</label>
```

```python
input = browser.find_element(By.CSS_SELECTOR, "[for='coding']").click()
```

По value
```html
<input type="checkbox" id="python" name="python" value="python" checked />
```

```html
<input type="radio" name="language" value="python">
```

```python
input = browser.find_element(By.CSS_SELECTOR, "[value='python']").click()
```

get_attribute

```python
robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None
```
____
## Список (select, option)


Выбрать option в списке
```python
browser.find_element(By.TAG_NAME, "select").click()

browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
# browser.find_element(By.CSS_SELECTOR, "[value='1']").click()
```
или
```python
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1")
# select.select_by_visible_text("text")
# select.select_by_index(index)
```

____
## Вызвать javascript код

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
browser.execute_script("alert(\"Robots at work\");")
browser.execute_script("document.title='Script executing';alert('Robots at work');")
```

## upload file
```python
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)
```

## alert
```python
alert = browser.switch_to.alert  # переключаемся на окно
alert.accept()  # нажимаем принять
```

```python
alert = browser.switch_to.alert  # переключаемся на окно
alert_text = alert.text  # получаем текст из окна
```
окно с выбором:
```python
confirm = browser.switch_to.alert
confirm.accept()  # принять
confirm.dismiss()  # отказаться
```
окно с полем ввода текста:
```python
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
```
## Переход на другую вкладку

```python
current_window = browser.current_window_handle  # текущая вкладка
first_window = browser.window_handles[0]
second_window = browser.window_handles[1]

browser.switch_to.window(window_name)
```
## Implicit Waits
Неявное ожидание. Проверяет наличие элемента каждые 500 мс
```python
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)
```
## Explicit Waits
```python
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
```
В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания:

- title_is
- title_contains
- presence_of_element_located
- visibility_of_element_located
- visibility_of
- presence_of_all_elements_located
- text_to_be_present_in_element
- text_to_be_present_in_element_value
- frame_to_be_available_and_switch_to_it
- invisibility_of_element_located
- element_to_be_clickable
- staleness_of
- element_to_be_selected
- element_located_to_be_selected
- element_selection_state_to_be
- element_located_selection_state_to_be
- alert_is_present

## assert

```python
assert True  #  True
assert False  # AssertionError
assert abs(-42) == -42  # AssertionError
assert abs(-42) == -42, 'error description'  # error description
assert abs(-42) == 42, 'error description'  # True
```
