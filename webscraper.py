import bs4 
import requests
import lxml


result = requests.get('https://spacescoop.org/en/words/')

soup = bs4.BeautifulSoup(result.text,"lxml")




def word(num):

    word_of_day = soup.select('.mb-3')[num].getText()

    definition = word_of_day.split(' ')


    final_def = []

    for item in definition:
            if (item != ''):
                final_def.append(item)

    fword = final_def[0]
    



def define(num):

    word_of_day = soup.select('.mb-3')[num].getText()

    definition = word_of_day.split(' ')


    final_def = []

    for item in definition:
            if (item != ''):
                final_def.append(item)

    rest = final_def[1:]

    str1 = ' '

    for x in rest:
            str1 += x + ' '

    print(str1)

    
        

    




        

