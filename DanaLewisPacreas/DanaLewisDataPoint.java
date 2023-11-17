public class DanaLewisDataPoint {
    private String time;
    private int hearRate;
    private int insulinLevel;
    //constructo for datapoints 
    public DanaLewisDataPoint(String time,int heartRate,int insulinlevel){
        this.time =time;
        this.hearRate =hearRate;
        this.insulinlevel =insulinlevel;
    }
    //time constructor
    public String getTime(){
        return time;
    }
    public void setTime(String time){
        this.time =time;
    }
    //heart rate constructor
    public int getHeartRate(){
        return heartRate;
    }
    public void setHeartRate(int heartRate){
        this.heartRate=heartRate;
    }
    //insulin level cosntructor
    public int getInsulinlevel(){
        return insulinlevel;
    }
    public void setinsulinlevel(int insulinlevel){
        this.insulinlevel=insulinlevel;
    }
    @Override
    public String toString(){
        //It should return the information in the following format
        //"Time 20:25, HR 103, IL 116"
        return "Time "+getTime()+","+"+"+"HR"+getHEartRate()+","+"IL"+getInsulinlevel();
    }
}