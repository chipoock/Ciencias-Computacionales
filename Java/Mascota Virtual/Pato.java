public class Pato extends SerVivo{

public Pato(char s,String r, String n, String c ){
    super(s,r,n,c); 
  
}
  void alas(){
   System.out.println("El pato " + nombre + " mueve las alas");
 }  

  void sonidos(){
   System.out.println("Cuack, Cuackkk!! "); 
}

    void moverse(){
     System.out.println("el pato camina " );
}
   void moverse(String volar){
   alas ();
   System.out.println("y esta volando");

}

  @Override
  void comunicar(){
  sonidos();
  alas();
}

 	
}