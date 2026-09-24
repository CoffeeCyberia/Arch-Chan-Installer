from textual.app import App, ComposeResult
from textual import on
from textual.widgets import Label, Select, TabbedContent, TabPane
from textual.screen import Screen
from textual.containers import Container
import subprocess

def GetNetworkInterfaces():
    NetworkInterfaceOutput = subprocess.check_output(
    ("ls /sys/class/net | grep -v lo"),
    shell=True,
    text=True
    )
    NetworkInterfaces = NetworkInterfaceOutput.splitlines
    return(NetworkInterfaces)


DEFAULT_CSS = """
#SSID-Select {
    display: none;
    margin-top: 1;
}
"""
class ArchInstaller(App):
    class StartScreen(Screen):
        def compose():
            with TabPane("Network Connection", classes="InstallationTabs"):
                with Container(id="button2area"):
                    interfaces = GetNetworkInterfaces()   # no second ()
                    yield Select(
                        ((iface, iface) for iface in interfaces),
                        id="SelectNetworkInterface",
                    )
                    yield Select(options=[], id="SSID-Select", prompt="Choose SSID...")

# on class level, next to compose():
@on(Select.Changed, "#SelectNetworkInterface")
def handle_interface(self, event: Select.Changed) -> None:
    ssid_select = self.query_one("#SSID-Select", Select)

    if not isinstance(event.value, str):      # selection cleared
        ssid_select.styles.display = "none"
        ssid_select.set_options([])
        return

    new_options: list[tuple[str, str]] = []   # always defined

    if event.value.startswith("wl"):          # wifi
        self.selected_interface = event.value
        subprocess.run(
            ["iwctl", "station", self.selected_interface, "scan"],
            check=True,
        )
        # TODO: parse `iwctl station <if> get-networks` for real SSIDs
        new_options = [("SSID1", "SSID1"), ("SSID2", "SSID2")]

    elif event.value.startswith("en"):        # ethernet, nothing to pick
        ssid_select.styles.display = "none"
        return

    ssid_select.set_options(new_options)
    ssid_select.styles.display = "block"

if __name__ == "__main__":
    app = ArchInstaller()
    app.run()                       