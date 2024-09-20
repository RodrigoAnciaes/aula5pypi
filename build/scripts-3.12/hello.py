#!python
import dev_abertoV2
import babel.dates
import gettext
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

if __name__ == '__main__':
    date, name = dev_abertoV2.hello()
    print(_('Último commit feito em: {} por {}').format(babel.dates.format_date(date), name))
