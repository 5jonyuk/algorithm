import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class alphabetCount {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String word = br.readLine().toUpperCase();
    int[] alphabetCount = new int[26];

    for(int i=0; i<word.length(); i++){
      char alphabet = word.charAt(i);
      if(alphabet >= 'A' && alphabet <= 'Z'){
        alphabetCount[alphabet-'A']++;
      }
    }
    int maxCount=0;
    int maxIndex=0;

     for(int i=0; i< alphabetCount.length; i++){
       if(alphabetCount[i]>maxCount){
         maxCount=alphabetCount[i];
         maxIndex=i;
       }
     }
     int countMax=0;

     for(int count : alphabetCount){
       if(count == maxCount){
         countMax++;
       }
     }
     if(countMax>1) System.out.println("?");
     else System.out.println((char)('A'+maxIndex));
  }
}