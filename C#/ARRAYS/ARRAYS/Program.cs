namespace ARRAYS
{
    internal class Program
    {
        static void Main(string[] args)
        {

            string[] miArray = new string[4] { "Isaac", "Juan", "Aide", "Michel" };
          

            ArrayClasico(miArray);
            ArrayForeach(miArray);

           
        }

        static void ArrayClasico(string[] miArray)
        {
            Console.WriteLine("-------ArrayClasico---------");

            Console.WriteLine(miArray[2]);
            miArray[2] = "pancho";
            Console.WriteLine(miArray[2] + "\n\n");
            for (int i = 0; i < miArray.Length; i++)
            {
                Console.WriteLine(miArray[i]);

            }
        }

        static void ArrayForeach(string[] miArray) {
            Console.WriteLine("------------FOREACH---------------");
            foreach (string mi in miArray)
            {
                Console.WriteLine(mi);

            }

        }
    }
}
