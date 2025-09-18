import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _2753 {
  public static void main(String [] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int year = Integer.parseInt(br.readLine());

    if(isYear(year)){
      System.out.println("1");
    }else System.out.println("0");
  }
  static boolean isYear(int year){
    return (year%4==0 && year%100!=0)||year%400==0;
  }
}
