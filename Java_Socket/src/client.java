import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class client {
    public static void main(String[] args) throws Exception {
        int port = 12345;
        ServerSocket serverSocket = new ServerSocket(port);
        System.out.println("Server started on port " + port);

        Socket clientSocket = serverSocket.accept();
        BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

        String line;
        while ((line = reader.readLine()) != null) { // Read messages line-by-line
            System.out.println("Received: " + line +" at "+System.currentTimeMillis() );
        }

        clientSocket.close();
        serverSocket.close();
    }
}
