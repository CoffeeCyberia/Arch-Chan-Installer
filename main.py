from textual.app import App
from textual import events


class ArchChan(App):
    pass

    def on_mount(self) -> None:
        self.screen.styles.background = "#0a141c"

ArchChan().run()