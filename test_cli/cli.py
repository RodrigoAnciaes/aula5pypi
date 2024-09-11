from datetime import date
import babel.numbers
import babel.dates
import babel.lists
import gettext

if __name__ == '__main__':
    gettext.bindtextdomain('cli', 'locale')
    gettext.textdomain('cli')
    _ = gettext.gettext
    today = date.today()
    print(babel.dates.format_date(today))

    number = 240000000000.32212
    print(babel.numbers.format_decimal(number))

    name = input(_('Input your name: '))
    print(_('Hello {}').format(name))