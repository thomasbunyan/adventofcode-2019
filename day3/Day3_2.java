
/**
 * Day3
 */

import java.util.*;
import java.io.*;

public class Day3_2 {

    public static void main(String[] args) {
        try {
            solve(getInput());
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    private static void solve(ArrayList<ArrayList<String>> wireInput) {
        HashMap<String, String> wires = new HashMap<String, String>();
        HashMap<String, Integer> intersections = new HashMap<String, Integer>();

        int x = 0;
        int y = 0;
        wires.put(x + "," + y, "O");
        int wireId = 1;
        for (ArrayList<String> wire : wireInput) {
            x = 0;
            y = 0;
            int distance = 0;
            for (String inst : wire) {
                String dir = inst.substring(0, 1);
                int dis = Integer.parseInt(inst.substring(1, inst.length()));
                if (dir.equals("U")) {
                    for (; dis > 0; dis--, y++, distance++) {
                        addValue(wires, intersections, x, y, wireId, distance);
                    }
                } else if (dir.equals("R")) {
                    for (; dis > 0; dis--, x++, distance++) {
                        addValue(wires, intersections, x, y, wireId, distance);
                    }
                } else if (dir.equals("D")) {
                    for (; dis > 0; dis--, y--, distance++) {
                        addValue(wires, intersections, x, y, wireId, distance);
                    }
                } else if (dir.equals("L")) {
                    for (; dis > 0; dis--, x--, distance++) {
                        addValue(wires, intersections, x, y, wireId, distance);
                    }
                }
            }
            wireId++;
        }

        int min = Integer.MAX_VALUE;
        for (int val : intersections.values()) {
            if (val < min)
                min = val;
        }
        System.out.println(min);

    }

    private static void addValue(HashMap<String, String> wires, HashMap<String, Integer> intersections, int x, int y,
            int wireId, int distance) {
        String key = x + "," + y;
        if (wires.get(key) == "O") {
        } else if (wires.get(key) != null && !(wireId + "").equals(wires.get(key).split("-")[0])) {
            int oldDis = Integer.parseInt(wires.get(key).split("-")[1]);
            intersections.put(key, distance + oldDis);
            if (oldDis < distance)
                distance = oldDis;
            wires.put(key, wireId + "-" + distance);
        } else {
            wires.put(key, wireId + "-" + distance);
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
}
