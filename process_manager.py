import subprocess
import sys
import argparse
import psutil
import os
import time

class MainClass:
    OUTPUT_FILENAME = 'out.txt'

    def __init__(self):
        pass

    def start(self, process_args):
        print("Старт процесса...") 
        with open(self.OUTPUT_FILENAME, 'w') as f:
            subprocess.Popen(process_args, stdout=f, stderr=f)
        print("Процесс успешно стартанул")
        print("Вывод процесса направлен в ", self.OUTPUT_FILENAME)

    def kill(self):
        print("Завершение процесса...")
        pid = self.getPID()      
        if pid:
            p = psutil.Process(pid)
            p.kill();
            print("Процесс завершен")
        else:
            print("Процесс не запущен... Невозможно завершить незапущенный процесс, попробуйте запустить процесс:\nprocess_manager.py START <процесс> <параметры>")

    def restart(self):
        print("Рестарт процесса...")
        pid = self.getPID()      
        if pid:
            p = psutil.Process(pid)
            p.kill();
            process_args = p.cmdline()
            with open(self.OUTPUT_FILENAME, 'w') as f:
                subprocess.Popen(process_args, stdout=f, stderr=f)
        else:
            print("Процесс не запущен... Невозможно перезагрузить незапущенный процесс, попробуйте запустить процесс:\nprocess_manager.py START <процесс> <параметры>")

    def timeout(self, seconds):
        print("Отсроченное завершение процесса...")
        pid = self.getPID()
        if pid:
            seconds_counter = int(seconds)
            while seconds_counter > 0:
                print("Через %d" % (seconds_counter))
                time.sleep(1)
                seconds_counter -= 1

            pid = self.getPID()
            if pid:
                p = psutil.Process(pid)
                p.kill();
                print("Процесс завершен")
            else:
                print("Процесс не запущен... Невозможно завершить незапущенный процесс, попробуйте запустить процесс:\nprocess_manager.py START <процесс> <параметры>")
        else:
            print("Процесс не запущен... Невозможно завершить незапущенный процесс, попробуйте запустить процесс:\nprocess_manager.py START <процесс> <параметры>")

    def getPID(self):
        result = None
        process_info = self.find_process_by_file(self.OUTPUT_FILENAME)
        if process_info:
            result = process_info['pid']
        return result
        
    def find_process_by_file(self, file_path):
        absolute_path = os.path.abspath(file_path)
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                files = proc.open_files()
                for f in files:
                    if f.path == absolute_path:
                        return proc.info
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return None

def try_enter_message():
    print("Введите команду:\n-- Старт процесса: process_manager.py START <process> <params>\n-- Завершение процесса: process_manager.py KILL\n-- Перезагрузка процесса: process_manager.py RESTART\n-- Отсроченное завершение процесса: process_manager.py TIMEOUT <seconds>")
    exit()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        try_enter_message()

    action = sys.argv[1].lower()

    if action == "start":
        if len(sys.argv) < 3:
            try_enter_message()
            
        process = sys.argv[2]
        process_args = sys.argv[2:]
        MainClass().start(process_args) 
        
    elif action == "kill":
        MainClass().kill()

    elif action == "restart":
        MainClass().restart() 

    elif action == "timeout":
        seconds = sys.argv[2]
        MainClass().timeout(seconds) 

    else:
        try_enter_message()

