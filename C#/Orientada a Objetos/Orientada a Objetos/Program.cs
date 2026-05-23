using System.IO.Pipes;

namespace Orientada_a_Objetos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string nom = "Isaac Rivas";
            string colorOjos = "verde";
            string colorPelo = "negro";
            float altura = 1.0f;
            int edad = 18;

            Persona humano = new Persona(nom, colorOjos, colorPelo, altura, edad);

            humano.Hablar();
            humano.Caminar(20);


            Console.WriteLine("La persona se llama: "+ humano.getNombre(nom));
            Console.WriteLine("Su color de pelo es: "+ humano.getColorPelo(colorPelo));
            Console.WriteLine("El color de ojos es: " + humano.getColorOjos(colorOjos));
            Console.WriteLine("Altura: " + humano.getAltura(altura));
            Console.WriteLine("Su edad es: " + humano.getEdad(edad));



            String no = "Damian";
            String colorOjo = "negro";
            String colorPel = "azul";
            float altur = 2.0f;
            int eda = 2;
            String madre = "Aide";
            String padre = "Isaac";

            Hijo h = new Hijo(no, colorOjo, colorPel, altur, eda,madre, padre );

            Console.WriteLine("\n\n\nLa persona se llama: " + h.getNombre(no));
            Console.WriteLine("Su color de pelo es: " + h.getColorPelo(colorOjo));
            Console.WriteLine("El color de ojos es: " + h.getColorOjos(colorPel));
            Console.WriteLine("Altura: " + h.getAltura(altur));
            Console.WriteLine("Su edad es: " + h.getEdad(eda));
            Console.WriteLine("Su Mama es: " + h.getMadre());
            Console.WriteLine("Su Papa es: " + h.getPadre());


            h.Caminar(12);
            h.Hablar();

        }



    }

}
