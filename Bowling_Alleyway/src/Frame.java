public class Frame {
    private int[] rolls;
    private int rollCount;

    public Frame() {
        rolls = new int[3];
        rollCount = 0;
    }

    public int[] getRolls() {
        return rolls;
    }

    public int getRollCount() {
        return rollCount;
    }

    public void addRoll(int pins) {
        rolls[rollCount++] = pins;
    }
}
