
personsList = []

#Cadastrar
def Register():
    qtd = int(input('Enter the number the people who will be registered: '))

    for i in range(qtd):
        person = input('Enter the name: ')
        personsList.append(person)

#Deletar
def Delete():
    name = input('Enter the name of the person to be deleted: ')

    pos = personsList.index(name)
    personsList.pop(pos)

#Atualizar
def Upadate():
    name = input('Put the name of person who you want update: ')
    pos = personsList.index(name)
    n_name = input('Now, put here the new name: ')

    for names in personsList:
        if name == names:
            personsList[pos] = n_name

#Listar pessoas
def List_people():
    print(personsList)

# Menu Principal
while True:
    print('=' * 40)
    choice = int(input('Enter you choice:\n 1 - Add Person;\n 2 - Delete Person;\n 3 - Update Person;\n 4 - List People;\n 0 - Exit.\n'))
    print('=' * 40)

    if choice == 1:
        Register()
    elif choice == 2:
        Delete()
    elif choice == 3:
        Upadate()
    elif choice == 4:
        List_people()
    elif choice == 0:
        break
    else:
        print('Invalid Choice, try again.')

with open('People.txt', 'w+') as arq:
    for name in personsList:
        arq.write(name)
        arq.write('\n')
