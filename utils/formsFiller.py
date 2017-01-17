import yaml
import os

projectDirectory = os.getcwd()

def formsFiller():
    """Creates a dictionary for all the values to be filled in signing in signing out form"""
    with open('%s/formsFiller.yaml'%projectDirectory, 'r') as formsFiller:
        formValues = yaml.load(formsFiller)
    return formValues