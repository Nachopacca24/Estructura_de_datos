# Geet

Geet is an educational git alternative, developed to understand git's internals.


## Installation

First, clone the repository and `cd` into it:
> `$ git clone https://github.com/Tortolala/geet.git`  
> `$ cd geet`

Then you might want to create a new virtual environment for the proyect:
> `$ mkdir venv`  
> `$ python3 -m venv venv`  
> `$ source venv/bin/activate`  

Once your new environment is activate, install the required dependencies by executing:
>`$ pip install -r requirements.txt`


To be able to run the *geet* command in your terminal, you need to create an alias in your `.bash_profile` or `.zshrc` file (example with **zsh** provided).


### Zsh

In your `.zshrc` file, add the following line and save the changes:  
> `alias geet='python {path-to-your-repo}/geet/main.py'`

After restarting your terminal, you should be able to execute:  

> `$ geet`  

And receive an output like this:   
<pre>
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  banner
  commit
  init
  log
  status              
</pre>

...and voilà.
