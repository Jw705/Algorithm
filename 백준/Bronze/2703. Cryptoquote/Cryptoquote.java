import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 1; i <= n; i++) {
            String input = br.readLine();
            String convertRule = br.readLine();
            String answer = "";
            for (int j = 0; j < input.length(); j++) {
                char ch = input.charAt(j);
                if (ch != ' ') {
                    answer = answer + convertRule.charAt((int) ch - (int) 'A');
                } else {
                    answer = answer + " ";
                }
            }
            System.out.println(answer);
        }

    }
}