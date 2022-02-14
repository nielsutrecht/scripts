# Assortment of scripts and tools

## Install

Clone the repositor somewhere and then add it to your path.

### MacOS

* Open the .bash_profile file in your home directory (for example, /Users/your-user-name/.bash_profile) in a text editor.
* Add export PATH="your-dir:$PATH" to the last line of the file, where your-dir is the directory you want to add.
* Save the .bash_profile file.
* Restart your terminal.

### Linux

* Open the .bashrc file in your home directory (for example, /home/your-user-name/.bashrc) in a text editor.
* Add export PATH="your-dir:$PATH" to the last line of the file, where your-dir is the directory you want to add.
* Save the .bashrc file.
* Restart your terminal.

## Tools

* ksecret - tool to list and display kubernetes secrets
* ghook - Git (pre-)commit tools to insert issue IDs and/or check for them based on the current branch or a regex

## Usage

### ghook

Git hooks are stored in the .git/hooks directory of your repository and local to your machine and the repository. By default
they contain samples that you can use by just removing the .sample from the filename. Git finds them based on the filename. So 
for example the commit message hook runs the commit-msg script.

I generally just use those scripts as a launch point to run the ghook script. So a `commit-msg` script that uses the check-message
functionality can look like this:

    #!/usr/bin/env bash
    ghook check-message "$1" "^([A-Z]{1,10}-[0-9]{1,6}).+$"

You can also let it insert the issue ID, but only succeed if you're on a feature branch:

    #!/usr/bin/env bash
    ghook expect-branch "^([A-Z]{1,10}-[0-9]{1,6}).+$" && ghook insert-branch "$1" "^([A-Z]{1,10}-[0-9]{1,6}).+$"


Make sure the commit-msg script is executable!