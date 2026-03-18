
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        Set<Integer> set = new HashSet<>();
        Set<Integer> allSet = new HashSet<>(Set.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if(command.equals("all")) {
                set.addAll(allSet);
            }
            else if(command.equals("empty")) {
                set.clear();
            }

            else {
                int num = Integer.parseInt(st.nextToken());
                if(command.equals("check")) {
                    if(set.contains(num)) {
                        bw.write("1");
                    } else {
                        bw.write("0");
                    }
                    bw.newLine();
                }
                if(command.equals("toggle")) {
                    if(set.contains(num)) {
                        set.remove(num);
                    } else {
                        set.add(num);
                    }
                }
                if(command.equals("add")) {
                    set.add(num);
                }
                if(command.equals("remove")) {
                    set.remove(num);
                }
            }
        }

        bw.flush();
        bw.close();
    }
}
