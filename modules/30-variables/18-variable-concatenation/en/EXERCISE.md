
Websites are constantly sending emails to their users. A common task is to automatically send a personalized email with the user's name in the header. If a database stores people's names, the task of generating the header boils down to concatenation: for example, you want to glue the string `Hello` with a string containing a user's name.

Write a program that will create the header and body of an email using ready-made variables and print the resulting strings.

Use the `first_name` and `greeting`, variables, a comma, and an exclamation point for the header. Print it in the correct order.

Use the variables `info` and `intro` for the body of the message, with the second sentence on a new line.

The result should look like this:

<pre class='hexlet-basics-output'>
Hello, Joffrey!
Here is important information about your account security.
We couldn't verify your mother's maiden name.
</pre>

Perform the task using only two `print()` statements.
