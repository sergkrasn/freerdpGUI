# freerdpGUI
FreerdpGUI graphical application for running xfreerdp in Linux-based operating systems

To build standalone application, pyinstaller is required, to install it, call the command.

    pip install pyinstaller

To build the application, use the command:
    
    pyinstaller freerdpgui.spec

The tool is written in ruby and requires ruby to be installed to use it. Install ruby using your systems package manager, for example.

    sudo apt install ruby

Once ruby is installed, you can install fpm using the gem tool.

    gem install fpm --user-install

If you see a warning e.g. You don't have /home/martin/.local/share/gem/ruby/2.7.0/bin in your PATH you will need to add that to your path in your .bashrc file.
...and that's it. Once the installation is complete, you're ready to use fpm. You can check it is installed and working by running:

    fpm --version
    1.14.2

# Assembling the package
Вefore assembling the package, you should run the script "package.sh" to create catologists
    
    bash package.sh
    
# Building your package

Now everything is where it should be in our package "filesystem", we're ready to start building the package itself.
Enter the following into your shell.

    ~/.gem/ruby/2.5.0/bin/fpm

After a few seconds, you should see a message to indicate that the package has been created.
