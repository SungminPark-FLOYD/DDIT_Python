package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JLabel lbl;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 298, 686);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl = new JLabel("출력단수");
		lbl.setBounds(29, 36, 103, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(144, 33, 102, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				gugudan();
			}
		});
		btn.setBounds(25, 61, 221, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(29, 103, 217, 521);
		contentPane.add(ta);
	}
	
	public void gugudan() {
		String dan = tf.getText();
		int da = Integer.parseInt(dan);
		String res = "";
		
		for(int i = 1; i < 10; i++) {
			res += da + " * " + i + " =  " + (da*i) + "\n";
		}
		
		ta.setText(res);
	
	}
}
