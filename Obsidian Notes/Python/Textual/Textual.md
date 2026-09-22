# main.py
## class Logo
```
class Logo(Label):
    def __init__(self) -> None:
        super().__init__(LOGO, classes="title")
```

## Bindings and Tab Management

```
BINDINGS = [
	Binding("left", "prev_tab", "Previous step"),
	Binding("right", "next_tab", "Next step"),
	Binding("up", "focus_previous", "Focus previous"),
	Binding("down", "focus_next", "Focus next"),
]


def on_mount(self) -> None:
	self.query_one(TabbedContent).query_one(Tabs).can_focus = Falsedef action_prev_tab(self) -> None:
	self.query_one(TabbedContent).query_one(Tabs).action_previous_tab()
def action_next_tab(self) -> None:
	self.query_one(TabbedContent).query_one(Tabs).action_next_tab()
```

### Bindings
For the Binding Parts go [[Bindings|here]]

### action prev_tab and next_tab

This Line says that it needs the TabbedContent Widget
``self.query_one(TabbedContent)``

This Line says that it needs the Tabs in the TabbedContent Widget
``.query_one(Tabs)``

This Line Calls the action_previus_tab function from the Tabs widget
`.action_previous_tab()``

## Why is slef used so much in textual


