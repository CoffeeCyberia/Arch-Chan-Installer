# Container
A Container is a Box to store Widgets in it.

To use Containers you need the following Line
```
from textual.containers import Container
```

An Example of a Container
```
with Container(): 
	yield Label("Hello") 
	yield Button("Click me")
```

You can also have Containers in Containers. Same for Vertical and Horizontal

# Vertical and Horizontal

## Vertical
Vertical is just a Vertical Container
```
from textual.containers import Vertical
```
## Horizontal
Horizontal is a Horizontal Container
```
from textual.containers import Horizontal
```

# Center
Center is like a Container but it automaticlaly Centers things.
```
from textual.containers import Center
```
# Differences

The Differences between Container, Vertical and Horizontal

- Container
	- Container for Everything
- Vertical
	- Arranges children vertically
- Horizontal
	- Arranges children horizontally
- Center
	- Centers the children


# ScrollableContainer

As the Name Says, its a Container with a Scrollbar
```
from textual.containers import ScrollableContainer
```

Functions:
-  VerticalScroll
- Horizontal Scroll