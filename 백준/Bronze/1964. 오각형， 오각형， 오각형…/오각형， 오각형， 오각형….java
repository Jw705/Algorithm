import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long n = Long.parseLong(br.readLine());
        long result = 5;

        for (long i = 2; i <= n; i++) {
            result = result + (i * 4) - (i - 1);  // 배열 대신 변수 사용
        }

        System.out.println(result % 45678);
    }
}