import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class BowlingScoreboard extends JFrame {
    private Player[] players;
    private int currentPlayer;

    private JTextField pinsField;
    private JButton submitButton;
    private JTextArea scoreboardTextArea;

    public BowlingScoreboard(Player[] players) {
        this.players = players;
        currentPlayer = 0;
        initUI();
    }

    private void initUI() {
        setTitle("StrikeMaster Bowling Alleyway System");
        setSize(800, 600);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        setLayout(new BorderLayout());

        pinsField = new JTextField(5);
        submitButton = new JButton("Submit");
        scoreboardTextArea = new JTextArea();

        JPanel inputPanel = new JPanel();
        inputPanel.add(new JLabel("Enter pins knocked down: "));
        inputPanel.add(pinsField);
        inputPanel.add(submitButton);

        add(inputPanel, BorderLayout.NORTH);
        add(new JScrollPane(scoreboardTextArea), BorderLayout.CENTER);

        submitButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                int pins = Integer.parseInt(pinsField.getText());
                players[currentPlayer].getFrames()[players[currentPlayer].getCurrentFrame()].addRoll(pins);
                updateScoreboard();
                currentPlayer = (currentPlayer + 1) % players.length;
                pinsField.setText("");
            }
        });
    }

    private void updateScoreboard() {
        // Update the scoreboardTextArea with the new scores for each player
        StringBuilder sb = new StringBuilder();
        for (Player player : players) {
            sb.append(player.getName()).append("\n");

            for (int i = 0; i < 10; i++) {
                Frame frame = player.getFrames()[i];
                int[] rolls = frame.getRolls();
                int rollCount = frame.getRollCount();

                sb.append("Frame ").append(i + 1).append(": ");
                for (int j = 0; j < rollCount; j++) {
                    sb.append(rolls[j]).append(" ");
                }
                sb.append("\n");
            }
            sb.append("\n");
        }

        scoreboardTextArea.setText(sb.toString());
    }
{
    }
}
