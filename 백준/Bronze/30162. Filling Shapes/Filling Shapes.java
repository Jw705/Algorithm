import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        if (n % 2 == 0) {
            int answer = 1;
            while (n > 1) {
                answer *= 2;
                n -= 2;
            }
            System.out.println(answer);
        } else {
            System.out.println(0);
        }

    }
}