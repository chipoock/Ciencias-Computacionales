import java.util.*;
public abstract class SerVivo{
  String nombre,raza, color;
;
  int edad,energia,animo,salud,hambre;

  //animo: 4-Feliz,3-contento,2-tristeYcansado, 1-enojado, 0-Depresion
 
 String eAnimo[]={"Depresion","Enojado","TristeYcansado","Contento","Feliz"};
  char sexo;

/** Constructor recibe como parametros: char sexo, cadena raza, cadena nombre
    El serVivo al nacer tiene solo el 50% de su energia y de animo esta contento*/

  public SerVivo(char s,String r, String n, String c){
    nombre=n;
    raza=r;    
    sexo=s;
    edad=0;
    energia=50; 
    animo=3;
    color = c;  
  }

   void comer(int porcion){
     System.out.println("\nTodo ser vivo necesita alimentarse");
     energia+=porcion*25;
     animo+=animo<4?1:0;
  }

  void descansar(int tiempo){
     System.out.println("\nDescansando...");
     energia+=tiempo*5;
     animo+=animo<4?1:0;
   }

  void jugar(){
    System.out.println("\nJugando...");
    energia-=10;
    if(energia>20)
       animo+=animo<4?1:0;
    else animo=2;
  }

  void banarlo(){
   System.out.println("\nEnjabonado y enjuagado= limpio");
   animo+=animo<4?1:0; 
   energia-=5;
  }
  

abstract void comunicar();

 void cicloVida(){
     Scanner sc=new Scanner(System.in); 
     int accion,u;  
    do{
       if(energia<=20)
         System.out.println("¡¡¡Debes alimentarlo su energia es baja!!!\n¡¡¡Es aconsejable descanse tambien!!!\n");
       System.out.println("\nDe animo esta: "+ eAnimo[animo]);
       System.out.println("\n1-Comer\n2-Descansar\n3-jugar\n4-Bañarlo\n"); accion=sc.nextInt();
       switch(accion){
           case 1:System.out.println("Cuantas porciones le daras? ");u=sc.nextInt();
                  comer(u); break;
           case 2:System.out.println("Unidades de descanso? ");u=sc.nextInt();
                  descansar(u); break;
           case 3:jugar(); break;
           case 4:banarlo(); break;
       }       
    }while(energia>=1);
    System.out.println("Tu mascota murio, no la alimentaste y diste descanso necesario");
  }
}