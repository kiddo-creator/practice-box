import javax.swing.JFrame;

public class Window {
	public static final int WIDTH = 300, HEIGHT = 600;
	private JFrame window;
	
	
	public Window() {
		window = new JFrame("Tetris Game");
		window.setSize(WIDTH,HEIGHT);
		window.setVisible(JFrame.EXIT_ON_CLOSE);
		window.setLocationRelativeTo(null);
	}
	
	public static void main(String[] args) {
		new window();
	}

}
