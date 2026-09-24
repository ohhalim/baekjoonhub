import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] solution(String s) {
        // 문자열 길이만큼 정답 배열 생성
        int[] answer =  new int[s.length()];
        // 각 문자가 마지막으로 등장한 인덱스 저장 
        Map<Character, Integer> lastIndex = new HashMap<>();
        // 문자열을 처음부터 끝까지 순회
        for (int i=0; i < s.length(); i++) {
            char c =s.charAt(i);
            if (lastIndex.containsKey(c)) {
                answer[i] = i -lastIndex.get(c);
            } else{
                answer[i] = -1;
            }
            lastIndex.put(c, i);
        }
        return answer;
    }
}