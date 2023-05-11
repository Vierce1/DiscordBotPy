from googlesearch import search
from datetime import datetime
import discord


users = { 322164425002057728:"Vierce" , 879464051267223572:"Naiyvara",
    159815678508007424:"ComradeGiraffe" , 157183377089363969:"The Great Ratsby" , 238467012399988738:"GoldForce" }

names = {"Naiyvara":"Ashley" , "Vierce":"Andrew"}

# General functions
def google_search(search_term, num_results):
    for url in search(search_term, num_results=num_results):
        return url


def get_date_hour():
    today = datetime.today()
    # strip off the milliseconds then convert back to datetime
    simple_today = datetime.strptime(str(today).split('.')[0], "%Y-%m-%d %H:%M:%S")
    return simple_today


def get_user_name(interaction: discord.Interaction):
    try:
        return users[int(interaction.user.id)]
    except Exception as e:
        print("Error in get_user_name: " + str(e))
        return None

def check_user(interaction: discord.Interaction, allowed_users: []):
    user = get_user_name(interaction)
    # user and user in allowed_users will be None if not found
    return (user is not None and user in allowed_users) is True

def get_name(user_name: str):
    print("Getting name for ... " + user_name)
    try:
        return names[user_name]
    except Exception as e:
        return None

def get_used_babies(user: str, top: bool, number: int):
    # returns (name: str, score: int)
    used_names_text = open("/home/andweste/Scripts/used_names.txt", "r").readlines()
    name_list = []
    for line in used_names_text[2:]:
        index = 1 if user == "Ashley" else 2
        name = line.split(';')[0]
        name_list.append((name, line.split(';')[index].strip()))
    # sort list by score
    sorted_list = sorted(name_list, key=lambda tuple: tuple[1])
    for i in range(len(sorted_list) - number):
        sorted_list.pop()
    for s in sorted_list:
        print(s)
    return sorted_list


