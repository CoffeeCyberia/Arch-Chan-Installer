# Ill try to use as little AI as Possible but Sometimes my skills arent good enought.
# But everything ill Code with AI will get Noted in Obsidian. You Can find my Notes for this Project in the Reposetory
# Thx for using this Programm. If you have some Correction for my code feel free to Edit and commit you Changes.

import os
from textual.binding import Binding
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static, Button, Label, TabbedContent, TabPane, RadioButton, RadioSet, Tabs, Select, Input
from textual.containers import Container, Center, Vertical, Horizontal
from textual.screen import Screen
import subprocess




LOGO = """       


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

"""

class Logo(Label):                                 #AI (Noted how it Works in the Obsidian Vault)
    def __init__(self) -> None:                    #AI
        super().__init__(LOGO, classes="title")    #AI

def GetNetworkInterfaces():
    NetworkInterfaceOutput = subprocess.check_output(
    ("ls /sys/class/net | grep -v lo"),
    shell=True,
    text=True
    )
    NetworkInterfaces = NetworkInterfaceOutput.splitlines
    return(NetworkInterfaces)


class StartScreen(Screen):
    def compose(self):
        yield Logo()
        with Container(id="button1area"):          #AI Told me Abaut Containers while Debuging (Noted how it Works in the Obsidian Vault)
            yield Button("Start",classes="button1", id="Start")
            yield Button("Exit",classes="button1", id="Exit")
    def on_button_pressed(self, event: Button.Pressed) -> None: #AI Helped me how Buttons Work and told me hwo to switch screens
        if event.button.id == "Start":                          #(Noted how it Works in the Obsidian Vault)
            self.app.push_screen(SeconndScreen())               #
        if event.button.id == "Exit":                           #
            self.app.exit()                                     #

class SeconndScreen(Screen):
    BINDINGS = [                                                #AI Helped me with the Bindings (Noted how it Works in the Obsidian Vault)
        Binding("left", "prev_tab", "Previous step"),           #
        Binding("right", "next_tab", "Next step"),              #
        Binding("up", "focus_previous", "Focus previous"),      #
        Binding("down", "focus_next", "Focus next"),            #
    ]
    def compose(self):
        yield Logo()
        with TabbedContent(classes="Installation"):
            with TabPane("Locale", classes="InstallationTabs"):
                with Container(id="button2area"):
                     yield Label ("Test")
            with TabPane("Device Selection", classes="InstallationTabs"):
                with Container(id="button2area"):
                    yield Label("[#5c6a72]On Which Devive do you want to Install Apple Puff?[/#5c6a72]",classes="DevSecText DevSec")
                    yield Label("[#F85552]!THE WHOLE DEVICE WILL BE EREASED![/#F85552]",classes="DevSecText DevSec")
                    # lsblk -o NAME,MODEL,SIZE ausgabe trennen so das jede zeile ein eintrag in einem array ist. So viele wie dann im array ist so viele macht es dann als yield
                    # DiskNumber = 0
                    # for i in Disks:
                    #   yield Label(Disk[DiskNumber])
                    #   DiskNumber + 1
                    diskoutput = subprocess.check_output(           #AI corrected my Idea (Noted how it Works in the Obsidian Vault)
                        ["lsblk", "-dn", "-o", "NAME,MODEL,SIZE"],  #
                        text=True                                   #
                    )                                               #
                    Disks = diskoutput.splitlines()                 #
                    with Center():                                  # Ai Told me about Center (Noted how it Works in the Obsidian Vault)
                        with RadioSet(classes="RadioSetDisk"):
                            for disk in Disks:
                                yield RadioButton(disk)
                    #yield Select(((line, line) for line in Disks),
                    #classes="DevSec SelectDisk"
                    #)
            with TabPane("User Creation", classes="InstallationTabs"):
                with Container(id="button2area"):
                    yield Label ("Test")
            with TabPane("Network Connection", classes="InstallationTabs"):
                with Container(id="button2area"):
                    NetworkInterfaces = GetNetworkInterfaces()
                    yield Select(((Disk, Disk)for Disk in NetworkInterfaces()), id="SelectNetworkInterface")
                    @on(Select.Changed, "#SelectNetworkInterface")
                    async def interface_selected(self, event: Select.Changed) -> None: # Defenetly AI i dont know this shit
                        if event.value is Select.BLANK:
                            return

                        SSIDs = [("DHCP", "dhcp"), ("Static", "static")]
                        existing = self.query("#SSID Select")
                        if existing:
                            existing.first(Select).set_options(SSIDs)
                        else:
                            await self.query_one("#button2area", Container).mount(
                                Select(SSIDs, prompt="Choose IP mode", id="second_select")
                            )
                    

            with TabPane("Software", classes="InstallationTabs"):
                with Container(id="button2area"):
                    yield Label ("Test")
            with TabPane("Summary", classes="InstallationTabs"):
                with Container(id="button2area"):
                    yield Label ("Test")  

        def on_mount(self) -> None:                                             #AI
            self.query_one(TabbedContent).query_one(Tabs).can_focus = False     #AI

        def action_prev_tab(self) -> None:                                      #AI
            self.query_one(TabbedContent).query_one(Tabs).action_previous_tab() #AI (Noted how it Works in the Obsidian Vault)

        def action_next_tab(self) -> None:                                      #AI
            self.query_one(TabbedContent).query_one(Tabs).action_next_tab()     #AI (Noted how it Works in the Obsidian Vault)




class ArchInstaller(App):
        CSS_PATH = "Stylesheet.tcss"
        BINDINGS = [                                            #AI helped me with Bindings (Noted how it Works in the Obsidian Vault)
        Binding("left", "focus_previous", "Focus previous"),    # 
        Binding("right", "focus_next", "Focus next"),           #
        Binding("up", "focus_previous", "Focus previous"),
        Binding("down", "focus_next", "Focus next"),
        ]
        def on_mount(self) -> None:
            self.push_screen(StartScreen())

        # Arrowkeys for Navigation (Original Keys)
        #def _on_key(self, event):
        #    match event.key:
        #        case "down":
        #            self.action_focus_next()
        #        case "up":
        #            self.action_focus_previous()
    
if __name__ == "__main__":
    app = ArchInstaller()
    app.run()                       