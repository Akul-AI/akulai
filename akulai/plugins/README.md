# Python Plugins

The code below takes the code from the `time.py`

``` python

def handle(akulai, command):
    if command.lower() == "hello, world!":
        akulAI.speak("Hello, world!")

```

The function `handle` will be executed when the plugin is loaded by the AkulAI class. This function takes two arguments, an instance of AkulAI and the command passed in by the user. The function then checks if the command is "Hello, world!", and if it is, it calls the speak function on the AkulAI instance to speak the text "Hello, world!".

You can save this code in a file called `hello_world.py` inside the plugins directory.

Please note that the above example is a very basic one and it is not doing any error handling and assumes that all the necessary modules are imported.
It's also important to note that you can use any of the python modules and packages to handle different tasks, such as HTTP requests, file I/O, etc. inside your python plugin, however, you need to install them before using them.

# JS Plugins

The code below makes a simple "Hello, World!" application.

``` javascript
module.exports.handle = function (akulai, command) {
  if (command.toLowerCase() === "hello, world!") {
    akulAI.speak("Hello, world!");
  }
}
```

The JavaScript function `module.exports.handle` will be executed when the JavaScript plugin is loaded by AkulAI. This function takes two arguments, an instance of AkulAI and the command passed in by the user. The function then checks if the command is "Hello, world!", and if it is, it calls the speak function on the AkulAI instance to speak the text "Hello, world!".

You can save this code in a file called `hello_world.js` inside the plugins directory.

It's also important to note that you can use any of the available NodeJS packages to handle different tasks, such as HTTP requests, file I/O, etc. inside your javascript plugin, however, you need to install them before using them.
