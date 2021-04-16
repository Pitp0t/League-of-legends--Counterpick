from bs4 import BeautifulSoup
import requests




print('Escribí el nombre del matchup separado por una coma:')
champion = input('>')
cadena = champion.lower().replace(' ','').replace('vs',',').split(',')

while True:
    print('Escribí el rol: middle, top, bot, jg')
    rol = input('>')
    if rol == 'middle' or rol == 'top' or rol == 'bottom' or rol == 'jg':
        break
    if rol =='mid':
        rol = 'middle'
        break
    if rol == 'adc' or 'rol' == 'sup' or rol == 'suport':
        rol = 'bottom'
        break
    else:
        print('Rol mal escrito pana')
    

        

html_text = requests.get(f'https://www.counterstats.net/league-of-legends/{cadena[0]}/vs-{cadena[1]}/{rol}/all').text
soup = BeautifulSoup(html_text, 'lxml')
all_champ = soup.find_all('div', class_ ='fifth-col col')
print('            ')
for stat in range(2, len(all_champ)):
    name = all_champ[stat].find('h3').text
    porcentajes = all_champ[stat].find_all('label')

    for porcentaje in range (0, len(porcentajes)):
        p1= porcentajes[0].text
        p2= porcentajes[1].text

    print(name)
    print(f'{cadena[0]}:{p1}')
    print(f'{cadena[1]}:{p2}')
 


