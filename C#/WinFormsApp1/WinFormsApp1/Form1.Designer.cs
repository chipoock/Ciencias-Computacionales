namespace WinFormsApp1
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            nombreBox = new TextBox();
            edadBox = new TextBox();
            numTelBox = new TextBox();
            gmailBox = new TextBox();
            guardarButton = new Button();
            gurdarButtom = new Button();
            limpiarButtom = new Button();
            tablaMuestra = new DataGridView();
            ((System.ComponentModel.ISupportInitialize)tablaMuestra).BeginInit();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AccessibleRole = AccessibleRole.ScrollBar;
            label1.AutoSize = true;
            label1.Location = new Point(49, 64);
            label1.Name = "label1";
            label1.Size = new Size(57, 15);
            label1.TabIndex = 0;
            label1.Text = "Nombre: ";
            label1.Click += label1_Click;
            // 
            // label2
            // 
            label2.AccessibleRole = AccessibleRole.ScrollBar;
            label2.AutoSize = true;
            label2.Location = new Point(70, 113);
            label2.Name = "label2";
            label2.Size = new Size(36, 15);
            label2.TabIndex = 1;
            label2.Text = "Edad:";
            // 
            // label3
            // 
            label3.AccessibleRole = AccessibleRole.ScrollBar;
            label3.AutoSize = true;
            label3.Location = new Point(54, 161);
            label3.Name = "label3";
            label3.RightToLeft = RightToLeft.Yes;
            label3.Size = new Size(52, 15);
            label3.TabIndex = 2;
            label3.Text = "Telefono";
            label3.Click += label3_Click;
            // 
            // label4
            // 
            label4.AccessibleRole = AccessibleRole.ScrollBar;
            label4.AutoSize = true;
            label4.Location = new Point(62, 210);
            label4.Name = "label4";
            label4.Size = new Size(44, 15);
            label4.TabIndex = 3;
            label4.Text = "Gmail: ";
            label4.Click += label4_Click;
            // 
            // nombreBox
            // 
            nombreBox.Location = new Point(112, 61);
            nombreBox.Name = "nombreBox";
            nombreBox.Size = new Size(226, 23);
            nombreBox.TabIndex = 4;
            nombreBox.TextChanged += nombreBox_TextChanged;
            // 
            // edadBox
            // 
            edadBox.Location = new Point(112, 110);
            edadBox.Name = "edadBox";
            edadBox.Size = new Size(226, 23);
            edadBox.TabIndex = 5;
            // 
            // numTelBox
            // 
            numTelBox.Location = new Point(112, 158);
            numTelBox.Name = "numTelBox";
            numTelBox.Size = new Size(226, 23);
            numTelBox.TabIndex = 6;
            // 
            // gmailBox
            // 
            gmailBox.Location = new Point(112, 207);
            gmailBox.Name = "gmailBox";
            gmailBox.Size = new Size(226, 23);
            gmailBox.TabIndex = 7;
            // 
            // guardarButton
            // 
            guardarButton.BackColor = Color.FromArgb(0, 102, 102);
            guardarButton.ForeColor = SystemColors.Control;
            guardarButton.Location = new Point(868, 515);
            guardarButton.Name = "guardarButton";
            guardarButton.Size = new Size(106, 41);
            guardarButton.TabIndex = 8;
            guardarButton.Text = "Guardar";
            guardarButton.UseVisualStyleBackColor = false;
            guardarButton.Click += guardarButton_Click;
            // 
            // gurdarButtom
            // 
            gurdarButtom.BackColor = Color.FromArgb(163, 0, 0);
            gurdarButtom.ForeColor = SystemColors.Control;
            gurdarButtom.Location = new Point(29, 515);
            gurdarButtom.Name = "gurdarButtom";
            gurdarButtom.Size = new Size(106, 41);
            gurdarButtom.TabIndex = 9;
            gurdarButtom.Text = "Eliminar";
            gurdarButtom.UseVisualStyleBackColor = false;
            gurdarButtom.Click += button1_Click;
            // 
            // limpiarButtom
            // 
            limpiarButtom.BackColor = Color.FromArgb(39, 33, 33);
            limpiarButtom.ForeColor = SystemColors.Control;
            limpiarButtom.Location = new Point(29, 468);
            limpiarButtom.Name = "limpiarButtom";
            limpiarButtom.Size = new Size(106, 41);
            limpiarButtom.TabIndex = 10;
            limpiarButtom.Text = "Limpiar";
            limpiarButtom.UseVisualStyleBackColor = false;
            limpiarButtom.Click += button2_Click;
            // 
            // tablaMuestra
            // 
            tablaMuestra.AllowUserToAddRows = false;
            tablaMuestra.AllowUserToDeleteRows = false;
            tablaMuestra.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            tablaMuestra.EditMode = DataGridViewEditMode.EditProgrammatically;
            tablaMuestra.Location = new Point(377, 61);
            tablaMuestra.Name = "tablaMuestra";
            tablaMuestra.ReadOnly = true;
            tablaMuestra.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            tablaMuestra.Size = new Size(597, 390);
            tablaMuestra.TabIndex = 11;
            tablaMuestra.CellContentClick += dataGridView1_CellContentClick;
            tablaMuestra.MouseDoubleClick += tablaMuestra_MouseDoubleClick;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.Silver;
            ClientSize = new Size(1028, 568);
            Controls.Add(tablaMuestra);
            Controls.Add(limpiarButtom);
            Controls.Add(gurdarButtom);
            Controls.Add(guardarButton);
            Controls.Add(gmailBox);
            Controls.Add(numTelBox);
            Controls.Add(edadBox);
            Controls.Add(nombreBox);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ((System.ComponentModel.ISupportInitialize)tablaMuestra).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private TextBox nombreBox;
        private TextBox edadBox;
        private TextBox numTelBox;
        private TextBox gmailBox;
        private Button guardarButton;
        private Button gurdarButtom;
        private Button limpiarButtom;
        private DataGridView tablaMuestra;
    }
}
