package application;
	
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;


public class Main extends Application {
	
	public void start(Stage primaryStage) {
		try {
			// 1. Cargamos el diseño desde la carpeta de vistas
			// Nota: El nombre del archivo debe terminar en .fxml
			FXMLLoader loader = new FXMLLoader(getClass().getResource("/application/Vista/Cliente.fxml"));
			Parent root = loader.load();

			// 2. Creamos la escena (el contenido de la ventana)
			Scene scene = new Scene(root);
	        primaryStage.setTitle("Cliente");
	        primaryStage.setScene(scene);
	        primaryStage.show();
	    } catch(Exception e) {
	        // Si la ruta está mal, aquí nos avisará el error
	        e.printStackTrace();
	    }
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
