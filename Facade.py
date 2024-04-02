import tkinter as tk

# 定义形状管理器类，用于管理不同的图形
# Определение класса менеджера форм для управления различными фигурами
class ShapeManager:
    def __init__(self, canvas):
        self.canvas = canvas  # 画布实例
        # Экземпляр холста

    # 创建圆形的方法
    # Метод для создания круга
    def create_circle(self, x, y, radius, **kwargs):
        return self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, **kwargs)

    # 创建矩形的方法
    # Метод для создания прямоугольника
    def create_rectangle(self, x1, y1, x2, y2, **kwargs):
        return self.canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

# 定义图形门面类，用于简化图形操作
# Определение фасадного класса графики для упрощения операций с графикой
class GraphicsFacade:
    def __init__(self, canvas):
        self.manager = ShapeManager(canvas)  # 实例化形状管理器
        # Создание экземпляра менеджера форм

    # 画一个蓝色圆形的方法
    # Метод для рисования синего круга
    def draw_blue_circle(self):
        self.manager.create_circle(50, 50, 40, fill='blue', outline='blue')

    # 画一个红色矩形的方法
    # Метод для рисования красного прямоугольника
    def draw_red_rectangle(self):
        self.manager.create_rectangle(150, 50, 250, 150, fill='red', outline='red')

# 定义图形编辑器类，用于创建用户界面
# Определение класса графического редактора для создания пользовательского интерфейса
class GraphicsEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("简易图形编辑器")  # 窗口标题
        # Заголовок окна

        self.canvas = tk.Canvas(root, width=400, height=300, bg='white')  # 创建画布
        self.canvas.pack(pady=20)
        # Создание холста

        self.facade = GraphicsFacade(self.canvas)  # 实例化图形门面

        # 添加按钮，通过Фасад类操作
        # 添加按钮，通过门面类进行操作
        tk.Button(root, text="创建蓝色圆形", command=self.facade.draw_blue_circle).pack(side=tk.LEFT, padx=10)
        # Кнопка для создания синего круга
        tk.Button(root, text="创建红色矩形", command=self.facade.draw_red_rectangle).pack(side=tk.LEFT)
        # Кнопка для создания красного прямоугольника

# 主函数，用于启动程序
# Главная функция для запуска программы
def main():
    root = tk.Tk()
    app = GraphicsEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()



    #
