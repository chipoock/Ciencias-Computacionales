package application.Controlador;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;

public class ClienteController {
	
	
	@FXML
	TextField escribirClienteField;
	
	@FXML
	TextArea chatClienteArea;
	
	
		

	
	
	@FXML
	
	public void EnvioMensaje() {
		
		String escribirCliente =  escribirClienteField.getText();
		String chatCliente = chatClienteArea.getText();
		
		
		
		
	}
	
	

}
