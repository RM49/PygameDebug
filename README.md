# PygameDebug
Make adding debug information to pygame screen easier  
"Pygame main" shows the module being used, "PygameDebug" being the module  
Code comments show usage  
main snippets as follows  
```
# initialise debug, pass screen, colour, fontsize
debug = PygameDebug.Debug(screen, (0, 255, 0), 24)

# placeholder variables, can be changed and will be updated when .Update called
x = 1
y = 2
z = "text"

# update and format as seen
debug.Update(("X", x), ("Y", y), ("Z", z)) # each brackets contain the text to show in the debug and the variable to show

```

Looks something like this:  
![image](https://github.com/RM49/PygameDebug/assets/108128974/839df021-4bd8-45be-a901-8b98238a0dd1)
