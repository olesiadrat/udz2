def checkInput(text):
        for i in text:
            if i.isdigit() == False:
                return False
        return True

print(checkInput('ggg'))