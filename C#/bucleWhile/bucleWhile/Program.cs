namespace bucleWhile
{
    internal class Program
    {




        static void Main(string[] args)
        {
            UseBreake();
            UseContinue();
            UseDoWhile();


        }

        private static void UseBreake()
        {
            int i = 1;
            Console.WriteLine("          Uso de break");

            while (i < 10)
            {
                if (i == 5)
                {
                    break;

                }

                Console.WriteLine(i);
                i++;


            }



        }


        private static void UseContinue()
        {
            int i = 1;
            Console.WriteLine("\n\n          Uso de continue");

            while (i < 10)
            {
                if (i == 5)
                {
                    i++;
                    Console.WriteLine("\n(Se uso el Continue y se salto el 5)\n");

                    continue;
                   

                }

                Console.WriteLine(i);
                i++;


            }
        }

        private static void UseDoWhile() 
        { 
            int n = 10;
            Console.WriteLine("\n\n          Uso de Do While");
            do
            { 
                Console.WriteLine(n);
                n++;
            
            } while (n < 5);


        }








    }
}