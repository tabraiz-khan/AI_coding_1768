public class Assignment5_1_8 {
    public static void main(String[] args) {
        // generate two methods to check primenumber , one should be naive approach and other should be optimized approach and explain how it imporves performance through well commented explanation
        int num = 17;   
        System.out.println("Naive Approach: Is " + num + " a prime number? " + isPrimeNaive(num));
        System.out.println("Optimized Approach: Is " + num + " a prime number? " + isPrimeOptimized(num));



        
    }
    // Naive approach to check for prime number
    public static boolean isPrimeNaive(int n) {
        // Check for edge cases
        if (n <= 1) return false; // 0 and 1 are not prime numbers
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false; // Found a divisor, not a prime number
            }
        }
        return true; // No divisors found, it's a prime number
    }

    // Optimized approach to check for prime number
    public static boolean isPrimeOptimized(int n) {
        // Check for edge cases
        if (n <= 1) return false; // 0 and 1 are not prime numbers
        if (n <= 3) return true;  // 2 and 3 are prime numbers

        // Eliminate multiples of 2 and 3
        if (n % 2 == 0 || n % 3 == 0) {
            return false; // Found a divisor, not a prime number
        }

        // Check for factors from 5 to sqrt(n)
        // We can skip even numbers by checking i and i + 2
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false; // Found a divisor, not a prime number
            }
        }
        return true; // No divisors found, it's a prime number
        
    }

  
    
    
}