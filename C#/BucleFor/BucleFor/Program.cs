namespace BucleFor
{
    internal class Program
    {
        static void Main(string[] args)
        {
            UseFor();
            UseForEach();

        }

        private static void UseFor() {
            Console.WriteLine("          Uso de For");

            for (int i = 0; i <=5 ; i++) {

                Console.WriteLine(i);
            
            
            }



        }

        private static void UseForEach()
        {
            Console.WriteLine("\n\n          Uso de ForEach");
            string[] nombres = { "Juan", "Isaac", "Aide", "Michel", "Ricardo" };
            
            foreach (string i in nombres)
            {

                Console.WriteLine(i);


            }



        }









    }
}
