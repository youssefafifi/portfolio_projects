import javax.swing.*;

public class BowlingAlleywaySystem {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                Player[] players = new Player[]{
                        new Player("Player 1"),
                        new Player("Player 2")
                };

                BowlingScoreboard scoreboard = new BowlingScoreboard(players);
                scoreboard.setVisible(true);
            }
        });
    }
}

