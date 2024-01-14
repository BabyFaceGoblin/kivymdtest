from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text = "Hello Daniel", 
                        halign = "center", 
                        theme_text_color = "Custom", text_color = (0, 0, 255/255.0, 1), 
                        font_style = "H2")
        # to get the real rgb color divide the values of what you find in google by 255
        
        icon_label = MDIcon(icon = "language-python", 
                            halign = "center")
        return label
    
DemoApp().run()