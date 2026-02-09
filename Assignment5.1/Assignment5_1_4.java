public class Assignment5_1_4 {
    
    public static void main(String[] args) {
        LibraryBook book = new LibraryBook("B001", "The Great Gatsby", "F. Scott Fitzgerald", "Jane Doe", 12);
        book.displayDetails();  
        double late_fee = book.calculate_late_fee();
        System.out.println("Calculated Late Fee: " + late_fee);
    }
}
class LibraryBook{
    String book_id;
    String title;
    String author;
    String borrower;
    int days_late;
    public LibraryBook(String book_id, String title, String author, String borrower, int days_late){
        this.book_id = book_id;
        this.title = title;
        this.author = author;
        this.borrower = borrower;
        this.days_late = days_late;
    }
    public void displayDetails(){
        System.out.println("Book ID: " + book_id);
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Borrower: " + borrower);
        System.out.println("Days Late: " + days_late);
    }
    public double calculate_late_fee(){
       double late_fee = 0;
       if(days_late <=5){
          late_fee = days_late * 5;
       }
       else if(days_late <= 10){
          late_fee = 5*5 + (days_late - 5)*7;

       }
      else{
          late_fee = 5*5 + 5*7 + (days_late - 10)*10;
    }

     return late_fee;

    }
}
