Make sure you have set up the program with either manual installation or by using one of the scripts provided before following this tutorial.

# AkulAI Plugins

The AkulAI class allows for the use of plugins to extend its functionality. Plugins can be written in both Python and JavaScript and are located in the "plugins" directory.

## Creating a Plugin
To create a plugin, simply create a new file in the "plugins" directory with the desired behavior. The file should be named with the name of the plugin and the file extension of either .py or .js.

## Python Plugins
Python plugins should be written as a function called `handle(akulai, command)` where `akulai` is an instance of the `AkulAI` class and `command` is the string of the command that the user said.

Here is an example of a Python plugin that says "Hello, World!" when the user says "hello":

``` python
def handle(akulai, command):
    if "hello" in command:
        akulai.speak("Hello, World!")
```
## Javascript Plugins
JavaScript plugins should be written as a function called `handle(akulai, command)` where `akulai` is an instance of the `AkulAI` class and `command` is the string of the command that the user said.

Here is an example of a JavaScript plugin that says "Hello, World!" when the user says "hello":

``` javascript
function handle(akulai, command) {
    if (command.indexOf("hello") !== -1) {
        akulai.speak("Hello, World!");
    } 
}
```
If you want to check for multiple words, you can use the `.indexOf()` method multiple times and use logical operators `(&&, ||, etc)` to check if multiple conditions are met.

It's important to note that `.indexOf()` is not the only way to check if a string contains a specific substring. you can use other methods such as `.includes()`, `.search()`, `RegExp`, etc.

For example, you can use `.includes()` instead of `.indexOf()`, like this:

``` javascript
if (command.includes("hello")) {
    akulai.speak("Hello, World!");
}
```
or you can use `RegExp` to check if a string matches a specific pattern, like this:

``` javascript
let match = command.match(/hello/);
if (match) {
    akulai.speak("Hello, World!");
}
```
It all depends on your plugin and preference.

Keep in mind that when making plugins which require packages, the `node_modules` directory and the `package.json` file belong in the root directory.

## Using a Plugin
Once a plugin has been created, it will automatically be loaded and available for use when the `AkulAI` class is instantiated. The `AkulAI` class will search for any files with the extensions of ".py" or ".js" in the "plugins" directory, and will add them to the list of available plugins.

A plugin can be executed by including its name in the command given to the `AkulAI` instance.

For example, if you have a plugin called "example" that says "Hello, World!" when the user says "hello", you can test it by saying "hello" and the response should be "Hello, World!"
