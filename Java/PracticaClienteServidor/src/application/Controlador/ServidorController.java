package application.Controlador;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;

public class ServidorController {

	
	
	

	@FXML
	TextField escribirServidorField;
	
	@FXML
	TextArea chatServidorArea;
	
	
		
	
	@FXML
	
	public void EnvioMensaje() {
		
		String escribirServidor =  escribirServidorField.getText();
		String chatServidor = chatServidorArea.getText();
		
		
		
		
	}
}
