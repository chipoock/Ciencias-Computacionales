
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Windows.Forms;
namespace WinFormsApp1
    
{
    public partial class Form1 : Form
    {

        private BindingList<Persona> personas = new BindingList<Persona>();

        private int editIndex = -1; //Menos uno cundo no se esta editando 
        









        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            limpiar();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (editIndex != -1)
            {


                personas.RemoveAt(editIndex);

                limpiar();
                DibujarTabla();

            } else {
                MessageBox.Show("Para eliminar primero da doble click en una fila");
                    
                    
                    }

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void tablaMuestra_MouseDoubleClick(object sender, MouseEventArgs e)
        {

            DataGridViewRow filaSeleccionada = tablaMuestra.SelectedRows[0];
            int posicionFila = tablaMuestra.Rows.IndexOf(filaSeleccionada);
            editIndex = posicionFila;
            System.Diagnostics.Debug.WriteLine(posicionFila);

            Persona p = personas[posicionFila];
            nombreBox.Text = p.nombre;
            edadBox.Text = p.edad;
            numTelBox.Text = p.numTelefono;
            gmailBox.Text = p.correo;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void guardarButton_Click(object sender, EventArgs e)
        {

            Persona p = new Persona();

            p.nombre = nombreBox.Text;
            p.edad = edadBox.Text;
            p.numTelefono = numTelBox.Text;
            p.correo = gmailBox.Text;


            if (editIndex != -1)
            {

                personas[editIndex] = p;
                editIndex = -1;
            
            }
            else
            {

                personas.Add(p);

            }

            limpiar();
        }


        public void limpiar() {

            editIndex = -1;

            DibujarTabla();

            nombreBox.Clear();
            edadBox.Clear();
            numTelBox.Clear();
            gmailBox.Clear();
        }

        private void DibujarTabla() { 
        
            tablaMuestra.DataSource = null;
            tablaMuestra.DataSource = personas;
        
        
        
        
        }

        private void nombreBox_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
