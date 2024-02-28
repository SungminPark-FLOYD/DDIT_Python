package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing05 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_mine;
	private JTextField tf_com;
	private JTextField tf_result;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing05 frame = new MySwing05();
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
	public MySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_mine = new JLabel("나:");
		lbl_mine.setBounds(28, 29, 57, 15);
		contentPane.add(lbl_mine);
		
		JLabel lbl_com = new JLabel("com:");
		lbl_com.setBounds(28, 65, 57, 15);
		contentPane.add(lbl_com);
		
		JLabel lbl_result = new JLabel("결과:");
		lbl_result.setBounds(28, 101, 57, 15);
		contentPane.add(lbl_result);
		
		tf_mine = new JTextField();
		tf_mine.setBounds(130, 26, 116, 21);
		contentPane.add(tf_mine);
		tf_mine.setColumns(10);
		
		tf_com = new JTextField();
		tf_com.setColumns(10);
		tf_com.setBounds(130, 62, 116, 21);
		contentPane.add(tf_com);
		
		tf_result = new JTextField();
		tf_result.setColumns(10);
		tf_result.setBounds(130, 98, 116, 21);
		contentPane.add(tf_result);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				game();
			}
		});
		btn.setBounds(28, 144, 218, 23);
		contentPane.add(btn);
	}
	
	private void game() {
		String user = tf_mine.getText();
		String com;
		double ran = Math.random();
		if(ran > 0.5) com = "홀";
		else com = "짝";
		
		tf_com.setText(com);
		if(user.equals(com)) tf_result.setText("승리");
		else tf_result.setText("패배");
	}

}
