from textual.app import App
from textual.widgets import Button, Welcome , TabbedContent, TabPane, Label, Select
from textual.containers import Container
from textual import on

class Test(App):
    DEFAULT_CSS = """
    #SSID-Select {
        display: none;
        margin-top: 1;
    }
    """
    def compose(self):
        NetworkInterfaces = ["Disk0", "Disk1", "Disk2"]
        with TabbedContent(classes="Installation"):
            with TabPane("Network Connection", classes="InstallationTabs"):
                with Container(id="button2area"):
                        
                    yield Select(((Disk, Disk)for Disk in NetworkInterfaces), id="SelectNetworkInterface")
                    yield Select(options=[], id="SSID-Select")
                    @on(Select.Changed, "#SelectNetworkInterface")
                    def handle_selection(self, event: Select.Changed) -> None:
                        first_select = event.select
                        second_select = self.query_one("#second-select", Select)

                        if event.value == Select.BLANK:
                            second_select.styles.display = "none"
                            return

                        if event.value == "fruits":
                            new_options = [("Apfel", "apple"), ("Banane", "banana"), ("Erdbeere", "strawberry")]
                        elif event.value == "vegetables":
                            new_options = [("Karotte", "carrot"), ("Brokkoli", "broccoli"), ("Spinat", "spinach")]
                        else:
                            new_options = []

                        second_select.update_options(new_options)
                        second_select.value = Select.BLANK
                        second_select.styles.display = "block"

                    test = '''           
                    yield Button("Hello",id="Start")
                    def on_button_pressed(self, event: Button.Pressed):
                        async def on_Select_Changed(self) -> None:
                            await self.mount(Label("Test"))
                            self.query_one(Button).label = "yes"
                    yield Label("Hello")'''   

if __name__ == "__main__":  
    app = Test()   
    app.run()