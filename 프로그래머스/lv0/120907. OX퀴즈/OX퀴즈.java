class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        for (int i = 0; i < quiz.length; i++) {
            String[] me = quiz[i].split(" ");
            int a = Integer.parseInt(me[0]);
            int b = Integer.parseInt(me[2]);
            int c = Integer.parseInt(me[4]);
            int op = me[1].equals("-") ? -1 : 1;
            answer[i] = a + op * b == c ? "O" : "X";
        }
        return answer;
    }
}