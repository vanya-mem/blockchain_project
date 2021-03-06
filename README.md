# Блокчейн проект
На данной странице я сделаю простенький блокчейн, который будет работать как подобие школьного дневника. Основная идея проекта - возможность увидеть: были ли изменены данные или нет.

# Установка через Git
Если у вас установлен Git, то можно просто сделать клонирование данного репозитория в своё виртуальное окружение. 

1) ![image](https://user-images.githubusercontent.com/71513027/158489028-f8924873-1753-4792-b5fe-c9d77efa9b8e.png)

2) Идем по пути своего виртуального окружения, нажимаем там правой кнопкой мыши и выбираем Git Bash Here 

![image](https://user-images.githubusercontent.com/71513027/158482777-b1aebff1-8eec-459d-977c-1c05d01a4637.png)

3)Пишем git clone и вставляем ссылку из пункта 1. Нажимаем Enter. Готово! 

![image](https://user-images.githubusercontent.com/71513027/158483701-cbe3c71f-373f-4b0d-a26d-e4b5d8cc6b48.png)

# Установка при помощи скачивания
Если же у вас нету Git'а, то файлы можно просто скачать. 

1) ![image](https://user-images.githubusercontent.com/71513027/158483973-1520ba52-2b96-479d-98b8-b9848337729e.png)

2)После скачивания, переходим в Загрузки. Там будет zip файл с названием blockchain_project. Открываем его и перебрасываем папку blockchain_project в виртуальное окружение. Готово!

![image](https://user-images.githubusercontent.com/71513027/158484188-f15dc5a0-fc9f-491d-9e1c-5d82e7132321.png)

# Использование 
Чтобы начать работу, необходимо открыть файл main.py по пути "виртуальное_окружение"/blockchain_project/flask/App

![image](https://user-images.githubusercontent.com/71513027/158484543-8982cc40-5ce5-4e5f-aeb0-e864bc89fd8a.png)

Далее, нажимаем правой кнопкой мыши по области с кодом и выбираем пункт "Run 'main'".

![image](https://user-images.githubusercontent.com/71513027/158484862-d9b48562-2994-4412-a9e3-ec34fba89bba.png)

В окне вывода у нас появится локальный адрес, пройдя по которому у нас откроется веб-интерфейс нашей программы. 

![image](https://user-images.githubusercontent.com/71513027/158485063-74858736-1106-47de-9f20-6d14191a3440.png)

Откроется окно браузера, в котором будут видны поля для ввода данных. Введя необходимые данные, нужно нажать кнопку "Записать". Записанная информация появится по пути виртуальное_окружение/blockchain_project/flask/App/blockchain/"Название папки, взятое из поля 'Имя и фамилия'". Там будет иннициалирующий блок с данными, которые мы только что записали. 

![image](https://user-images.githubusercontent.com/71513027/158485672-160d0ae7-85ab-4b44-806e-6db53510698b.png)

![image](https://user-images.githubusercontent.com/71513027/158485754-065fe152-2a9f-4777-9d27-3185cdfd458f.png)

![image](https://user-images.githubusercontent.com/71513027/158485781-4d00fb0e-1bc6-4090-b790-589220d1b038.png)

![image](https://user-images.githubusercontent.com/71513027/158485819-0c7471c8-e700-4142-8425-aa2e1e91a2da.png)

При записи следующих блоков, у нас будет формироваться хэш-сумма предыдущих данных, которая будет записана в строке 'Хэш'.

![image](https://user-images.githubusercontent.com/71513027/158486016-a744046e-a93a-4d22-8945-f516b65faa66.png)

Далее, мы можем проверить: были ли изменены данные в предыдущих записях. Сделать это можно при помощи кнопки 'Проверить целостность'. Если информация не была изменена, то будут выведены следующие данные: "Номер блока: Всё в порядке" (картинка 1). В противном же случае будет написано: "Номер блока: Изменен" (картинка 2).

![image](https://user-images.githubusercontent.com/71513027/158486453-36d11a72-c7d1-4b75-a1fe-e5b48b7e0138.png)

![image](https://user-images.githubusercontent.com/71513027/158486505-c9c0bb7f-6be8-4a40-80ee-df70b8f901c2.png)

Чтобы завершить работу программы, необходимо зайти в среду программирования и нажать на красный квадратик в меню "Run" у файла main.py.

![image](https://user-images.githubusercontent.com/71513027/158486766-78e82f43-0ed8-4b1b-b009-de15d25052b1.png)

# Дополнительная информация

Для полноценной работы программы необходимы следующие компоненты:
1) Установленный Python
2) Установленный PyCharm
3) Если со скачиванием кода библиотека flask не установилась, то необходимо зайти в PyCharm, выбрать внизу вкладку "Terminal" и там подключиться к директории проекта (cd путь до директории, где находится наша программа). Далее, надо написать следующее: pip install flask и нажать Enter. Готово!

![image](https://user-images.githubusercontent.com/71513027/158903823-b67952c2-1067-4efc-ae66-ef95a7683dee.png)

![image](https://user-images.githubusercontent.com/71513027/158903879-56d86e3b-aefb-4109-bc0a-dc94ee0fa679.png)
