import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // 이름 (string)을 키로, 인원수(Integer)를 값으로 저장하는 빈 HashMap을 만든다
        Map<String, Integer> map = new HashMap<>();
        
        // participant 배열에서 이름을 하나씩 꺼내 name에 담으면서 반복 
        for (String name: participant) {
            // name의 현재 인원수를 가져와 1을 더한뒤 다시 name의 값으로 저장
            map.put(name, map.getOrDefault(name, 0) + 1);
        }
        // completion배열에서 이름을 하나씩 꺼내 name에 담으며 반복
        for (String name: completion) {
            // name의 현재 인원수 를 가져와 1을 뺀뒤 다시 name값으로 저장 
            map.put(name, map.getOrDefault(name, 0) - 1);
        }
        // map에 저장된 모든이름을 하나씩 꺼내 name에 담으면 반복
        for (String name: map.keySet()) {
            // name의 남은 인원수가 0이 아니라면 
            if (map.get(name) != 0) {
                //그 이름을 정답으로 반환하고 메서드를 끝낸다 
                return name;
            }
        }
        return ""; 
    }
}