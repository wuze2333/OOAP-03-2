import tkinter as tk
#This Singleton Design Patterns
# Класс для управления настройками
class SettingsManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SettingsManager, cls).__new__(cls)
            cls._instance.themeColor = 'Light'
            cls._instance.fontSize = 12
        return cls._instance

    ##__new__ класса SettingsManager и использует закрытый статический
    # атрибут _instance и блокировку потока _lock, чтобы гарантировать,
    # что в любой момент, независимо от того, сколько потоков попытается создать
    # экземпляр SettingsManager, будет создан только один экземпляр.
    # Это обеспечивает глобальную уникальность класса SettingsManager.

# Класс GUI
class GUI:
    def __init__(self, master):
        self.master = master
        self.settings = SettingsManager()

        # Элементы интерфейса
        self.theme_option = tk.StringVar(value=self.settings.themeColor)
        self.font_size_slider = tk.Scale(master, from_=10, to=20, orient='horizontal', label='Размер шрифта',
                                         command=self.update_font_size)
        self.font_size_slider.set(self.settings.fontSize)

        # Добавление меню выбора темы и ползунка размера шрифта
        tk.OptionMenu(master, self.theme_option, 'Light', 'Dark', command=self.update_theme).pack()
        self.font_size_slider.pack()

        # Область предварительного просмотра
        self.preview = tk.Label(master, text="Предварительный просмотр текста")
        self.preview.pack()
        self.update_preview()

        #Для класса SettingsManager используется паттерн Singleton, при котором все компоненты
        # приложения используют один и тот же экземпляр настроек. Это гарантирует,
        # что при изменении настроек (например, цвета темы или размера шрифта)
        # эти изменения вступят в силу глобально,
        # а не для каждого компонента будет создана своя копия  настроек,
        # что может привести к несогласованному поведению и отображению.#



    def update_theme(self, theme):
        self.settings.themeColor = theme
        self.update_preview()

    def update_font_size(self, event):
        self.settings.fontSize = self.font_size_slider.get()
        self.update_preview()

    def update_preview(self):
        # Обновление стиля области предварительного просмотра в соответствии с текущими настройками
        bgColor = '#FFF' if self.settings.themeColor == 'Light' else '#333'
        fgColor = '#000' if self.settings.themeColor == 'Light' else '#FFF'
        self.preview.config(bg=bgColor, fg=fgColor, font=('Arial', self.settings.fontSize))

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop() # Входим в основной цикл событий