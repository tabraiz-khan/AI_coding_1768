public class Assignment5_1_1 {
    public static void main(String[] args) {
        Employee emp = new Employee("E001", "John Doe", "Software Engineer", 60000, 7);
        emp.displayDetails();
        double allowance = emp.calculateAllowance();
        System.out.println("Calculated Allowance: " + allowance);
        emp.displayDetails(); // Display updated details
    }
    
}
class Employee{
    String emp_id;
    String emp_name;
    String emp_designation;
    int basic_salary;
    float experience;
    public Employee(String emp_id, String emp_name, String emp_designation, int basic_salary, float experience){
        this.emp_id = emp_id;
        this.emp_name = emp_name;
        this.emp_designation = emp_designation;
        this.basic_salary = basic_salary;
        this.experience = experience;
    }

    public void displayDetails(){
        System.out.println("Employee ID: " + emp_id);
        System.out.println("Employee Name: " + emp_name);
        System.out.println("Employee Designation: " + emp_designation);
        System.out.println("Basic Salary: " + basic_salary);
        System.out.println("Experience: " + experience + " years");
    }

    public double calculateAllowance(){
        double allowance = 0;
        if(experience > 10){
            allowance = basic_salary * 0.20;
        } else if(experience >=5){
            allowance = basic_salary * 0.10;

        }
        else if(experience < 5){
            allowance = basic_salary * 0.05;
        }
        this.basic_salary += allowance;
        return allowance;
    }


}
        