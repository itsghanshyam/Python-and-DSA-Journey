"""In this lab, you will build a User Configuration Manager that allows users 
to manage their settings such as theme, language, and notifications. You will
implement functions to add, update, delete, and view user settings."""


test_settings = {
    'theme':'dark',
    'area': 'small'
}
def add_setting(dic,pair):
    key,value = pair
    key,value = key.lower(),value.lower()
    if key in dic:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dic.update({key:value})
        return f"Setting '{key}' added with value '{value}' successfully!"



def update_setting(dic,pair):
    key,value = pair
    key,value = key.lower(),value.lower()
    if key in dic:
        dic.update({key:value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(dic,key):
    key = key.lower()
    if key in dic:
        del dic[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"
    
def view_settings(dic):
    output = "Current User Settings:\n"
    if len(dic) == 0:
        return "No settings available."
    else:
        for key,value in dic.items():
            output += f"{key.title()}: {value}\n"
        
        return output
        



print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))