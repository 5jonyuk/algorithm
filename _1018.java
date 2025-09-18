import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class _1018 {
  public static boolean[][] borad;
  public static int min = 64;

  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine()," ");

    int row = Integer.parseInt(st.nextToken());
    int col = Integer.parseInt(st.nextToken());

    borad = new boolean[row][col];

    for(int i=0; i<row; i++){
      String line = br.readLine();
      for(int j=0; j<col; j++){
        if(line.charAt(j)=='W')
          borad[i][j] = true;
        else borad[i][j] = false;
      }
    }

    for(int i=0; i<=row-8; i++){
      for(int j=0; j<=col-8; j++){
        find(i,j);
      }
    }
    System.out.println(min);
  }
  static void find(int x, int y){
    int end_x = x+8;
    int end_y = y+8;
    int count=0;

    boolean TF = borad[x][y];

    for(int i=x; i<end_x; i++){
      for(int j=y; j<end_y; j++){
        if(borad[i][j]!=TF)
          count++;
        TF = !TF;
      }
      TF= !TF;
    }
    count = Math.min(count, 64-count);
    min = Math.min(min, count);

  }
}