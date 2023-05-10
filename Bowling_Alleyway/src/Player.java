public class Player {
    private String name;
    private Frame[] frames;
    private int currentFrame;

    public Player(String name) {
        this.name = name;
        frames = new Frame[10];
        for (int i = 0; i < 10; i++) {
            frames[i] = new Frame();
        }
        currentFrame = 0;
    }

    public String getName() {
        return name;
    }

    public Frame[] getFrames() {
        return frames;
    }

    public int getCurrentFrame() {
        return currentFrame;
    }

    public void setCurrentFrame(int currentFrame) {
        this.currentFrame = currentFrame;
    }
}
