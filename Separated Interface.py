import tkinter as tk
from tkinter import messagebox, simpledialog
from abc import ABC, abstractmethod

# 定义状态接口 / Определение интерфейса состояния
class TaskState(ABC):
    @abstractmethod
    def check(self, context):
        pass

    @abstractmethod
    def publish(self, context):
        pass

# 具体状态类实现接口 / Реализация интерфейса конкретных состояний
class Draft(TaskState):
    def check(self, context):
        messagebox.showinfo("Check", "Checking draft...")  # 检查草稿 / Проверка черновика
        if self._is_valid():
            context.set_state(Review())  # 设置为审核状态 / Установить состояние "Review"
        else:
            context.set_state(NotPresented())  # 设置为未提交状态 / Установить состояние "NotPresented"

    def _is_valid(self):
        # 假设某些验证逻辑 / Предположим, некоторая логика проверки
        return True

    def publish(self, context):
        messagebox.showwarning("Publish", "Cannot publish. Draft not reviewed.")  # 无法发布，草稿未审核 / Невозможно опубликовать. Черновик не проверен.

class NotPresented(TaskState):
    def check(self, context):
        messagebox.showinfo("Check", "Draft not presented. Needs to be revised.")  # 草稿未提交，需要修订 / Черновик не представлен, необходимо пересмотреть
        context.set_state(Draft())  # 设置为草稿状态 / Установить состояние "Draft"

    def publish(self, context):
        messagebox.showwarning("Publish", "Cannot publish. Draft not presented.")  # 无法发布，草稿未提交 / Невозможно опубликовать. Черновик не представлен.

class Review(TaskState):
    def check(self, context):
        messagebox.showinfo("Check", "Reviewing...")  # 正在审核 / Проверка...
        if self._is_valid():
            context.set_state(Poster())  # 设置为海报状态 / Установить состояние "Poster"
        else:
            context.set_state(NotPresented())  # 设置为未提交状态 / Установить состояние "NotPresented"

    def _is_valid(self):
        # 假设某些验证逻辑 / Предположим, некоторая логика проверки
        return True

    def publish(self, context):
        messagebox.showwarning("Publish", "Cannot publish. Review in progress.")  # 无法发布，审核中 / Невозможно опубликовать. Проверка в процессе.

class Poster(TaskState):
    def check(self, context):
        messagebox.showinfo("Check", "Poster already reviewed.")  # 海报已审核 / Постер уже проверен.

    def publish(self, context):
        messagebox.showinfo("Publish", "Publishing poster...")  # 发布海报 / Публикация постера...
        context.set_state(Published())  # 设置为已发布状态 / Установить состояние "Published"

class Published(TaskState):
    def check(self, context):
        messagebox.showwarning("Check", "Cannot check. Already published.")  # 无法检查，已发布 / Невозможно проверить, уже опубликовано.

    def publish(self, context):
        messagebox.showinfo("Publish", "Already published.")  # 已发布 / Уже опубликовано.

# 上下文类 / Класс контекста
class Task:
    def __init__(self, name, label):
        self.name = name
        self.state: TaskState = Draft()  # 初始状态为草稿 / Начальное состояние - черновик
        self.label = label
        self.update_state_label()

    def set_state(self, state: TaskState):
        self.state = state
        self.update_state_label()

    def check(self):
        self.state.check(self)

    def publish(self):
        self.state.publish(self)

    def update_state_label(self):
        state_name = self.state.__class__.__name__
        self.label.config(text=f"Task: {self.name} | State: {state_name}")  # 更新状态标签 / Обновить метку состояния

# GUI部分 / Часть GUI
def add_task():
    task_name = simpledialog.askstring("Input", "Enter the task name:")  # 输入任务名称 / Введите название задачи
    if task_name:
        task_label = tk.Label(task_frame, text="", font=("Arial", 10))
        task_label.pack(pady=5)
        task = Task(task_name, task_label)
        tasks.append(task)
        task.update_state_label()

def start_task():
    task_name = simpledialog.askstring("Input", "Enter the task name to start:")  # 输入要开始的任务名称 / Введите название задачи для начала
    for task in tasks:
        if task.name == task_name:
            task.check()
            return
    messagebox.showwarning("Warning", f"No task named '{task_name}' found.")  # 未找到任务 / Задача с именем '{task_name}' не найдена

def complete_task():
    task_name = simpledialog.askstring("Input", "Enter the task name to complete:")  # 输入要完成的任务名称 / Введите название задачи для завершения
    for task in tasks:
        if task.name == task_name:
            task.publish()
            return
    messagebox.showwarning("Warning", f"No task named '{task_name}' found.")  # 未找到任务 / Задача с именем '{task_name}' не найдена

# 创建GUI应用 / Создание GUI приложения
app = tk.Tk()
app.title("Task Manager")  # 任务管理器 / Менеджер задач
app.geometry("400x300")

tasks = []

task_frame = tk.Frame(app)
task_frame.pack(pady=20)

# 添加任务按钮 / Кнопка добавления задачи
add_task_button = tk.Button(app, text="Add Task", command=add_task, width=20)
add_task_button.pack(pady=5)

# 开始任务按钮 / Кнопка начала задачи
start_task_button = tk.Button(app, text="Start Task", command=start_task, width=20)
start_task_button.pack(pady=5)

# 完成任务按钮 / Кнопка завершения задачи
complete_task_button = tk.Button(app, text="Complete Task", command=complete_task, width=20)
complete_task_button.pack(pady=5)

app.mainloop()
