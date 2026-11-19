package lv3;

import java.util.*;

public class 베스트앨범_marked {
    private record Song(int id, int plays, String genres) {
    }

    public int[] solution(String[] genres, int[] plays) {
        // 각 장르별 총 재생횟수 저장
        Map<String, Integer> genresTotalPlayMap = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            if (genresTotalPlayMap.containsKey(genres[i])) {
                genresTotalPlayMap.put(
                        genres[i],
                        genresTotalPlayMap.get(genres[i]) + plays[i]);
            } else {
                genresTotalPlayMap.put(
                        genres[i],
                        plays[i]);
            }
        }

        List<String> sortedGenres = genresTotalPlayMap.entrySet().stream()
                .sorted((a, b) -> Integer.compare(b.getValue(), a.getValue()))
                .map(Map.Entry::getKey)
                .toList();

        // 노래 정보 추출
        List<Song> songs = new ArrayList<>();
        for (int i = 0; i < genres.length; i++) {
            songs.add(new Song(i, plays[i], genres[i]));
        }

        // 재생 수가 많은 장르 순으로 해당 장르의 상위 2개 노래 뽑고 정답에 저장
        List<Integer> answer = new ArrayList<>();
        for (String genre : sortedGenres) {
            List<Integer> songIds = songs.stream()
                    .filter(song -> song.genres().equals(genre))
                    .sorted((a, b) -> {
                        int compare = Integer.compare(b.plays(), a.plays());
                        if (compare == 0) {
                            return Integer.compare(a.id(), b.id());
                        }
                        return compare;
                    })
                    .limit(2)
                    .map(Song::id)
                    .toList();

            answer.addAll(songIds);
        }

        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
