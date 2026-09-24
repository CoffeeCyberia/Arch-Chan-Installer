from textual.app import App, ComposeResult
from textual import on
from textual.widgets import Label, Select, TabbedContent, TabPane


class DependentSelectApp(App):
    DEFAULT_CSS = """
    #second-select {
        display: none;
        margin-top: 1;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent(classes="Installation"):
            with TabPane("Locale", classes="InstallationTabs"):
                yield Label("Wähle zuerst eine Kategorie:")

                yield Select(
                    options=[
                        ("Obst", "fruits"),
                        ("Gemüse", "vegetables"),
                        ("Burger", "Burger")
                    ],
                    id="first-select",
                )

                yield Select(
                    options=[],
                    id="second-select",
                    prompt="Wähle ein Produkt...",
                )

    @on(Select.Changed, "#first-select")
    def handle_selection(self, event: Select.Changed) -> None:
        second_select = self.query_one("#second-select", Select)

        # Auswahl gelöscht
        if event.value == Select.NULL:
            second_select.styles.display = "none"
            second_select.update_options([])
            return

        if event.value == "fruits":
            new_options = [
                ("Apfel", "apple"),
                ("Banane", "banana"),
                ("Erdbeere", "strawberry"),
            ]

        elif event.value == "vegetables":
            new_options = [
                ("Karotte", "carrot"),
                ("Brokkoli", "broccoli"),
                ("Spinat", "spinach"),
            ]

        else:
            new_options = []

        second_select.set_options(new_options)
        second_select.value = Select.NULL
        second_select.styles.display = "block"


if __name__ == "__main__":
    DependentSelectApp().run()