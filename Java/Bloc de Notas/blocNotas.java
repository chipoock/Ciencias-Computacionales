import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class blocNotas{

    Frame f;
    TextArea escribir;
    MenuBar mb;
    Menu archivo, ayuda, config, acercade;
    MenuItem nuevo, tema, abrir, guardar, salir,isaac;
    Label etiqueta1,etiqueta2;
    Panel panelSur, panelEtiquetas;
    JTabbedPane tabs;
    JPanel panel1;
    JToolBar barraHerramientas;
    JButton btnGuardar, btnCopiar, btnCortar, btnPegar, btnAumentar, btnDisminuir, btnBuscar;

    int contadorPestañas = 1;

    public blocNotas(){

        f = new Frame("Bloc Notas");
        escribir = new TextArea();
        mb = new MenuBar();
        f.setLayout(new BorderLayout());

        archivo = new Menu("Archivo");
        ayuda = new Menu("Ayuda");
        acercade = new Menu("Acerca de...");
        config = new Menu("Config");

        nuevo = new MenuItem("Nuevo");
        abrir = new MenuItem ("Abrir");
        guardar = new MenuItem("Guardar");
        tema = new MenuItem("Modo Oscuro");
        salir = new MenuItem("Salir");
        isaac = new MenuItem("Isaac de Jesus Rivas Garcia");

        etiqueta1 = new Label("Linea: 32 ");
        etiqueta2 = new Label("Columna: 2");

        tabs = new JTabbedPane();
        panel1 = new JPanel(new BorderLayout());
        escribir.setBackground(new Color(41, 41, 41));
        escribir.setForeground(Color.WHITE);
        panel1.add(escribir, BorderLayout.CENTER);
        tabs.addTab("Ventana 1", panel1);
                  
        barraHerramientas = new JToolBar();
        btnGuardar = new JButton(new ImageIcon("imagenes/guardar.png"));
        btnCopiar = new JButton(new ImageIcon("imagenes/copiar.png"));
        btnCortar = new JButton(new ImageIcon("imagenes/tijeras.png"));
        btnPegar = new JButton(new ImageIcon("imagenes/pegar.png"));
        btnAumentar = new JButton(new ImageIcon("imagenes/mas.png"));
        btnDisminuir = new JButton(new ImageIcon("imagenes/menos.png"));
        btnBuscar = new JButton(new ImageIcon("imagenes/busqueda.png"));

       
        barraHerramientas.add(btnGuardar);
        barraHerramientas.add(btnCopiar);
        barraHerramientas.add(btnCortar);
        barraHerramientas.add(btnPegar);
        barraHerramientas.addSeparator();
        barraHerramientas.add(btnAumentar);
        barraHerramientas.add(btnDisminuir);
        barraHerramientas.addSeparator();
        barraHerramientas.add(btnBuscar);

        f.add(barraHerramientas, BorderLayout.NORTH);
        f.add(tabs, BorderLayout.CENTER);

        nuevo.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                contadorPestañas++;
                JPanel nuevaPestaña = new JPanel(new BorderLayout());
                TextArea nuevoTexto = new TextArea();
                nuevoTexto.setBackground(new Color(41, 41, 41));
                nuevoTexto.setForeground(Color.WHITE);
                nuevaPestaña.add(nuevoTexto, BorderLayout.CENTER);
                tabs.addTab("Ventana " + contadorPestañas, nuevaPestaña);
                tabs.setSelectedComponent(nuevaPestaña);
            }
        });

        panelEtiquetas = new Panel(new FlowLayout(FlowLayout.LEFT,10,5));
        panelEtiquetas.add(etiqueta1);
        panelEtiquetas.add(etiqueta2);

        panelSur = new Panel(new BorderLayout());
        panelSur.add(panelEtiquetas, BorderLayout.WEST);
        panelSur.setBackground(new Color(230, 230, 230));
        panelSur.setPreferredSize(new Dimension(700, 30));

        f.add(panelSur, BorderLayout.SOUTH);

        f.setMenuBar(mb);
        f.setSize(800,950);
        f.setVisible(true);
        f.validate();

        mb.add(archivo);
        mb.add(ayuda);

        archivo.add(nuevo);
        archivo.add(abrir);
        archivo.add(guardar);
        archivo.add(salir);
        archivo.add(config);
        config.add(tema);

        ayuda.add(acercade);
        acercade.add(isaac);
    }

    public static void main(String arg[]){
        blocNotas obj = new blocNotas();
    }
}

