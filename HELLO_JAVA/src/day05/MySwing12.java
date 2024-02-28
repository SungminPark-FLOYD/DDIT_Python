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

public class MySwing12 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;
	private int[] arr;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing12 frame = new MySwing12();
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
	public MySwing12() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 303, 516);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lel = new JLabel("맞출수");
		lel.setBounds(32, 46, 57, 15);
		contentPane.add(lel);
		
		tf = new JTextField();
		tf.setBounds(129, 43, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				game();
			}
		});
		btn.setBounds(32, 83, 211, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(32, 138, 213, 302);
		contentPane.add(ta);
		
		arr = randomNum();
	}
	
	
	private int[] randomNum() {
		int[] aa = {
				1,2,3,4,5, 6,7,8,9,
		};
		
		for(int i = 0; i < 1000; i++) {
			int ran = (int)((Math.random()*9));
			int a = aa[0];
			aa[0] = aa[ran];
			aa[ran] = a;
		}
		
		int[] n = {aa[0], aa[1], aa[2]};
		return n;
	}
	
	private String baseBall(int[] digits) {
		int st = 0;
		int b = 0;
		String sb = "";
		if(arr[0] == digits[0]) st++;
		if(arr[1] == digits[1]) st++;
		if(arr[2] == digits[2]) st++;
	
		if(arr[0] == digits[1]) b++; 
		if(arr[0] == digits[2]) b++;
		if(arr[1] == digits[0]) b++; 
		if(arr[1] == digits[2]) b++;
		if(arr[2] == digits[1]) b++;
		if(arr[2] == digits[0]) b++;

		
		
		if(st == 3) sb = "축하합니다";
		else sb = st + "S" + b + "B" + "\n";
		return sb;
		
		
	}
	private void game() {
		String user = "";	
		String res = "";
		user = tf.getText();
        int[] digits = new int[user.length()];
        for(int i=0; i<user.length(); i++) digits[i] = user.charAt(i) - '0';
        res = baseBall(digits);       
        ta.append(user + "\t" + res + "\n");
        tf.setText("");
               
	}
}
