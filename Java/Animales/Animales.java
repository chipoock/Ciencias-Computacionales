import java.util.*;
public class Animales{
    

public static void main(String[] args){

//Perro

 Perro miPerruno = new Perro("macho","pepe",5, "Perro");
 System.out.println("---Mascota Perro--- \n");
  System.out.println("Se llama " + miPerruno.nombre + " es " + miPerruno.sexo + " y tiene " +    miPerruno.edad + " años");
   miPerruno.comer();
   miPerruno.moverCola();
   miPerruno.tipo();
   miPerruno.moverse();
 

 System.out.println("\n \n"); 
//Pato
 

  Pato miPato = new Pato("Macho","Patroclo",0,"Pato");
 
 System.out.println("---Mascota Pato--- \n");

   System.out.println("Se llama " + miPato.nombre + " es " + miPato.sexo + " y tiene " +    miPato.edad + " años");
    miPato.nacer();
    miPato.moverse();
    miPato.alas();
    miPato.tipo();
    miPato.moverse("muy alto");
 
  
} 


 
} 