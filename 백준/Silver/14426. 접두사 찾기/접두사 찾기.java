import java.io.*;
import java.util.*;

public class Main {

    static TrieNode root;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        root = new TrieNode();
        for (int i = 0; i < N; i++) {
            insert(br.readLine());
        }
        int cnt = 0;
        for (int i = 0; i < M; i++) {
            if (search(br.readLine()))
                cnt++;
        }
        System.out.println(cnt);
    }

    static class TrieNode {
        HashMap<Character, TrieNode> children;
        boolean isEnd;

        public TrieNode() {
            children = new HashMap<>();
        }
    }

    static void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEnd = true;
    }

    static boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return false;
            }
            node = node.children.get(c);
        }
        return true;
    }

}