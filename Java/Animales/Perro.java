public class Perro extends SerVivo{
 
  public Perro(String sexo, String nombre, int edad, String tipo){
   super(sexo,nombre, edad, tipo); 
  
}
  @Override
  void sonidos(){
   System.out.println("Guaaww, Guaaww!");
}

  void moverCola() {
    System.out.println(nombre + " está moviendo la cola.");
  }
  @Override
  void nacer(){
     System.out.println("El " + tipo + " "+ nombre + " acaba de nacer");
}

}