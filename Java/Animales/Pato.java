public class Pato extends SerVivo{

boolean volar = true;
public Pato(String sexo, String nombre, int edad, String tipo){
  super(sexo, nombre, edad, tipo);
 
  
}
  void alas(){
   System.out.println("El " + tipo + " mueve las alas");
 }  
  @Override
  void sonidos(){
   System.out.println("Cuack, Cuackkk!! "); 
}

  @Override
  void nacer(){
     System.out.println("El " + tipo + " "+ nombre + " acaba de nacer");
}  
  @Override
    void moverse(){
     moverse(true);
}

    void moverse(String modoVuelo){
     System.out.println("el pato vuela " + modoVuelo);
}
 

 	
}