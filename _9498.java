import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;

public class _9498 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int examScore = Integer.parseInt(br.readLine());
    System.out.println(Score(examScore));
  }

  static Character Score(int examScore) {
    if (examScore>=90 && examScore<=100)
      return 'A';
    else if (examScore>=80 && examScore<=89)
      return 'B';
    else if (examScore>=70 && examScore<=79)
      return 'C';
    else if (examScore>=60 && examScore<=69)
      return 'D';
    else
      return 'F';
  }
}
