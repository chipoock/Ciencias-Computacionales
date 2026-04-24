import java.util.*;
public class MascotaVirtual{
   MascotaVirtual mascota;
   Gato g;
   Pato pato;
   Perro perro;
   
/**constructor inicializara los atributos pasivos del nuevo objeto
    este puede ser un Gato, un Perro o un Cotorro. 
   Parametros requeridos, int tipoDeMascota, char sexo, cadena raza, cadena nombre, cadena color
   Una vez inicializado el objeto invoca el ciclo de vida de la mascota 
*/
public MascotaVirtual(int t,char s,String r, String n,String c){  
  if(t==1) {
   g = new Gato( s, r,  n, c);
   g.cicloVida(); 
}
  else if(t==2) {
   pato = new Pato(s,r,n,c);
   pato.cicloVida();
}
  else if (t==3) {
   perro = new Perro(s,r,n,c);  
   perro.cicloVida();

}

  else{
    System.out.println("No se ha encontrado ningun animal");
} 
}

public static void main(String args[]){
   String n, c,r;
   char s;
   int t;   
   System.out.println("Que quieres:\n1-Gato\n2-Pato\n3-Perro\n4-Salir");
   Scanner sc=new Scanner(System.in);  
   t=sc.nextInt();
   if(t<4){
     System.out.println("Sexo de tu mascota? ");
     s=sc.next().charAt(0);sc.nextLine();  
     System.out.println("Raza ?");
     r=sc.nextLine();
     System.out.println("Nombre ?");
     n=sc.nextLine();
     System.out.println("Color ?");
     c=sc.nextLine();
     new MascotaVirtual(t,s,r,n,c);
   }else System.out.println("Bye!");
   }


}