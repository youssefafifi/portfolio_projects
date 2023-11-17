import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
public class DanaLewisArray{
    //TODO: Array for storage
    //defclare storage for danalewis data points 
    private DanaLewisDataPoint [] datapoints =new DanaLewisDataPoint[2000];
    private int size =0;
    //constructor
    //add data points to this array
    public void addDatapoint(DanaLewisDataPoint d){
        if(size<datapoints.length){
            datapoints[size]=d;
            size++;
        }else{
            //handle every other scenario
        }
    }
    //current heart rate for later operations?
    public int getCurrentAverageHeartRate(){
        if(size==0){
            return 0;
        }
        int totalHeartRate=0;
        for(int i=0;i<size;i++){
            totalHeartRate+=dataints[i].getHeartRate();
        }
        return totalHeartRate /size;
            
    }
    //insulin levels 
    public int getCurrentAverageInsulinLevel(){
        if(size==0){
            return 0;
            //empty array or corrupt one
        }
        int totalInsulinlevel=0;
        for(int i=0;i<size;i++){
            totalInsulinlevel+=datapoints[i].getInsulinLevel();
        }
        return totalInsulinLevel/size;
    }
    public static void main(String [] args){
        try{
            Scanner scanner = new Scanner(new File("0010Points.txt");
            while(scanner.has.NextLine()){
                String line = scanner.nextLine();
                String[] parts =line.split(",");
                if(parts.length ==3){
                    String time =parts[0];
                    int heartRate=Integer.parseInt(parts[1]);
                    int insulinLevel =Intger.parseInt(parts[2]);
                    DanaLewisDataPoint datapoint =new DanaLewisDataPoint(time, heartRate, insulinLevel);
                    danaLewisArray.addDataPoint(dataPoint);
                }else{
                    System.out.println("Invalid data format in Line: "+line);
                }
            }
            scanner.close();
            //print results
            System.out.println("Average Heart rate :"+danaLewisArray.getcurrentAverageHeartRate());
            System.out.println("Averge Insulin level: "+danaLewisArray.getcurrentinsulinlevel());
        }catch(FileNotFoundException e){
            e.printStacktrace();
        }
    }
}