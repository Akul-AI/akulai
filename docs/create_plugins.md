Make sure you have set up the program with either manual installation or by using one of the scripts provided before following this tutorial.

# AkulAI Plugins

The AkulAI class allows for the use of plugins to extend its functionality. Plugins can be written in Python, Perl or JavaScript and are located in the `plugins` directory.

## Creating a Plugin
To create a plugin, simply create a new folder in the "plugins" directory. Add a file in it. The file should be named `main` and the file extension of either .py, .pl, or .js.

Next, create a file in your sub-directory called `plugin.info`. It should look something like this:

```
author: John Doe
dependencies: requests, pandas
description: Lorem ipsum di olor nulla quis lorem ut libero malesuada feugiat. This plugin.info file is an example. See the akulai_plugins repository for more examples.
```

The dependencies may vary based on your project. Note that when listing the dependencies, list them by the name you installed them. For example, if you installed a dependency with `pip install py-example`(note that this is an example, and applies to all languages), but imported it with `import example`, you would still list the dependency `as py-example`. If you have no dependencies required to be installed, just leave it blank. 

## Python Plugins
Python plugins should be written as a function called `handle()` with one parameter, `command`, which is the text of what the user said. It should return the text of AkulAI would like to say to the user.

Here is an example of a Python plugin that says "Hello, World!" when the user says "hello":

``` python
def handle(command):
    if "hello" in command:
        return "Hello there!"
```
## Javascript Plugins
JavaScript plugins should read from the commandline and write to stdout using console.log().

Here is an example of a JavaScript plugin that says "Hello, World!" when the user says "hello":

``` javascript
command = ""
if(process.argv.length > 2){
    command = process.argv[2]
}
if (command.indexOf("hello") !== -1){
    console.log("Hello there!")
}
```
If you want to check for multiple words, you can use the `.indexOf()` method multiple times and use logical operators `(&&, ||, etc)` to check if multiple conditions are met.

It's important to note that `.indexOf()` is not the only way to check if a string contains a specific substring. you can use other methods such as `.includes()`, `.search()`, `RegExp`, etc.

For example, you can use `.includes()` instead of `.indexOf()`, like this:

``` javascript
if (command.includes("hello")){
    console.log("Hello there!")
}
```
or you can use `RegExp` to check if a string matches a specific pattern, like this:

``` javascript
let match = command.match(/hello/);
if (match) {
    console.log("Hello there!")
}
```
It all depends on your plugin and preference.

Keep in mind that when making plugins which require packages, the `node_modules` directory and the `package.json` file belong in the root directory.

## Perl Plugins

Here is an example of a Perl plugin:

``` perl
#!/usr/bin/perl

my $command = shift();
if($command=~/hello/){
    print("Hello there!\n");
}
```
Perl plugins should read from the commandline and write to stdout using print(). This example uses the command variable to check if the command contains the word "hello" and if true, print a response for AkulAI to read.

## Using a Plugin
Once a plugin has been created, it will automatically be loaded and available for use when the `AkulAI` class is instantiated. The `AkulAI` class will search for any files with the extensions of ".py" or ".js" in the "plugins" directory, and will add them to the list of available plugins.

Plugins are all currently executed every time an utterance is detected.

For example, if you have a plugin that says "Hello, World!" when the user says "hello", you can test it by saying "hello" and the response should be "Hello there!"
