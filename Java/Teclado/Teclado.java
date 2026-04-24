import java.awt.*;
public class Teclado{
  Frame f;
  TextArea ta;
  Button teclas[];  
  Panel p;
  Label lb;
  Checkbox ch;
  Choice c;
  MenuBar mb;
  Menu archi,edi;
  MenuItem abrir,cerrar, copy,paste;
  CheckboxMenuItem cmi;
  String etiqueta[]={"Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Ñ","Z","X","C","V","B","N","M",",",":","."};
   
public Teclado(){
   f= new Frame("Teclado");
   ta= new TextArea();
   p= new Panel();
   lb = new Label("Texto de prueba");
   ch = new Checkbox("Opcion 1",true);
   c =new Choice();
   mb=new MenuBar();
   cmi = new CheckboxMenuItem("Vista impresion");
   archi = new Menu("Archivo");
   edi =  new Menu("Editar");
   abrir= new MenuItem("Abrir");
   cerrar= new MenuItem("Cerrar");
   copy= new MenuItem("Copiar");
   paste= new MenuItem("Pegar");
   
   
   
   mb.add(archi);
   archi.add(cmi);
   archi.add(edi);
   archi.add(abrir);
   archi.add(cerrar);
   edi.add(copy);
   edi.add(paste);


   c.add("Azul");
   c.add("rojo");
   c.add("amarillo"); 
   teclas = new Button[32];
   

   for(int i=0;i<etiqueta.length;i++){
   teclas[i]=new Button(etiqueta[i]);
   p.add(teclas[i]);
}
  //Freme (Ventana Completa)
  f.setLayout(new GridLayout(5,2,5,5));

  f.add(lb);
  f.add(ta);
  f.add(p);
  f.add(ch);
  f.add(c);
  f.setSize(600,600);
  f.setVisible(true);
  f.setResizable(false);
  f.setMenuBar(mb);

  // Area de texto 
  ta.setBackground(Color.black);


 //Panel
  p.setLayout(new GridLayout(3,10,5,5));
  p.setBackground(Color.red);

 }
public static void main(String args[]){
  Teclado obj = new Teclado();
 }

}