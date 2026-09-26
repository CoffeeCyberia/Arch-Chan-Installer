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
from textual.theme import Theme
import subprocess, re





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

ConnectionStatusButton = ""

my_theme = Theme(
    name="my-theme",
    primary="#93B259",
    )

class Logo(Label):                                 #AI (Noted how it Works in the Obsidian Vault)
    def __init__(self) -> None:                    #AI
        super().__init__(LOGO, classes="title")    #AI

def GetNetworkInterfaces():
    return sorted(n for n in os.listdir("/sys/class/net") if n != "lo")


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
    selected_interface: str | None = None
    entered_password: str | None = None
    selected_ssid: str | None = None
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
                    yield Select(((NetInt, NetInt)for NetInt in NetworkInterfaces), id="SelectNetworkInterface", classes="select1")
                    yield Select(options=[], id="SSID-Select", classes="select1")
                    yield Input(placeholder="Enter Password", id="EnterWLANPassword", password=True)
                    yield Label(ConnectionStatusButton, id="ConnectionStatus")
                    yield Button("Connect", id="ConnectWLANButton", classes="button1")
                    

                    test= """
                    def network_interface_selected(self, event: Select.Changed) -> None:
                        if event.value == Select.NULL:
                            return
                        self.selected_interface = event.value
                        subprocess.run(
                        ["iwctl", "station", self.selected_interface, "scan"],
                        check=True
                        )
                    """
                    
                    
                    test= """
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
                            """
                    

            with TabPane("Software", classes="InstallationTabs"):
                with Container(id="button2area"):
                    yield Label ("Test")
            with TabPane("Summary", classes="InstallationTabs"):
                with Container(id="button2area"):
                    yield Label ("Test")  


    @on(Select.Changed, "#SelectNetworkInterface")
    def on_network_interface_selected(self, event: Select.Changed) -> None:
        SSID_select = self.query_one("#SSID-Select", Select)
        Password_Input = self.query_one("#EnterWLANPassword", Input)
        Connect_Button = self.query_one("#ConnectWLANButton", Button)
        if event.value == Select.BLANK:
            SSID_select.styles.display = "none"
            SSID_select.update_options([])
            Password_Input.styles.display = "none"
            Connect_Button.styles.display = "none"
            return
        
        if "wl" in event.value:
            self.selected_interface = event.value

            #if /sys/class/net/Networkinterface/operstate is up label: Internet Connected, if down the run the connection thing
             
            subprocess.run(
            ["sudo", "iwctl", "station", event.value, "scan"]
            )
            output = subprocess.check_output(
                ["sh", "-c", r"""iwctl station "$1" get-networks | sed 's/\x1b\[[0-9;]*m//g' | tail -n +5 | sed 's/^[ >]*//; s/ \{2,\}.*//' | grep -v '^$'""", "sh", event.value],
                text=True,
            )
            new_options = [line for line in output.splitlines() if line.strip()]

            SSID_select.set_options((s, s) for s in new_options)
            SSID_select.clear
            SSID_select.styles.display = "block" 
            Password_Input.clear
            Password_Input.styles.display = "block"
            Connect_Button.styles.display = "block"
            

        elif "en" in event.value:
            print()
            #if network device is up label: Internet Connected, if down the: Internet is not connected

        else:
            new_options = ["NotApple", "NotDurum"]
                    


    @on(Select.Changed, "#SSID-Select")
    def on_ssid_selected(self, event: Select.Changed) -> None:
        self.selected_ssid = event.value

    @on(Input.Changed, "#EnterWLANPassword")
    def handle_selection(self, event: Input.Changed) -> None:
        self.entered_password = event.value
        

    def on_password_changed(self, event: Button.Pressed,):
        if event.button.id == "ConnectWLANButton":
            ConnectionStatus = self.query_one("#ConnectionStatus", Label)
            ConnectionStatus.styles.display = "none"
            ConnectionStatus.styles.color = "none"
            interface = self.selected_interface
            password = self.entered_password
            ssid = self.selected_ssid
            password_quoted = '"' + password + '"'
            ssid_quoted = '"' + ssid + '"'
            ConnectSuccess = '"' + "Success: Connected!" + '"'
            ConnectFail = '"' + "Failure: Could not connect." + '"'
            WLANStatus = subprocess.check_output(
                ["sudo", "iwctl","--passphrase", password_quoted, "station", interface, "connect", ssid_quoted, "&&", "echo", ConnectSuccess, "||", "echo", ConnectFail],
                check=True,
                shell=True
                )
            if WLANStatus == ConnectSuccess:
                ConnectionStatusButton = "Connection Established"
                ConnectionStatus.styles.display = "block"
                ConnectionStatus.styles.color = "#8DA101"

            elif WLANStatus == ConnectFail:
                ConnectionStatusButton = "Connection Failed"
                ConnectionStatus.styles.display = "block"
                ConnectionStatus.styles.color = "#F85552"
            else:
                ConnectionStatusButton = "something went wrong"
                ConnectionStatus.styles.display = "block"
                ConnectionStatus.styles.color = "#F85552"

    

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