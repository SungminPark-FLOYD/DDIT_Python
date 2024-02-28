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

public class MySwing09 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing09 frame = new MySwing09();
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
	public MySwing09() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 335, 549);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_first = new JLabel("첫별수");
		lbl_first.setBounds(26, 25, 57, 15);
		contentPane.add(lbl_first);
		
		JLabel lbl_last = new JLabel("끝별수");
		lbl_last.setBounds(26, 66, 57, 15);
		contentPane.add(lbl_last);
		
		tf_first = new JTextField();
		tf_first.setBounds(149, 22, 116, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(149, 63, 116, 21);
		contentPane.add(tf_last);
		
		JButton btn = new JButton("별그리기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				star();
			}
		});
		btn.setBounds(26, 104, 239, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(26, 137, 239, 316);
		contentPane.add(ta);
	}
	
	private void star() {
		String tf = tf_first.getText();
		String tl = tf_last.getText();
		String star = "";
		int tf1 = Integer.parseInt(tf);
		int tl1 = Integer.parseInt(tl);
		
		for(int i = tf1; i<= tl1; i++) {
			star += printStar(i);
		}
		
		ta.setText(star);
	}
	
	private String printStar(int i) {
		String s = "";
		for(int k = 1; k <= i; k++) {
			s += "*";
		}
		
		return s+ "\n";
	}
	
	
}
