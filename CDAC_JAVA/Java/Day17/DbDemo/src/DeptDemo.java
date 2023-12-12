import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.sql.*;

public class DeptDemo {
    public static void main(String[] args) throws SQLException {
        Connection con =null;

        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Enter dept no: ");
            int deptno = Integer.parseInt(br.readLine());

            //Step1
            //Load Driverclass in memory
            Class.forName("oracle.jdbc.driver.OracleDriver");

            //step2
            //Creating Connection (url,username,password)
            con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","12345");

            //step 3
            //Create Statement
           // Statement st = con.createStatement();
            PreparedStatement st = con.prepareStatement("Select * from emp where deptno =?");
            st.setInt(1,deptno);

            //step4
            //Excecuteing Query
            ResultSet rs = st.executeQuery();

            //Iterating through RS
            while(rs.next())
            {
                //Using Column index
                //System.out.println(rs.getInt(1)+ " "+ rs.getString(2));

                //Using Column name
                System.out.println(rs.getInt("Empno")+ " "+ rs.getString("Ename"));
            }



        }catch (Exception e)
        {
            e.printStackTrace();
        }
        finally {
            //step5
            //Close Connection
            con.close();
        }

    }
}
