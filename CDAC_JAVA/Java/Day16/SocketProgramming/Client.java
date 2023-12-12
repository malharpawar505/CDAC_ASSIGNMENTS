import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        final String SERVER_IP = "192.168.1.85";//"server_machine_ip"; // Replace with the server's IP address
      final int SERVER_PORT = 12345;
        try {
            Socket socket = new Socket(SERVER_IP, SERVER_PORT);
            
            // Set up input and output streams
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            // Read input from the console and send it to the server
            BufferedReader consoleInput = new BufferedReader(new InputStreamReader(System.in));
            String userInput;
            while ((userInput = consoleInput.readLine()) != null) {
                out.println(userInput);

                // Receive and display the server's response
                String serverResponse = in.readLine();
                System.out.println("Server: " + serverResponse);
            }

            // Close the resources
            in.close();
            out.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
