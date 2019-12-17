
/**
 * Day3
 */

import java.util.*;
import java.io.*;

public class Day3 {

    public static void main(String[] args) {
        try {
            solve(getInput());
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    private static void solve(ArrayList<ArrayList<String>> wireInput) {
        HashMap<String, String> wires = new HashMap<String, String>();
        ArrayList<String> intersections = new ArrayList<String>();

        int x = 0;
        int y = 0;
        wires.put(x + "," + y, "O");
        int wireId = 1;
        for (ArrayList<String> wire : wireInput) {
            x = 0;
            y = 0;
            for (String inst : wire) {
                String dir = inst.substring(0, 1);
                int dis = Integer.parseInt(inst.substring(1, inst.length()));
                if (dir.equals("U")) {
                    for (; dis > 0; dis--, y++) {
                        addValue(wires, intersections, x, y, wireId);
                    }
                } else if (dir.equals("R")) {
                    for (; dis > 0; dis--, x++) {
                        addValue(wires, intersections, x, y, wireId);
                    }
                } else if (dir.equals("D")) {
                    for (; dis > 0; dis--, y--) {
                        addValue(wires, intersections, x, y, wireId);
                    }
                } else if (dir.equals("L")) {
                    for (; dis > 0; dis--, x--) {
                        addValue(wires, intersections, x, y, wireId);
                    }
                }
            }
            wireId++;
        }
        intersections.sort(intComparator);
        System.out.println(intersections);
        System.out.println(Math.abs(Integer.parseInt(intersections.get(0).split(",")[0]))
                + Math.abs(Integer.parseInt(intersections.get(0).split(",")[1])));
    }

    private static void addValue(HashMap<String, String> wires, ArrayList<String> intersections, int x, int y,
            int wireId) {
        String key = x + "," + y;
        if (wires.get(key) == "O") {
        } else if (wires.get(key) != null && !(wireId + "").equals(wires.get(key))) {
            wires.put(key, wireId + "");
            intersections.add(key);
        } else {
            wires.put(key, wireId + "");
        }

    }

    private static ArrayList<ArrayList<String>> getInput() throws IOException {
        File file = new File("./input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        ArrayList<ArrayList<String>> list1 = new ArrayList<ArrayList<String>>();

        String st;
        while ((st = br.readLine()) != null) {
            ArrayList<String> list2 = new ArrayList<String>();
            String[] codes = st.split(",");
            for (String x : codes) {
                list2.add(x);
            }
            list1.add(list2);
        }

        return list1;

    }

    public static Comparator<String> intComparator = new Comparator<String>() {
        @Override
        public int compare(String a, String b) {
            int valA = Math.abs(Integer.parseInt(a.split(",")[0])) + Math.abs(Integer.parseInt(a.split(",")[1]));
            int valB = Math.abs(Integer.parseInt(b.split(",")[0])) + Math.abs(Integer.parseInt(b.split(",")[1]));
            return valA - valB;
        }
    };
}
