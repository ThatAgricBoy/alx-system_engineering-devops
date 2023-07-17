# Debugging

> > With great power comes great responsibilities

The user root is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the root user, as if you fat finger a command and for example run rm -rf /, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the root user can do, just need to use a specific command that you need to discover.

