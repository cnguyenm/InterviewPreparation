package HashTables;

import java.util.*;

/**
 You have a list of dishes. Each dish is associated with a list of ingredients used to prepare it.
 You want to group the dishes by ingredients,
 so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

 Return an array where each element is a list with the first element equal to the name of the ingredient
 and all of the other elements equal to the names of dishes that contain this ingredient.
 The dishes inside each list should be sorted lexicographically.
 The result array should be sorted lexicographically by the names of the ingredients in its elements.

 Example

 For

 dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
 ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
 ["Quesadilla", "Chicken", "Cheese", "Sauce"],
 ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

 the output should be

 groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
 ["Salad", "Salad", "Sandwich"],
 ["Sauce", "Pizza", "Quesadilla", "Salad"],
 ["Tomato", "Pizza", "Salad", "Sandwich"]]


 */


public class GroupingDishes {

    public static String[][] groupingDishes(String[][] dishes) {

        // check null
        if (dishes == null)
            return null;

        // var
        int row, col;
        String curDish;
        String curIngre;
        ArrayList<String> listDishes;
        HashMap<String, ArrayList<String>> map = new HashMap<>();

        // loop
        for (row = 0; row < dishes.length; row++) {

            // 1st index is dish
            curDish = dishes[row][0];

            // loop through all ingre
            for (col = 1; col < dishes[row].length; col++) {

                // get Ingre
                curIngre = dishes[row][col];

                // if map not have, add to map
                if (!map.containsKey(curIngre)) {
                    map.put(curIngre, new ArrayList<>());
                }

                // add dish to ingre->list<Dish>
                listDishes = map.get(curIngre);
                listDishes.add(curDish);
            }
        }

        // throw away ingre with less than 2
        String[] arrayIngre = map.keySet().toArray(new String[0]);
        for (String ingre : arrayIngre) {
            listDishes = map.get(ingre);
            if (listDishes.size() < 2) {
                map.remove(ingre);
            }
        }

        // create result
        String[][] result = new String[map.size()][];
        String[] arrayDishes;

        // sort list of ingredient
        String[] listIngre = map.keySet().toArray(new String[0]);
        Arrays.sort(listIngre);

        // get list of dishes
        int index = 0;
        for ( String ingre : listIngre) {

            // sort list of dishes
            listDishes = map.get(ingre);


            arrayDishes = listDishes.toArray(new String[0]);
            Arrays.sort(arrayDishes);

            // convert to list to put ingre as head
            listDishes = new ArrayList<String>(Arrays.asList(arrayDishes));
            listDishes.add(0, ingre);

            // put it into result
            result[index] = listDishes.toArray(new String[0]);
            index++;
        }

        return result;

    }


    public static void main(String[] args) {

        String[][] dishes =
                {   {"Salad","Tomato","Cucumber","Salad","Sauce"},
                    {"Pizza","Tomato","Sausage","Sauce","Dough"},
                    {"Quesadilla","Chicken","Cheese","Sauce"},
                    {"Sandwich","Salad","Bread","Tomato","Cheese"}  };

        String[][] result = groupingDishes(dishes);

        int row, col;
        for (row = 0; row < result.length; row++) {

            System.out.print(result[row][0] + ": ");
            for (col = 1; col < result[row].length; col++) {
                System.out.print(result[row][col] + ", ");
            }
            System.out.println();
        }

    }
}

























