public class Assignment5_1_10 {
    public static void main(String[] args) {
        //I want you to write code for program that explains exception handling for different types of erros and give clear explanation 
        // with well formed comments in java
        // Exception handling in Java is a powerful mechanism to handle runtime errors and maintain the normal flow of the application.
        // It allows developers to write code that can gracefully handle exceptions, preventing the program from crashing and providing a way to recover from errors.
        // Here are some common types of exceptions in Java and how to handle them: 
        // 1. ArithmeticException: This exception occurs when an arithmetic operation goes wrong, such as division by zero.
        try {
            int result = 10 / 0; // This will throw ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero. Please provide a non-zero divisor.");
        }

        // 2. NullPointerException: This exception occurs when you try to use an object reference that has not been initialized (i.e., it is null).
        try {
            String str = null;
            System.out.println(str.length()); // This will throw NullPointerException
        } catch (NullPointerException e) {
            System.out.println("Cannot call a method on a null object. Please initialize the object before using it.");
        }
        // 3. ArrayIndexOutOfBoundsException: This exception occurs when you try to access an array index that is out of bounds.
        try {
            int[] arr = new int[5];
            System.out.println(arr[10]); // This will throw ArrayIndexOutOfBoundsException
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array index is out of bounds. Please check the array length and access a valid index.");
        }

        // 4. NumberFormatException: This exception occurs when you try to convert a string to a number, but the string does not have the appropriate format.
        try {
            int num = Integer.parseInt("abc"); // This will throw NumberFormatException
        } catch (NumberFormatException e) {
            System.out.println("Invalid number format. Please provide a valid integer string.");
        }
        // 5. IOException: This exception occurs when there is an input/output error, such as when reading from a file that does not exist.
        try {
            java.nio.file.Files.readAllLines(java.nio.file.Paths.get("nonexistentfile.txt")); // This will throw IOException
        } catch (java.io.IOException e) {
            System.out.println("An I/O error occurred. Please check if the file exists and is accessible.");
        }

        
    }
    
}
