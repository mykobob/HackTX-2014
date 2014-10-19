import java.util.*;
import java.net.*;
import java.io.*;
import java.text.*;
public class Server{
	public static void main(String[] args) throws Exception {
	    int port = 1337;
	    ServerSocket serverSocket = new ServerSocket(port);
	    System.err.println("Listening on port: " + port);
	    while (true) {
	        Socket clientSocket = serverSocket.accept();
	        System.err.println("Connection!");
	        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
	        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream()));
	        String s
	        out.write("HTTP/1.0 200 OK\r\n");
	        out.write("Content-Type: text/javascript\r\n");
	        out.write("Content-Length: 5\r\n");
	        out.write("\r\n");
	        out.write("\"yay\"");
	        out.close();
	        in.close();
	        try{
	        	Thread.sleep(100);
	        }catch(Exception e){
	        	e.printStackTrace();
	        }
	        ScreenCapture.save(new File("/Users/Jim/Dropbox/Notes/Note"+new SimpleDateFormat("MM-dd-yy-hh-mm").format(new Date())+".jpg"));
	        clientSocket.close();
	    }
	}
}