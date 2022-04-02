from flask import flash

def isRequired(field, name):
    if field == "":
        flash('El ' + name + ' es obligatorio')
        return False
    
    return True