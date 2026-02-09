public class Assignment5_1_7 {
    public static void main(String[] args) {
        int[] scores_list = {
            85, 42, 78, 90, 33, 67, 88, 45, 23, 56,
            72, 91, 38, 49, 60, 77, 84, 95, 29, 41,
            66, 73, 80, 54, 39, 92, 47, 58, 81, 34,
            69, 74, 86, 99, 21, 55, 63, 70, 82, 44,
            50, 61, 75, 89, 30, 53, 68, 79, 94, 37,
            65, 71, 83, 96, 28, 46, 59, 64, 87, 40
        };
        computeStatistics(scores_list);


        
    }

// create a function that takes scores_list which has 60 student's scores and computes key performance statistics
// Should return highest score, lowest scores, class average, number of students passed (score >= 40) and number of students failed (score < 40)
// use classes and objects to solve it
    public static void computeStatistics(int[] scores_list) {
        Statistics stats = new Statistics(scores_list);
        stats.calculate();
        stats.display();
    }
}
class Statistics {
    int[] scores;
    int highest;
    int lowest;
    double average;
    int passed;
    int failed;

    public Statistics(int[] scores) {
        this.scores = scores;
    }

    public void calculate() {
        highest = Integer.MIN_VALUE;
        lowest = Integer.MAX_VALUE;
        int total = 0;
        passed = 0;
        failed = 0;

        for (int score : scores) {
            if (score > highest) highest = score;
            if (score < lowest) lowest = score;
            total += score;
            if (score >= 40) passed++;
            else failed++;
        }
        average = (double) total / scores.length;
    }

    public void display() {
        System.out.println("Highest Score: " + highest);
        System.out.println("Lowest Score: " + lowest);
        System.out.println("Class Average: " + average);
        System.out.println("Number of Students Passed: " + passed);
        System.out.println("Number of Students Failed: " + failed);
    }
}
