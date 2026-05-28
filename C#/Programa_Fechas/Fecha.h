#ifndef FECHA_H_CUT_UDG_MX
#  define FECHA_H_CUT_UDG_MX

# include <string>
# include <iostream>

class Fecha
{
public:
    enum {
        INVALID_DAY = -1,
        INVALID_MONTH = -2,
        INVALID_YEAR = -3
    };

private:
    short dia;
    short mes;
    short annio;

public:

    Fecha() {
        dia = 27;
        mes = 9;
        annio = 2003;
    }

    Fecha(short d, short m, short a) {

        if (!set_fecha(d, m, a)) {
            dia = 27;
            mes = 9;
            annio = 2003;
        }
    }

    Fecha(const Fecha& copiaFecha) {
        this->dia = copiaFecha.dia;
        this->mes = copiaFecha.mes;
        this->annio = copiaFecha.annio;
    }

private:

    short get_dia() const {
        return dia;
    }

    bool set_dia(short d, short max = 31) {

        if (d < 1 || d > max) {
            return false;
        }

        dia = d;
        return true;
    }

    short get_mes() const {
        return mes;
    }

    bool set_mes(short m) {

        if (m < 1 || m > 12) {
            return false;
        }

        mes = m;
        return true;
    }

    short get_annio() const {
        return annio;
    }

    bool set_annio(short a) {

        if (a <= 0) {
            return false;
        }

        annio = a;
        return true;
    }

    bool biciesto(short a) const {

        if (a % 400 == 0) return true;
        if (a % 100 == 0) return false;

        return (a % 4 == 0);
    }

    short diasDelMes(short m, short a) const {

        switch (m) {

        case 2:
            return biciesto(a) ? 29 : 28;

        case 4:
        case 6:
        case 9:
        case 11:
            return 30;

        default:
            return 31;
        }
    }

public:

    std::string get_fecha(bool extra = false) const
    {
        std::string retVal;

        if (!extra) {

            retVal = std::to_string(dia);
            retVal += "/";
            retVal += std::to_string(mes);
            retVal += "/";
            retVal += std::to_string(annio);

            return retVal;
        }

        const std::string meses[] = {
            "Ene","Feb","Mar","Abr","May","Jun",
            "Jul","Ago","Sep","Oct","Nov","Dic"
        };

        retVal = std::to_string(dia);
        retVal += "/";
        retVal += meses[mes - 1];
        retVal += "/";
        retVal += std::to_string(annio);

        return retVal;
    }

    bool set_fecha(short d,
        short m = INVALID_MONTH,
        short a = INVALID_YEAR)
    {
        if (m == INVALID_MONTH || a == INVALID_YEAR)
            return false;

        if (!set_annio(a))
            return false;

        if (!set_mes(m))
            return false;

        short max_dias = diasDelMes(m, a);

        if (!set_dia(d, max_dias))
            return false;

        return true;
    }

    bool operator<(const Fecha& other) const {

        if (annio < other.annio) return true;
        if (annio > other.annio) return false;

        if (mes < other.mes) return true;
        if (mes > other.mes) return false;

        return dia < other.dia;
    }

    bool operator>(const Fecha& other) const {

        if (annio > other.annio) return true;
        if (annio < other.annio) return false;

        if (mes > other.mes) return true;
        if (mes < other.mes) return false;

        return dia > other.dia;
    }

    bool operator==(const Fecha& other) const {

        return (dia == other.dia &&
            mes == other.mes &&
            annio == other.annio);
    }
};

std::ostream& operator<<(std::ostream& salida,
    const Fecha& other)
{
    salida << other.get_fecha();
    return salida;
}

#endif