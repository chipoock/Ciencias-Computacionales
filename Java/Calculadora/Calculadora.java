import java .awt.*;
public class Calculadora{
 Frame framePrincipal;
 TextArea textDigitos;
 Button buttonsParaCalculadora[];
 Panel panelBotones;
 Panel panelTexto;
 String cantidadDeBotones[]={" C "," * "," / "," <x| "," 7" ," 8 "," 9 "," + "," 4 "," 5 "," 6 "," - "," 1 "," 2 "," 3 ","=","+/-"," 0 "," . "};
 

 public Calculadora(){

  //Creación de Ventana Principal

  framePrincipal = new Frame("Calculadora");
  panelTexto = new Panel();
  panelBotones = new Panel();
  buttonsParaCalculadora = new Button[cantidadDeBotones.length];


  //Creacion de botones

  for(int i=0;i<cantidadDeBotones.length;i++){
   buttonsParaCalculadora[i] = new Button(cantidadDeBotones[i]);
   panelBotones.add(buttonsParaCalculadora[i]);    


  //Frame(Ventana Completa)
  framePrincipal.setLayout(new GridLayout(2,8));
  framePrincipal.setSize(340, 550);
  framePrincipal.setVisible(true);
  framePrincipal.setResizable(false);

       //Añado cosas al frame
  framePrincipal.add(panelTexto);
  framePrincipal.add(panelBotones);

  //Panel texto
  panelTexto.setBackground(Color.black);
  

  //Panel Botones
  panelBotones.setLayout(new GridLayout(5,2));
  panelBotones.setBackground(Color.gray);

   }

 }
 
   public static void main(String args[]){
   Calculadora obj = new Calculadora();







}




}