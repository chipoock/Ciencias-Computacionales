using Orientada_a_Objetos;

internal class Hijo : Persona
{
    string madre;
    string padre;

    public Hijo(string nombre, string colorOjos, string colorPelo, float altura, int edad, string madre, string padre) : base(nombre, colorOjos, colorPelo, altura, edad)
    {
        this.madre = madre;
        this.padre = padre;
    }


    public String getMadre() {

        return madre;

    }


    public void setMadre(String madre)
    {
        this.madre = madre;
    }

    public override void Caminar(int velocidad) {

        base.Caminar(velocidad);
    Console.WriteLine("Es un bebe no puede caminar");
            
            }









    public String getPadre()
    {

        return padre;

    }

    public void setPadre(String padre)
    {
        this.padre = padre;
    } 






}