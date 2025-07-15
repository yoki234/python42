class Menu:

    def main():
        value = input('поиск:\n1-трэк\n2-исполнитель\n3-альбом ')
        match value:
            case('1'):
                track = input('ввести название трека')
            
            case('2'):
                artist = input('ввести название исполнителя')
            case('3'):
                album = input('введите название альбома ')

class Migrate:
    def __init__(self):
        self.path = '////'

    def get_track(self):
        try:
            with sql.connect(self.path) as db:
                cur = db.cursor()
                cur.execute('''''')

                date = cur.fetchell





1
