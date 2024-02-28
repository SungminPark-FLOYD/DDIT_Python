package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private String phone = "";

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
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
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 393, 368);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(29, 33, 322, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add(btn1);
			}
		});
		btn1.setBounds(29, 76, 97, 23);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add(btn2);
			}
		});
		btn2.setBounds(138, 76, 97, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add(btn3);
			}
		});
		btn3.setBounds(254, 76, 97, 23);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add(btn4);
			}
		});
		btn4.setBounds(29, 109, 97, 23);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add(btn5);
			}
		});
		btn5.setBounds(138, 109, 97, 23);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add(btn6);
			}
		});
		btn6.setBounds(254, 109, 97, 23);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add(btn7);
			}
		});
		btn7.setBounds(29, 142, 97, 23);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add(btn8);
			}
		});
		btn8.setBounds(138, 142, 97, 23);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add(btn9);
			}
		});
		btn9.setBounds(254, 142, 97, 23);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				add(btn0);
			}
		});
		btn0.setBounds(29, 175, 97, 23);
		contentPane.add(btn0);
		
		JButton btnCall = new JButton("CALL");
		btnCall.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {	
				
				call();
			}
		});
		btnCall.setBounds(138, 175, 213, 23);
		contentPane.add(btnCall);
	}
	
	//필드에 숫자 추가
	private void add(JButton button) {
		String num = button.getText();
		phone += num;
		tf.setText(phone);
	}
	//버튼누르고 call누르면 alert창 나오면서 calling + 번호 + 확인버튼 누르면 창 닫기
	private void call() {
		JOptionPane.showMessageDialog(tf, "Calling ~~ \n" + phone);
		phone = "";
		tf.setText(phone);
	}

}
