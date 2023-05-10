import java.util.Scanner;
import java.util.Formatter;
import java.io.*;
import java.io.FileNotFoundException;
public class DoorAccess {

	public static void main(String[] args) {
		try {
			int x = 0;
			Scanner in = new Scanner(new File("DoorAccessLog.txt"));
			Formatter out = new Formatter("WynnieScibettaLog.txt");
			for(int i=0; i<3; i++) {
				in.next();
			}
//			System.out.println(in);
			for(int i=3;i<1203;i++) {
//				System.out.println(i);
				String first = in.next();
//				System.out.println(first);
				String last = in.next();
//				System.out.println(first+last);
				String time = in.next()+in.next()+in.next();
				System.out.println(first+" "+last+" "+time);
				if(first.equals("Wynnie")) {
//					System.out.println("found");
					x=x+1;
				}
			}
			System.out.println(x);
			out.format("the number she entered thhe building is "+x);
			out.flush();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} 
	}

}
