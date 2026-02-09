public class ASsignment5_1_3 {
    public static void main(String[] args) {
        product prod = new product("P001", "Smartphone", 50000, "Electronics");
        prod.displayDetails();
        prod.calculateDiscount();
        System.out.println("Calculated Discount: " + prod.discount);
        System.out.println("Final Price after Discount: " + prod.final_price);


        
    }
    
}
class product{
    String product_id;
    String product_name;
    float price;
    String category;
    float discount;
    float final_price;
    public product(String product_id, String product_name, float price, String category){
        this.product_id = product_id;
        this.product_name = product_name;
        this.price = price;
        this.category = category;
        
    }
    public void displayDetails(){
        System.out.println("Product ID: " + product_id);
        System.out.println("Product Name: " + product_name);
        System.out.println("Price: " + price);
        System.out.println("Category: " + category);
    }
    public float calculateDiscount(){
        float discount = 0;
        if(category.equalsIgnoreCase("Electronics")){
            discount = price * 0.10f;
        } 
        else if(category.equalsIgnoreCase("Clothing")){
            discount = price * 0.15f;

        }
        else{
            discount = price * 0.05f;
        }
        this.discount=discount;
        this.final_price=price - discount;


        return discount;


}   

}
