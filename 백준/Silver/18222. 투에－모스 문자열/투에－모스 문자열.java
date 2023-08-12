import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long k = sc.nextLong();
        long i = 1L, cnt = 0L;
        while (i * 2 < k)
            i *= 2;
        while (k != 1) {
            if (i < k) {
                cnt++;
                k -= i;
            }
            i /= 2;
        }
        System.out.println(cnt % 2 == 0 ? 0 : 1);
    }

}