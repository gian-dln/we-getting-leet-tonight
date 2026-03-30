import java.util.*;

public class lab8 {
    
    /**
     * Main lab8 method - replace this with your actual problem logic
     * 
     */
    public String[] bestConfiguration(String[] colors) {
        // TODO: Implement your lab8 here
        Map<String, Integer> map = new HashMap<>();
        List<String> keys = new ArrayList<>();


        for (int i=0; i<colors.length; i++) {
            if (map.containsKey(colors[i])) {
                map.put(colors[i], map.get(colors[i])+1);
            }
            else {
                map.put(colors[i], 1);
                keys.add(colors[i]);
            }
        }

        Collections.sort(keys);


        System.out.println(keys);
        System.out.println(map);

        String[] result = new String[colors.length];
        int index = 0;

        for (String key: keys) {
            int count = map.get(key);

            for (int i=0; i<count; i++) {
                result[index] = key;
                index++;
            }
        }

        return result;
    }
    

    public static void main(String[] args) {
        lab8 lab8 = new lab8();
        String[] array1 = new String[] {"y", "c", "b", "c", "y", "c"};
        System.out.println(Arrays.toString(lab8.bestConfiguration(array1)));
        
    }
}