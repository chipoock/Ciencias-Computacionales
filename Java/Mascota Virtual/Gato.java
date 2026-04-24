public class Gato extends SerVivo{
  public Gato(char s,String r, String n,String c){
    super(s,r,n,c); 
  
  }
   void maullar(){
     System.out.println("Miuau,miauauuuu");
   } 
  void ronronear(){
    System.out.println("Grrrggeerrrrr");
  }
   void comunicar(){
     maullar();
     ronronear();
 }
}