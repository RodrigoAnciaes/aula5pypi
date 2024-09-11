#!/usr/bin/env python3
from datetime import date
import dev_abertoV2
import babel.dates
import gettext

if __name__ == '__main__':
    gettext.bindtextdomain('cli', 'locale')
    gettext.textdomain('cli')
    _ = gettext.gettext
    try:
        date, name = dev_abertoV2.hello()
    except:
        date, name = date.today(), 'Desconhecido'
    print(_('Último commit feito em: {} por {}').format(babel.dates.format_date(date), name))
