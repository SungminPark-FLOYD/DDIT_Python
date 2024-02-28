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

public class MySwing11 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JTextArea ta;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing11 frame = new MySwing11();
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
	public MySwing11() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 269, 568);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("숫자(1~100)");
		lbl.setBounds(40, 31, 83, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(153, 28, 65, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("숫자맞추기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				mClick();
			}
		});
		btn.setBounds(40, 56, 178, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(40, 100, 178, 330);
		contentPane.add(ta);
		
		//랜덤함수 호출
		setRandom();
	}
	
	int ran;
	
	void setRandom() {
		ran = (int)(Math.random()*100)+1;
		System.out.println(ran);
	}
	
	//TODO 숫자 UP && DOWN 게임
	//숫자 넣고 버튼 누르면 tf 비우고 ta에 text 누적
	private void mClick() {
		String user = "";
		String com = "";
		
		
		user = tf.getText();
		int userNum = Integer.parseInt(user);
		
		if(userNum == ran) com = "정답";
		if(userNum < ran) com = "UP";
		if(userNum > ran) com = "DOWN";
		
		tf.setText("");
		ta.append(userNum + "  " + com  + "\n");
	
	}

}
