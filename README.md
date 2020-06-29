# python-contextmenu
Very simple python script for adding a compiled python program to the context menu.

---

# Usage

Add "contextmenu.py" to the same folder as your project.

### Commands:

```py
import contextmenu

contextmenu.filemenu().add() # Add python program to file context menu
contextmenu.filemenu().remove() # Remove python program from file context menu

contextmenu.foldermenu().add() # Add python program to folder context menu
contextmenu.foldermenu().add() # Remove python program from folder context menu
```

<hr width=50>

### Optional Arguments:

```py
class filemenu:
    def add(self, text: str=None, key_name: str=None, target_file: str=None, icon: str=None, use_async: str=False):
    def remove(self, key_name: str=None, target_file: str=None, use_async=False):

class foldermenu:
    def add(self, text: str=None, key_name: str=None, target_file: str=None, icon: str=None, use_async: str=False):
    def remove(self, key_name: str=None, target_file: str=None, use_async=False):
```

