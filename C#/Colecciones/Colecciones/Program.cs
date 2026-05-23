using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;

namespace Colecciones
{
    internal class Program
    {
        static void Main(string[] args)
        {



            Pila();
            Cola();
            ListaOrdenada(); //TABLA HASH


        }


        private static void Pila()
        {

            Stack pila = new Stack();
            pila.Push(50);
            pila.Push(25);
            pila.Push(100);

            Console.WriteLine("Los elementos de la pila son: ");

            while (pila.Count > 0)
            {
                Console.WriteLine(pila.Pop());
            }


            Console.WriteLine(pila.Count);


        }


        private static void Cola() { 
            
            Console.WriteLine("\n\n---------- COLAS ----------");
            
            Queue cola = new Queue();
            cola.Enqueue(50);
            cola.Enqueue(25);
            cola.Enqueue(100);



            Console.WriteLine("Los elementos de la cola son: ");

            while (cola.Count > 0)
            {
                Console.WriteLine(cola.Dequeue());
            }


            Console.WriteLine(cola.Count);

            
        }

        private static void ListaOrdenada() {

            Console.WriteLine("\n\n---------- Hash ----------");

            SortedList listaOrdenada = new SortedList();
            listaOrdenada.Add(50, "El Valor el 2do el 1ro es la llave");
            listaOrdenada.Add(20, "Isaac Rivas");
            listaOrdenada.Add(1500, "Aide Michel");
            listaOrdenada.Add(620, "Carlangas");
            listaOrdenada.Add(10, "Usuario Desconocido");

            Console.WriteLine("LOS ELEMENTOS ORDENADOS CON CLAVE SON: ");

            foreach (object llave in listaOrdenada.Keys) { 
                

                Console.WriteLine("llave: " + llave + " Valor: " + listaOrdenada[llave]);
                
            
            }




        }





    }
}