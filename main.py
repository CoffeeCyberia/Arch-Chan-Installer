import os
from textual.app import App
from textual.widgets import Footer, Header, Static, Button, Label
from textual.containers import Container

class ArchInstaller(App):
    CSS_PATH = "Stylesheet.tcss"
    def compose(self):
        yield Label("""                                                                                                                                                        
[#F85552]         .8.          [/#F85552][#DFA000] 8 888888888o   [/#DFA000][#8DA101]8 888888888o   [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888888888  [/#DF69BA]           [#35A77C]8 888888888o  [/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 8888888888   [/#F85552][#DFA000]8 8888888888   [/#DFA000]
[#F85552]        .888.         [/#F85552][#DFA000] 8 8888    `88. [/#DFA000][#8DA101]8 8888    `88. [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 8888    `88.[/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552]       :88888.        [/#F85552][#DFA000] 8 8888     `88 [/#DFA000][#8DA101]8 8888     `88 [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 8888     `88[/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552]      . `88888.       [/#F85552][#DFA000] 8 8888     ,88 [/#DFA000][#8DA101]8 8888     ,88 [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 8888     ,88[/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552]     .8. `88888.      [/#F85552][#DFA000] 8 8888.   ,88' [/#DFA000][#8DA101]8 8888.   ,88' [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 888888888888[/#DF69BA]           [#35A77C]8 8888.   ,88'[/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 888888888888 [/#F85552][#DFA000]8 888888888888 [/#DFA000]
[#F85552]    .8`8. `88888.     [/#F85552][#DFA000] 8 888888888P'  [/#DFA000][#8DA101]8 888888888P'  [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 888888888P' [/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552]   .8' `8. `88888.    [/#F85552][#DFA000] 8 8888         [/#DFA000][#8DA101]8 8888         [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 8888        [/#35A77C][#F57D26] 8 8888      88[/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552]  .8'   `8. `88888.   [/#F85552][#DFA000] 8 8888         [/#DFA000][#8DA101]8 8888         [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 8888        [/#35A77C][#F57D26] ` 8888     ,8P[/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552] .888888888. `88888.  [/#F85552][#DFA000] 8 8888         [/#DFA000][#8DA101]8 8888         [/#8DA101][#3A94C5] 8 8888         [/#3A94C5][#DF69BA]8 8888        [/#DF69BA]           [#35A77C]8 8888        [/#35A77C][#F57D26]   8888   ,d8P [/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
[#F85552].8'       `8. `88888. [/#F85552][#DFA000] 8 8888         [/#DFA000][#8DA101]8 8888         [/#8DA101][#3A94C5] 8 888888888888 [/#3A94C5][#DF69BA]8 888888888888[/#DF69BA]           [#35A77C]8 8888        [/#35A77C][#F57D26]    `Y88888P'  [/#F57D26][#F85552] 8 8888         [/#F85552][#DFA000]8 8888         [/#DFA000]
""", classes="title")
        with Container(classes="button1area"):
            yield Button("Start",classes="button1", id="Start")
            yield Button("Exit",classes="button1", id="Exit")

    def _on_key(self, event):
        match event.key:
            case "down":
                self.action_focus_next()
            case "right":
                self.action_focus_next()
            case "up":
                self.action_focus_previous()
            case "left":
                self.action_focus_previous()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "Start":
            next
        if event.button.id == "Exit":
            exit()
    
if __name__ == "__main__":
    app = ArchInstaller()
    app.run()                       