namespace nulos2
{
    internal class Program
    {
        static void Main(string[] args)
        {

            HasValue();
            MetodoValue();
            MetodoGetValueOrDefault();

        }

        static void HasValue()
        {
            int? i = null;

            Console.WriteLine(" HAS VALUE");

            if (i.HasValue)
                Console.WriteLine("Tiene valor: " + i.Value);
            else
                Console.WriteLine("tiene valor NULL");


        }

        static void MetodoValue() {
            Console.WriteLine("\n\n Metodo Value");
            int? x = 5;
            int y = 0;
            try
            {
                y = x.Value;
                Console.WriteLine("El valor de Y es: " + y);
            } catch { Console.WriteLine(" Operacion no valida"); }
        }

        static void MetodoGetValueOrDefault() {
            Console.WriteLine("Get Value Or Default");
            int? i = null;
            i = 20;
            bool? x = null;
            x = true;
            Console.WriteLine(i.GetValueOrDefault());
            Console.WriteLine(x.GetValueOrDefault());


        }
    }
}
