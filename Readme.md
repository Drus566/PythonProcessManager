# Описание
process_manager.py - скрипт для управления процессом.

### Управление:
Введите команду:
-- Старт процесса: process_manager.py START <process> <params>
-- Завершение процесса: process_manager.py KILL
-- Перезагрузка процесса: process_manager.py RESTART
-- Отсроченное завершение процесса: process_manager.py TIMEOUT <seconds>"

### Примечение:
Скрипт может перезагрузить или завершить процесс только если он уже запущен. Скрипт анализируется файл вывода запущенного процесса (по умолчанию out.txt), если он открыт, то получаем всю информацию о процессе, который открыл его и перезапускаем/завершаем процесс.

### Используемое ПО 
* Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
* Библиотека psutil: 5.9.8 (необходимо доустановить `pip3 install psutil`

### Пример применения 
n1@tc08:~/python$ touch alt.txt
n1@tc08:~/python$ python3 process_manager.py START tail -f alt.txt
Старт процесса...
Процесс успешно стартанул
Вывод процесса направлен в  out.txt
n1@tc08:~/python$ echo "Привет мир" >> alt.txt
n1@tc08:~/python$ cat out.txt
Привет мир
n1@tc08:~/python$ python3 process_manager.py TIMEOUT 3
Отсроченное завершение процесса...
Через 3
Через 2
Через 1
Процесс завершен
n1@tc08:~/python$ echo "Hello world" >> alt.txt
n1@tc08:~/python$ cat out.txt
Привет мир
n1@tc08:~/python$
