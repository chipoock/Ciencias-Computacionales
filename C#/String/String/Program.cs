namespace String
{
    internal class Program
    {
        static void Main(string[] args)
        {
            MetodoSubString();
            RecorridoStrings();
            MetodoIndexOf();
            MetodoToLowerToUpper();
            MetodoPad();

        }


        private static void MetodoSubString() {
            Console.WriteLine("------ METODO SUBSTRING ------");
            string nombre = "Isaac Rivas \n";
            string Apellido = nombre.Substring(6);
            Console.WriteLine(Apellido);

            string nombre2 = "Isaac Rivas Orientada a Objetos";
            string cadenaCompleta = nombre2.Substring(6, 5); //Inicio y final del dato que quieres obtener de la cadena
            Console.WriteLine(cadenaCompleta);

        }

        private static void RecorridoStrings() {
            Console.WriteLine("----- METODO RECORRIDO STRING -----");

            string nombre = "* Isaac de Jesus Rivas Garcia *";

            foreach (char c in nombre) {
                if (c != '*') {
                    Console.Write(c);
                }

            }

        }

        private static void MetodoIndexOf() {
            Console.WriteLine("\n\n ----- METODO INDEXOF ----- ");
            string nombre = "Sistemas Operativos";
            int posicion1 = nombre.IndexOf("Operativos");


            Console.WriteLine(posicion1);
            int posicion2 = nombre.IndexOf("Operativos", 10); //Regresa -1 
            Console.WriteLine(posicion2);


        }


        private static void MetodoToLowerToUpper() {
            Console.WriteLine("\n\n----- METODO TO LOWER AND TO UPPER -----");
            string nombre, minus, mayus;

            nombre = "Isaac Rivas";
            minus = nombre.ToLower();
            mayus = nombre.ToUpper();
            Console.WriteLine(mayus);
            Console.WriteLine(minus);

        }


        private static void MetodoPad() {
            Console.WriteLine("\n\n----- METODO PAD -----"); //Agrega Ceros en un string para mantener el orden en las bases de datos
            string apellido, codigo;
            apellido = "Rivas";
            codigo = "219201686";

            apellido = apellido.PadRight(10,'x');
            codigo = codigo.PadLeft(12, '0');
            Console.WriteLine(apellido);
            Console.WriteLine(codigo);




        }

    }


}

