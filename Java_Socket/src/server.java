import java.io.OutputStream;
import java.net.Socket;
import java.util.concurrent.TimeUnit;

public class server {
    public static void main(String[] args) throws Exception {
        String host = "10.0.0.64";
        int port = 12345;

        Socket socket = new Socket(host, port);
        OutputStream out = socket.getOutputStream();

        String[] messages = {"Message1", "Message2", "Message3"};

        for (String message : messages) {
            out.write((message + "\n").getBytes()); // Append '\n' as the delimiter
            out.flush();
            TimeUnit.MILLISECONDS.sleep(50); // Simulate real-time delay
        }

        socket.close();
    }
}
