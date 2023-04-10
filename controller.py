import model
import view

pb = model.Phonebook('phone_db.txt')
def start():
    while True:
        #print(pb.main_menu())
        choice = view.main_menu()
        match choice:
            case 1 :
                print(pb)
            case 2:
                name = input('Введите имя: ')
                phone = input('Введите телефон: ')
                comment = input('Введите комменатрий: ')
                pb.new_contact(name, phone, comment)
                view.show_message('Контакт добавлен, сохранись!')
            case 3:
                word = input('Введите имя искомого контакта: ')
                print(pb.search(word))
            case 4:
                print(pb)
                index = int(input('Введите индекс контакта, который будем изменять: '))
                name = input('Введите имя (или ENTER, чтобы оставить без изменений): ')
                phone = input('Введите телефон (или ENTER, чтобы оставить без изменений): ')
                comment = input('Введите комменатрий (или ENTER, чтобы оставить без изменений): ')
                pb.change(index-1, name, phone, comment)
                view.show_message('Контакт успешно изменен, сохранись!')
            case 5:
                print(pb)
                index = int(input('Введите индекс контакта, который будем удалять: '))
                pb.delete(index-1)
                view.show_message('Контакт успешно удален')
            case 6:
                pb.save()
            case 7:
                break
            


