import tkinter as tk
from tkinter import messagebox

# 定义状态接口 / Определение интерфейса состояния
class State:
    def check(self, context):
        pass

    def publish(self, context):
        pass

# 草稿状态 / Состояние черновика
class Draft(State):
    def check(self, context):
        messagebox.showinfo("Check", "Checking draft...")  # 显示检查草稿的信息 / Показать информацию о проверке черновика
        if self._is_valid():
            context.set_state(Review())
        else:
            context.set_state(NotPresented())

    def _is_valid(self):
        # 假设某些验证逻辑 / Предполагаем некоторая логика проверки
        return True

# 未提交状态 / Состояние "не представлен"
class NotPresented(State):
    def check(self, context):
        messagebox.showinfo("Check", "Draft not presented. Needs to be revised.")  # 显示草稿未提交的信息 / Показать информацию о не представленном черновике
        context.set_state(Draft())

    def publish(self, context):
        messagebox.showwarning("Publish", "Cannot publish. Draft not presented.")  # 显示无法发布的警告 / Показать предупреждение о невозможности публикации

# 审核状态 / Состояние проверки
class Review(State):
    def check(self, context):
        messagebox.showinfo("Check", "Reviewing...")  # 显示审核的信息 / Показать информацию о проверке
        if self._is_valid():
            context.set_state(Poster())
        else:
            context.set_state(NotPresented())

    def _is_valid(self):
        # 假设某些验证逻辑 / Предполагаем некоторая логика проверки
        return True

    def publish(self, context):
        messagebox.showwarning("Publish", "Cannot publish. Review in progress.")  # 显示无法发布的警告 / Показать предупреждение о невозможности публикации

# 海报状态 / Состояние плаката
class Poster(State):
    def publish(self, context):
        messagebox.showinfo("Publish", "Publishing poster...")  # 显示发布海报的信息 / Показать информацию о публикации плаката
        context.set_state(Published())

    def check(self, context):
        messagebox.showinfo("Check", "Poster already reviewed.")  # 显示海报已审核的信息 / Показать информацию о проверенном плакате

# 已发布状态 / Состояние опубликованного
class Published(State):
    def publish(self, context):
        messagebox.showinfo("Publish", "Already published.")  # 显示已经发布的信息 / Показать информацию о уже опубликованном

    def check(self, context):
        messagebox.showwarning("Check", "Cannot check. Already published.")  # 显示无法检查的警告 / Показать предупреждение о невозможности проверки

# 上下文类 / Класс контекста
class Context:
    def __init__(self, label):
        self.state = Draft()  # 初始状态为草稿 / Начальное состояние - черновик
        self.label = label
        self.update_state_label()

    def set_state(self, state):
        self.state = state  # 设置当前状态 / Установка текущего состояния
        self.update_state_label()

    def check(self):
        self.state.check(self)  # 调用当前状态的检查方法 / Вызов метода проверки текущего состояния

    def publish(self):
        self.state.publish(self)  # 调用当前状态的发布方法 / Вызов метода публикации текущего состояния

    def update_state_label(self):
        state_name = self.state.__class__.__name__
        self.label.config(text=f"Текущее состояние: {state_name}")  # 更新标签显示当前状态 / Обновление метки для отображения текущего состояния

# 检查操作 / Действие проверки
def check_action():
    context.check()

# 发布操作 / Действие публикации
def publish_action():
    context.publish()

# 创建GUI应用 / Создание GUI приложения
app = tk.Tk()
app.title("文档状态管理器")  # 设置窗口标题 / Установка заголовка окна
app.geometry("600x450")

# 状态标签 / Метка состояния
state_label = tk.Label(app, text="Текущее состояние: Draft", font=("Arial", 12))
state_label.pack(pady=10)

context = Context(state_label)

# 检查按钮 / Кнопка проверки
check_button = tk.Button(app, text="исследовать", command=check_action, width=20)
check_button.pack(pady=15)

# 发布按钮 / Кнопка публикации
publish_button = tk.Button(app, text="выпускать", command=publish_action, width=20)
publish_button.pack(pady=15)

app.mainloop()
