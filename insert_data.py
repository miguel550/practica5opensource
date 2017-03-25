import csv
import sys
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "practica5ftp.settings")
import django
django.setup()

from home.models import PagosARS


def is_luhn_valid(cc):
    num = list(map(int, str(cc)))
    return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0

if len(sys.argv) == 2:
    file = sys.argv[1]
    with open(file) as f:
        pagos = csv.DictReader(f)
        for pago in pagos:
            pago_m = PagosARS()
            cedula = pago_m.cedula = pago["cedula"]
            pago_m.monto = float(pago["monto"])
            if not is_luhn_valid(cedula) or '0'*len(cedula) == cedula:
                print(f'Cedula no valida: {cedula}')
            else:
                pago_m.save()
        print("Pagos importados a la base de datos!")
