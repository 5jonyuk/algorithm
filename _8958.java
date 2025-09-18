import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _8958 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int TestCase = Integer.parseInt(br.readLine());
    int Count=0;
    int TestResult=0;
    int[] Result = new int[TestCase];

    for(int i=0; i<TestCase; i++){
      String Quiz = br.readLine().trim().toUpperCase();
      for(int j=0; j<Quiz.length(); j++){
        char QuizResult = Quiz.charAt(j);
        if(Condition1(QuizResult,Quiz.length())){
          Count+=1;
          TestResult+=Count;
          Result[i]=TestResult;
        }
        else if (Condition2(QuizResult,Quiz.length())){
          Count=0;
        }
        else System.out.println("O나 X만을 입력해주세요.");
      }
      TestResult=0;
      Count=0;
    }
    for(int i=0; i<TestCase; i++){
      System.out.println(Result[i]);
    }
  }
  static boolean Condition1(char c, int length){
    return c == 'O' && (length>0 && length<80);
  }
  static boolean Condition2(char c, int length){
    return c == 'X' && (length>0 && length<80);
  }
}
