package HashTables;
import java.util.*;

/**
 * Created by chau on 10/13/2017.
 Given an array strings, determine whether it follows the sequence given in the patterns array.
 In other words, there should be no i and j for which strings[i] = strings[j]
 and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

 Example

 For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
 areFollowingPatterns(strings, patterns) = true;
 For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
 areFollowingPatterns(strings, patterns) = false
 *
 */
public class AreFollowingPatterns {

    public static boolean areFollowingPatterns(String[] strings, String[] patterns) {

        // check
        if (strings == null && patterns == null)
            return true;

        if (strings == null || patterns == null)
            return false;

        // var
        Map<String, String> map = new HashMap<>();
        int i;
        String value, key;

        for ( i = 0; i < patterns.length; i++) {

            // if key exist, but key -> wrong value
            if (map.containsKey(patterns[i])) {
                value = map.get(patterns[i]);
                if (strings[i].compareTo(value) != 0) {
                    return false;
                }
                // else correct
                continue;
            }

            // if value exist, but wrong_key -> value
            if (map.values().contains(strings[i])) {
                return false;
            }

            // else
            map.put(patterns[i], strings[i]);

        }

        return true;


    }

    public static void main(String[] args) {

        String[] strings = {"cat", "dog", "dog"};
        String[] patterns = {"a", "b", "b"};

        System.out.println(areFollowingPatterns(strings, patterns));
    }
}



























