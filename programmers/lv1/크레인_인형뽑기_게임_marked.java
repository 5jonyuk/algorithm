package lv1;

import java.util.ArrayDeque;
import java.util.Deque;

// push는 0번인덱스로 넣기
// add는 뒷쪽으로 넣기
public class 크레인_인형뽑기_게임_marked {
    public int solution(int[][] board, int[] moves) {
        Deque<Integer> store = new ArrayDeque<>();
        int answer = 0;

        for (int selectColumn : moves) {
            for (int i = 0; i < board.length; i++) {
                if (board[i][selectColumn - 1] != 0) {
                    if (!store.isEmpty()) {
                        if (store.peek() == board[i][selectColumn - 1]) {
                            store.pop();
                            board[i][selectColumn - 1] = 0;
                            answer += 2;
                        } else {
                            store.push(board[i][selectColumn - 1]);
                            board[i][selectColumn - 1] = 0;
                        }
                        break;
                    } else {
                        store.push(board[i][selectColumn - 1]);
                        board[i][selectColumn - 1] = 0;
                        break;
                    }
                }
            }
        }
        return answer;
    }
}
