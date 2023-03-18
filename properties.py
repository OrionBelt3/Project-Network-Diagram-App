import os
import re
import pickle
import numpy as np

from PyQt5 import QtWidgets

import graph_model
from checker import Checker
from encrypt_module import decrypt_file

def join(*args):
    return os.path.join(*args).replace(os.path.sep, "/")

basedir = os.path.dirname(__file__) # путь до данного файла


class Properties():
    # static field
    verificationPassedTasks = {1: False, 2: False, 3: False, 4: False, 5: False} # массив пройденных заданий

    def __init__(self, MainWindow):
        # self.start_time = time.time_ns() # время начала работы программы в наносекундах
        # self.end_time = None # время завершения последнего задания в наносекундах
        # self.elapsed_time = None # время прошедшее с начала работы программы до завершения последнего задания в наносекундах

        # свойства, использующиеся в разных заданиях
        self.variant = MainWindow.numINGroup
        self.teacherMode = False
        self.key_path = "" # путь до ключа преподавателя 
        self.enter_teacher_mode = [False, False, False, False, False, False]

        # свойства первого окна
        self.MainWindow = MainWindow
        self.radius_points = 30 # радиус вершин по всем заданиям (кроме второго)
        self.step_grid = 100 # шаг сетки по X
        self.step_gridY = 75 # шаг сетки по Y
        self.correct_w = self.MainWindow.getCorrectWeights()
        self.n = len(self.correct_w)
        self.tp = Checker.findEarlyPeriods(self.correct_w, self.n)
        self.tn = Checker.findLatePeriods(self.correct_w, self.tp, self.n)
        self.max_possible_time = self.tp[self.n-1] # максимальное время (для сетки)

        #свойства второго окна
        self.scaler = 3 # параметр увеличения радиуса для второго задания
        self.radius_points_task_2 = self.radius_points * self.scaler # радиус во втором задании

        #свойства третьего окна
        self.state_of_graph_3 = None

        #свойства четвертого окна
        self.state_of_graph_4 = None

        #свойства пятого окна
        self.state_of_graph_5 = None
        self.number_of_squads = self.get_number_of_squads() # количество отделений
        self.correctSquadsPeopleNumber = self.getCorrectSquadsPeopleNumber()
        self.max_sequences_amount = self.GetMaxSequencesAmount(self.number_of_squads) # максимальное число последовательностей по отделениям
        self.graph_for_task_3_4 = self.get_graph_from_radius() # граф для 3-4 задания
        self.graphs_for_task_5 = self.get_graphs_for_task_5() # графы для 5 задания

    def update(self):
        self.variant = self.MainWindow.numINGroup
        self.teacherMode = False
        Properties.verificationPassedTasks = {1: False, 2: False, 3: False, 4: False, 5: False} # массив пройденных заданий
        self.key_path = "" # путь до ключа преподавателя 
        self.enter_teacher_mode = [False, False, False, False, False, False]

        # свойства первого окна
        self.radius_points = 30 # радиус вершин по всем заданиям (кроме второго)
        self.step_grid = 100 # шаг сетки по X
        self.step_gridY = 75 # шаг сетки по Y
        self.correct_w = self.MainWindow.getCorrectWeights()
        self.n = len(self.correct_w)
        self.tp = Checker.findEarlyPeriods(self.correct_w, self.n)
        self.tn = Checker.findLatePeriods(self.correct_w, self.tp, self.n)
        self.max_possible_time = self.tp[self.n-1] # максимальное время (для сетки)

        #свойства второго окна
        self.scaler = 3 # параметр увеличения радиуса для второго задания
        self.radius_points_task_2 = self.radius_points * self.scaler # радиус во втором задании

        #свойства третьего окна
        self.state_of_graph_3 = None

        #свойства четвертого окна
        self.state_of_graph_4 = None

        #свойства пятого окна
        self.state_of_graph_5 = None
        self.number_of_squads = self.get_number_of_squads() # количество отделений
        self.correctSquadsPeopleNumber = self.getCorrectSquadsPeopleNumber()
        self.max_sequences_amount = self.GetMaxSequencesAmount(self.number_of_squads) # максимальное число последовательностей по отделениям
        self.graph_for_task_3_4 = self.get_graph_from_radius() # граф для 3-4 задания
        self.graphs_for_task_5 = self.get_graphs_for_task_5() # графы для 5 задания

    
    def GetMaxSequencesAmount(self, number_of_squads):
        max_sequences_amount = 0
        for squad in range(1, number_of_squads+1):
            current_squad_max = 0
            for row in range(self.MainWindow.ui.tableVar.rowCount()):
                try:
                    current_squad = int(self.MainWindow.ui.tableVar.item(row, 1).text())
                except:
                    current_squad = -1
                if (current_squad == squad):
                    current_squad_max  += 1
            if (current_squad_max > max_sequences_amount):
                max_sequences_amount = current_squad_max
        return max_sequences_amount

    # функция подсчета количесва отделений
    def get_number_of_squads(self):
        number_of_squads = 1
        for row in range(self.MainWindow.ui.tableVar.rowCount()):
            if self.MainWindow.ui.tableVar.item(row, 1).text() >= '1' and self.MainWindow.ui.tableVar.item(row, 1).text() <= '9' :
                i = int(self.MainWindow.ui.tableVar.item(row, 1).text())
            if number_of_squads < i:
                number_of_squads = i
        return number_of_squads

    # функция получения общего графа
    def get_graph_from_radius(self):
        return graph_model.Graph(self.radius_points)

    # функция получения общего графа
    def get_graph_from_graph(self, graph):
        new_graph = graph.copy()
        return new_graph

    # функция получения списка графов для 5 задания
    def get_graphs_for_task_5(self):
        graphs = []
        for i in range(self.number_of_squads):
            graphs.append(self.get_graph_from_radius)
        return graphs

    @staticmethod
    def getVerificationPassedTasks(current):
        return Properties.verificationPassedTasks[current]    

    # функция получения подтверждения пройденых заданий
    @staticmethod
    def getVerificationPassedPretasks(current):
        if (Properties.verificationPassedTasks[current - 1] == False):
            return False
        else:
            return True

    # функция присваивания  подтверждения заданию
    @staticmethod
    def setVerificationPassedTask(number):
        Properties.verificationPassedTasks[number] = True

    @staticmethod
    def setVerificationPassedTaskAll(arg):
        if (arg):
            Properties.verificationPassedTasks = {1: True, 2: True, 3: True, 4: True, 5: True}
        else:
            Properties.verificationPassedTasks = {1: False, 2: False, 3: False, 4: False, 5: False}

    # ФУНКЦИИ ДЛЯ РАБОТЫ С ШИФРОВАНИЕМ   
    def check_key(self, key_path) -> bool:
        try:
            with open(key_path, "rb") as file:
                secret_key = file.read()
            tmp_path = join(basedir, "encrypted_key")
            print("TMP_PATH ", tmp_path)
            teacher_token = decrypt_file(tmp_path, "teacher_token.txt") ####### ОШИБКА
            print("teacher_token", teacher_token, "\t", "secret_key ", secret_key)
            if teacher_token == b"ERROR_DECRYPT":
                print("key_path not exist1: ERROR_DECRYPT")
                return False
            if secret_key == teacher_token:
                print("key_path is exist")
                return True
        except Exception:
            print("key_path not exist2 LOSE")
            return False

    def enter_key(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName()[0]
        print(file_name)
        if file_name == "":
            print("key_path not exist1")
            return False
        if self.check_key(file_name):
            self.key_path = file_name
            print("key_path is exist")
            return True
        else:
            print("key_path not exist2")
            return False

    def get_num_squad(self):
        self.tableNumSquad = []
        for row in range(self.MainWindow.ui.tableVar.rowCount()):
            if self.MainWindow.ui.tableVar.item(row, self.MainWindow.ui.tableVar.columnCount() - 1) and self.MainWindow.ui.tableVar.item(row, self.MainWindow.ui.tableVar.columnCount() - 1) != ' ':
                self.tableNumSquad.append([])
                tmpItem = self.MainWindow.ui.tableVar.item(row, self.MainWindow.ui.tableVar.columnCount() - 1).text()
                self.tableNumSquad[-1].append(tmpItem)
            else:
                break

            #self.tableNumSquad[-1].appclear_answerend(tmpItem)
            #print("item", row, self.MainWindow.ui.tableVar.columnCount() - 1, " ", self.tableNumSquad[-1][-1])
        
        for i in self.tableNumSquad:
            print(i)

    def getCorrectSquadsPeopleNumber(self):
        SquadsPeopleNumber = np.zeros((self.number_of_squads), int)

        for row in range(self.number_of_squads):
            SquadPeopleNumber = int(self.MainWindow.ui.tableVar.item(row, 5).text())
            SquadsPeopleNumber[row] = SquadPeopleNumber

        return SquadsPeopleNumber


####################____ФУНКЦИИ_ДЛЯ_РАБОТЫ_С_СОХРАНЕНИЕМ_ОБЪЕКТА_ДЛЯ_ПРЕПОДА__####################################################
    
    def save_graph_for_teacher(self, graph, i, subtask = 0):
        if subtask == 0:
            with open(f'answer/states_of_graphs_{i}/state_{self.variant}.pickle', 'wb') as file:
                pickle.dump(graph, file)
        else:
            with open(f'answer/states_of_graphs_{i}/state_{self.variant}_task_{subtask}.pickle', 'wb') as file:
                pickle.dump(graph, file)

    def get_graph_for_teacher(self, i, subtask = 0):
        if subtask == 0:
            with open(f'answer/states_of_graphs_{i}/state_{self.variant}.pickle', 'rb') as file:
                graph = pickle.load(file)
        else:
            with open(f'answer/states_of_graphs_{i}/state_{self.variant}_task_{subtask}.pickle', 'rb') as file:
                graph = pickle.load(file)
        return graph


    def get_gft(self, i, subtask = 0):
        if subtask == 0:
            with open(f'answer/states_of_graphs_{i}/state_1.pickle', 'rb') as file:
                graph = pickle.load(file)
        else:
            with open(f'answer/states_of_graphs_{i}/state_1_task_{subtask}.pickle', 'rb') as file:
                graph = pickle.load(file)
        return graph
#######################################################################################################################


####################____ФУНКЦИИ_ДЛЯ_РАБОТЫ_С_СОХРАНЕНИЕМ_ОБЪЕКТА_ДЛЯ_ СТУДЕНТА__####################################################

    def save_graph_for_student(self, graph, i, subtask = 0):
        if subtask == 0:
            with open(f'answer_of_student/states_of_graphs_{i}/state_{self.variant}.pickle', 'wb') as file:
                pickle.dump(graph, file)
        else:
            with open(f'answer_of_student/states_of_graphs_{i}/state_{self.variant}_task_{subtask}.pickle', 'wb') as file:
                pickle.dump(graph, file)


    def get_graph_for_student(self, i, subtask = 0):
        if subtask == 0:
            with open(f'answer_of_student/states_of_graphs_{i}/state_{self.variant}.pickle', 'rb') as file:
                graph = pickle.load(file)
        else:
            with open(f'answer_of_student/states_of_graphs_{i}/state_{self.variant}_task_{subtask}.pickle', 'rb') as file:
                graph = pickle.load(file)
        return graph
#######################################################################################################################

####################____ФУНКЦИИ_ДЛЯ_ОЧИСТКИ_СОХРАНЕНИЯ_СТУДЕНТА____####################################################

    def clear_answer(self, task, subtask = 0):

        if subtask == 0:
            try:
                os.remove(f'answer_of_student/states_of_graphs_{task}/state_{self.variant}.pickle')
                print(f'[INFO] DELETE ----> answer_of_student/states_of_graphs_{task}/state_{self.variant}.pickle')
            except:
                print(f'[WARN] DELETE ----> answer_of_student/states_of_graphs_{task}/state_{self.variant}.pickle' + 'not found!')
        else:
            try:
                os.remove(f'answer_of_student/states_of_graphs_{task}/state_{self.variant}_task_{subtask}.pickle')
                print(f'[INFO] DELETE ----> answer_of_student/states_of_graphs_{task}/state_{self.variant}_task_{subtask}.pickle')
            except:
                print(f'[WARN] DELETE ----> answer_of_student/states_of_graphs_{task}/state_{self.variant}_task_{subtask}.pickle' + 'not found!')

####################################################################################################################### 


####################____ФУНКЦИИ_ДЛЯ_ОЧИСТКИ_СОХРАНЕНИЯ_ПРЕПОДА___####################################################

    def clear_answer_teacher(self, task, subtask = 0):

        if subtask == 0:
            try:
                os.remove(f'answer/states_of_graphs_{task}/state_{self.variant}.pickle')
                print(f'[INFO] DELETE ----> answer/states_of_graphs_{task}/state_{self.variant}.pickle')
            except:
                print(f'[WARN] DELETE ----> answer/states_of_graphs_{task}/state_{self.variant}.pickle' + 'not found!')
        else:
            try:
                os.remove(f'answer/states_of_graphs_{task}/state_{self.variant}_task_{subtask}.pickle')
                print(f'[INFO] DELETE ----> answer/states_of_graphs_{task}/state_{self.variant}_task_{subtask}.pickle')
            except:
                print(f'[WARN] DELETE ----> answer/states_of_graphs_{task}/state_{self.variant}_task_{subtask}.pickle' + 'not found!')

####################################################################################################################### 

####################____ФУНКЦИИ_ДЛЯ_ОЧИСТКИ_СОХРАНЕНИЯ_СТУДЕНТА____####################################################
    
    def clear_answer_universal(self, variant, pathToDir = 'answer_of_student/'):
        for i in range(1, 6):
            path = pathToDir + f'states_of_graphs_{i}/'
            pattern = f'state_{variant}'
            self.purge(path, pattern)
        
    def purge(self, dir, pattern):
        try:
            for f in os.listdir(dir):
                if re.search(pattern, f):
                    print(f'[INFO] DELETE FILE ----> {os.path.join(dir, f)}')
                    os.remove(os.path.join(dir, f))
        except:
            pass
####################################################################################################################### 
