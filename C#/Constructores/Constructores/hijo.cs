using System;
using System.Collections.Generic;
using System.Text;

namespace Constructores
{
    internal class hijo : Personaconstructor
    {
    
        string madre;

        string padre;


        public hijo(string n, string co,
            string cp, int a,int e, string m, string p) : base(n, co, cp, a, e)
        {
            this.madre = m;
            this.padre = p;
        }


public void fumarmarihuana()
		{

    Console.WriteLine("esta fumando marihuana");


}

        public void Caminar(int velocidad)
        {
            base.Caminar(velocidad);
            Console.WriteLine("es un bebe y no puede caminar");
        }
public string GetMadre()
{
    return GetMadre();
}

public string GetPadre()
{
    return GetPadre();
}

public void SetMadre(string nombreMadre)
{
    this.madre = nombreMadre;
}
public void SetPadre(string nombrePadre)
{
    this.padre = nombrePadre;
}
    }
}
