public class RegCustomer extends Customer {
    private int reg_no;

    public int getReg_no() {
        return reg_no;
    }

    public void setReg_no(int reg_no) {
        this.reg_no = reg_no;
    }

    public RegCustomer(String name, String address, int reg_no) {
        super(name, address);
        this.reg_no = reg_no;
    }

    @Override
    public String toString() {
        return super.toString()+"RegCustomer [reg_no=" + reg_no + "]";
    }
    public double getDiscount(double shoppingPrice)
  {
    return shoppingPrice - shoppingPrice *0.05;
  }
    
    
}
