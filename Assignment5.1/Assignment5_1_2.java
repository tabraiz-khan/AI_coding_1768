public class Assignment5_1_2 {
    public static void main(String[] args) {
        Electricity_Bill bill = new Electricity_Bill("C001", "Alice Smith", 350);
        bill.displayDetails();
        int bill_amt=bill.calculateBill();
        bill.total_bill=bill_amt;
        bill.displayDetails();
        
    }

    
}
class Electricity_Bill{
    String customer_id;
    String name;
    int units_consumed;
    int total_bill;
    public Electricity_Bill(String customer_id, String name, int units_consumed){
        this.customer_id = customer_id;
        this.name = name;
        this.units_consumed = units_consumed;
    }
    public void displayDetails(){
        System.out.println("Customer ID: " + customer_id);
        System.out.println("Customer Name: " + name);
        System.out.println("Units Consumed: " + units_consumed);
        System.out.println("Total bill calculation: " + total_bill);
    }   
    public int calculateBill(){
        double bill_amount = 0;
        if(units_consumed <= 100){
            bill_amount = units_consumed * 5;
        } 
        else if(units_consumed<=300){
            bill_amount= 100*5 + (units_consumed - 100)*7;

        }
        else{
            bill_amount= 100*5 + 200*7 + (units_consumed - 300)*10;
        }
        return (int)bill_amount;


    }
}
