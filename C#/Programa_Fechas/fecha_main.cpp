#include <iostream>
#include <cstdlib>

#include "Fecha.h"

int main() {

    using namespace std;

    Fecha fechas[12];

    short d, m, a;

    for (int i = 0; i < 12; i++) {

        cout << "Escribe una fecha en formato dd mm aaaa: ";
        cin >> d >> m >> a;

        fechas[i].set_fecha(d, m, a);
    }

    cout << endl;

    for (int i = 0; i < 12; i++) {

        for (int j = i + 1; j < 12; j++) {

            if (fechas[i] < fechas[j]) {

                cout << fechas[i]
                    << " es menor que "
                    << fechas[j]
                    << endl;
            }

            else if (fechas[i] > fechas[j]) {

                cout << fechas[i]
                    << " es mayor que "
                    << fechas[j]
                    << endl;
            }

            else if (fechas[i] == fechas[j]) {

                cout << fechas[i]
                    << " es igual a "
                    << fechas[j]
                    << endl;
            }
        }
    }

    return 0;
}