import input 
import logger 

def join():
    name, surname, location, number = input.get_phonebook_data()
    logger.append(name, surname, location, number)
    return name, surname, location, number