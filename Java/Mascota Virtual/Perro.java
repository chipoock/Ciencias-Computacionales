public class Perro extends SerVivo{
 
  public Perro(char s,String r, String n, String c ){
    super(s,r,n,c); 

  
}
  void sonidos(){
   System.out.println("Guaaww, Guaaww!");
}

  void moverCola() {
    System.out.println(nombre + " está moviendo la cola.");
  }

  void muerde(){
  System.out.println(nombre + "esta mordiendo");
}
  @Override
  void comunicar(){
  sonidos();
  moverCola();
}
}