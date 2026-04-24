import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GameMenuGraphics extends JPanel implements MouseListener {

    private Rectangle newGameBtn, aboutBtn, helpBtn, exitBtn;
    private String selectedOption = "";
    private Image background;

    public GameMenuGraphics() {
        // Cargar imagen de fondo
        background = new ImageIcon("background.jpg").getImage();

        // Definir botones como áreas rectangulares
        newGameBtn = new Rectangle(100, 200, 200, 40);
        aboutBtn   = new Rectangle(100, 260, 200, 40);
        helpBtn    = new Rectangle(100, 320, 200, 40);
        exitBtn    = new Rectangle(100, 380, 200, 40);

        addMouseListener(this);
        setFocusable(true);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;

        // Fondo
        g2.drawImage(background, 0, 0, getWidth(), getHeight(), this);

        // Fondo semitransparente para el menú lateral
        g2.setColor(new Color(0, 0, 0, 150));
        g2.fillRect(50, 150, 250, 300);

        // Configurar texto
        g2.setFont(new Font("Arial", Font.BOLD, 22));
        g2.setColor(Color.WHITE);
        g2.drawString("GAME MENU", 110, 180);

        // Dibujar botones
        drawButton(g2, newGameBtn, "NEW GAME");
        drawButton(g2, aboutBtn, "ABOUT");
        drawButton(g2, helpBtn, "HELP");
        drawButton(g2, exitBtn, "EXIT GAME");
    }

    private void drawButton(Graphics2D g2, Rectangle rect, String text) {
        if (selectedOption.equals(text)) {
            g2.setColor(new Color(255, 255, 255, 100));
            g2.fill(rect);
        }

        g2.setColor(Color.WHITE);
        g2.draw(rect);
        FontMetrics fm = g2.getFontMetrics();
        int textX = rect.x + (rect.width - fm.stringWidth(text)) / 2;
        int textY = rect.y + (rect.height + fm.getAscent()) / 2 - 5;
        g2.drawString(text, textX, textY);
    }

    @Override
    public void mouseClicked(MouseEvent e) {
        Point p = e.getPoint();

        if (newGameBtn.contains(p)) {
            System.out.println("Ir a nueva pantalla de juego");
        } else if (aboutBtn.contains(p)) {
            JOptionPane.showMessageDialog(this, "Hecho por ti :)");
        } else if (helpBtn.contains(p)) {
            JOptionPane.showMessageDialog(this, "Instrucciones...");
        } else if (exitBtn.contains(p)) {
            System.exit(0);
        }
    }

    @Override public void mousePressed(MouseEvent e) {}
    @Override public void mouseReleased(MouseEvent e) {}
    @Override public void mouseEntered(MouseEvent e) {}
    @Override public void mouseExited(MouseEvent e) {}

    public static void main(String[] args) {
        JFrame frame = new JFrame("Game Menu with Graphics");
        GameMenuGraphics menu = new GameMenuGraphics();
        frame.add(menu);
        frame.setSize(800, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}