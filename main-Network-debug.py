import os
from textual.binding import Binding
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static, Button, Label, TabbedContent, TabPane, RadioButton, RadioSet, Tabs, Select, Input
from textual.containers import Container, Center, Vertical, Horizontal
from textual.screen import Screen
import subprocess


#Original code

def compose(self):
    with Container(id="button2area"):
        def GetNetworksInterfaces():
            NetworkInterfaceOutput = subprocess.check_output(
            ("ls /sys/class/net | grep -v lo"),
            text=True
            )
            NentworkInterfaces = NetworkInterfaceOutput.splitlines
            return(NentworkInterfaces)
#i have no idea what trash im turning into garbage 
        yield Select(()for Disk in GetNetworksInterfaces())         
        @on(Select.Changed)                                         #checked how to get the selection with AI
        def select_changed(self, event: Select.Changed):    #
            NetworkInterface=event.value
            def NetworkInterfaceStatus(NI):
                NetworkInterfaceStatusOutput = subprocess.check_output("cat /sys/class/net/",NI,"/operstate", text=True)
                if NetworkInterfaceStatusOutput == "up":
                    return(True)
                elif NetworkInterfaceStatusOutput == "down":
                    return(False)
                else:
                    return("Something went Wrong (Maybe your PC is Garbage)")
            if NetworkInterfaceStatus(event.value) == True:
                yield Label("Network Interface Status:[#8DA101]Conected[/#8DA101]")
            elif NetworkInterfaceStatus(event.value) == False:
                if "en" in event.value:
                    yield Label("Wirred Network Interface Status:[#F85552]Disconected[/#F85552]")
                                        # make a recheck function executed by a button press
                def AvailableSSID(NetworkInterface):
                    subprocess.run(["iwctl", "station", NetworkInterface, "scan"])
                    OutputSSIDs = subprocess.run(["iwctl", "station", NetworkInterface, "get-networks"], text=True)
                    SSIDs = OutputSSIDs.splitlines
                    return(SSIDs)
                yield Select(()for SSID in AvailableSSID(NetworkInterface))
                @on(Select.Changed)
                def select_changed(self, event: Select.Changed):
                    SSID = event.value
                    yield Input(placeholder="Enter Password", id="Password")
                    yield Label("Press Enter to Submit")
                    def on_input_submitted(self, event: Input.Submitted):
                        value = event.value
                        self.query_one("#Password", Input).value
                        WLANOutput = subprocess.check_output(["iwctl", "--passphrase", event.value,"station", NetworkInterface, "connect", SSID], text=True)
                        yield Label(WLANOutput)    



#edited

def compose(self):
    with Container(id="button2area"):
        yield Select(()for Disk in GetNetworkInterfaces())         
        @on(Select.Changed)                                         #checked how to get the selection with AI
        def select_changed(self, event: Select.Changed):    #
            NetworkInterface=event.value
            def NetworkInterfaceStatus(NI):
                NetworkInterfaceStatusOutput = subprocess.check_output("cat /sys/class/net/",NI,"/operstate", text=True)
                if NetworkInterfaceStatusOutput == "up":
                    return(True)
                elif NetworkInterfaceStatusOutput == "down":
                    return(False)
                else:
                    return("Something went Wrong (Maybe your PC is Garbage)")
            if NetworkInterfaceStatus(event.value) == True:
                yield Label("Network Interface Status:[#8DA101]Conected[/#8DA101]")
            elif NetworkInterfaceStatus(event.value) == False:
                if "en" in event.value:
                    yield Label("Wirred Network Interface Status:[#F85552]Disconected[/#F85552]")
                                        # make a recheck function executed by a button press
                def AvailableSSID(NetworkInterface):
                    subprocess.run(["iwctl", "station", NetworkInterface, "scan"])
                    OutputSSIDs = subprocess.run(["iwctl", "station", NetworkInterface, "get-networks"], text=True)
                    SSIDs = OutputSSIDs.splitlines
                    return(SSIDs)
                yield Select(()for SSID in AvailableSSID(NetworkInterface))
                @on(Select.Changed)
                def select_changed(self, event: Select.Changed):
                    SSID = event.value
                    yield Input(placeholder="Enter Password", id="Password")
                    yield Label("Press Enter to Submit")
                    def on_input_submitted(self, event: Input.Submitted):
                        value = event.value
                        self.query_one("#Password", Input).value
                        WLANOutput = subprocess.check_output(["iwctl", "--passphrase", event.value,"station", NetworkInterface, "connect", SSID], text=True)
                        yield Label(WLANOutput)    



                        