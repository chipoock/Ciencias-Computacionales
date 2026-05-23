namespace Arrays_strings
{

  
        internal class Program
        {
            static void Main(string[] args)
            {
            string[] nombreAlumnos = new string[4] { "Ricardio", "Paul thomas Anderson", "kubrick", "Hitchcok" };

                Console.WriteLine(nombreAlumnos[2]);
            nombreAlumnos[2] = "Paul thomas Anderson";

            Console.WriteLine(nombreAlumnos[2]);

            for (int i = 0; i < nombreAlumnos.Length; i++)
            {


                Console.WriteLine(nombreAlumnos[i]);

            }
            Console.WriteLine("------------------");

            foreach(string n in nombreAlumnos)
            {
                Console.WriteLine(n);
            }

            }
        }
    }