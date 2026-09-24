How is a Binding Build
```
Binding(key, action, description)

Example 1:
Binding("down", "focus_next", "Focus next")
Example 2:
Binding("left", "prev_tab", "Previous step")
```

The Important Content for Example 2 is, that the action is a self made one. 
```
def action_prev_tab(self) -> None:                                      #AI
	self.query_one(TabbedContent).query_one(Tabs).action_previous_tab()
```

As you see the "prev_step" is actually called "action_prev_tab()"

The Original "prev_tab" would be "action_prev_tab()" but Textual has following rule:
```
action_<action name>
```
 
 So the we just call it by the Action Name
```
"prev_tab" -> action_prev_tab()
```

If you want to have multiple Bindings, you can do it as following:
```
BINDINGS[
	Binding("left", "prev_tab", "Previous step"), 
	Binding("right", "next_tab", "Next step"), 
	Binding("up", "focus_previous", "Focus previous"), 
	Binding("down", "focus_next", "Focus next"),
]
```

