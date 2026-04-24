public abstract class SerVivo{
   String nombre, sexo, tipo;
   int edad;
  abstract void nacer();

  void crecer(){
   System.out.println("Ahora es mas grande");
 }
 
  void comer(){
   System.out.println("Esta comiendo");
 }
  void reproducirse(){
   System.out.println("Se reproduce ");
 
 }
  
  void morir(){
   System.out.println("El ser vivo a muerto");
 }
  void sonidos(){
  System.out.println("Hace sonidos");
}

  void tipo(){
    System.out.println("Es de tipo " + tipo);
}

void moverse(){
   System.out.println("Se mueve por tierra");

 }
 void moverse(boolean puedeVolar){
   System.out.println("Se mueve por el aire");

 }
 

public SerVivo (String sexo, String nombre, int edad, String tipo){
  
  this.nombre = nombre;
  this.edad = edad;
  this.sexo = sexo;
  this.tipo = tipo;
 }



}
