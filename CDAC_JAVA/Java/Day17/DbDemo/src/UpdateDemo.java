import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class UpdateDemo {
    public static void main(String[] args) throws SQLException {
        Connection con =null;

        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Enter id: ");
            int userid = Integer.parseInt(br.readLine());
            System.out.println("Enter name: ");
            String name = br.readLine();


            //Step1
            //Load Driverclass in memory
            Class.forName("oracle.jdbc.driver.OracleDriver");

            //step2
            //Creating Connection (url,username,password)
            con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","12345");

            //step 3
            //Create Statement

            PreparedStatement st = con.prepareStatement(" Update user420 set name=? where id=?");
            st.setString(1,name);
            st.setInt(2,userid);


            //step4
            //Excecuteing Query
            int id = st.executeUpdate();

            System.out.println(id +"record Updated successfully.");


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

