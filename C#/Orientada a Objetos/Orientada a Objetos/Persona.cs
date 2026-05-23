using System;
using System.Collections.Generic;
using System.Text;

namespace Orientada_a_Objetos
{
    internal class Persona
    {
        String nombre, colorOjos, colorPelo;
        float altura;
        int velocidad, edad;


        public Persona(String nombre,String colorOjos, String colorPelo, float altura, int edad)
        {
            setNombre(nombre);
            setAltura(altura);
            setColorOjos(colorOjos);
            setColorPelo(colorPelo);
            setEdad(edad);

        }


        public virtual void  Caminar(int velocidad) {

            Console.WriteLine("Caminar a: " + velocidad + "Km por hora");
        
        }

        public void Hablar() {
            Console.WriteLine("Esta Hablando");
        }








        public String getNombre(String nombre) { 

            return nombre;
        
        }

        public void setNombre(String nombre) {

            this.nombre = nombre;

            
        
        }






        public String getColorOjos(String colorOjos)
        {

            return colorOjos;

        }

        public void setColorOjos(String colorOjos)
        {
            this.colorOjos = colorOjos;


        }







        public String getColorPelo(String colorPelo)
        {

            return colorPelo;

        }

        public void setColorPelo(String colorPelo)
        {

            this.colorPelo = colorPelo;



        }


        public float getAltura(float altura)
        {

            return altura;

        }

        public void setAltura(float altura)
        {


            this.altura = altura;
                

        }

        public int getEdad(int edad)
        {

            return edad;

        }

        public void setEdad(int edad)
        {

            
            this.edad = edad;


        }

    }
}
