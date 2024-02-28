package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf01;
	private JTextField tf02;
	private JTextField tf03;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf01 = new JTextField();
		tf01.setBounds(12, 30, 59, 21);
		contentPane.add(tf01);
		tf01.setColumns(10);
		
		JLabel lbl = new JLabel("+");
		lbl.setBounds(83, 33, 14, 15);
		contentPane.add(lbl);
		
		tf02 = new JTextField();
		tf02.setColumns(10);
		tf02.setBounds(99, 30, 59, 21);
		contentPane.add(tf02);
		
		tf03 = new JTextField();
		tf03.setColumns(10);
		tf03.setBounds(231, 30, 59, 21);
		contentPane.add(tf03);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add();
			}
		});
		btn.setBounds(167, 29, 52, 23);
		contentPane.add(btn);
	}
	
	private void add() {
		int t1 = Integer.parseInt(tf01.getText());
		int t2 = Integer.parseInt(tf02.getText());
		
		int sum = t1 + t2;
		
		tf03.setText(Integer.toString(sum));
		
		
	}
}
