import java.util.*;
import java.io.*;
import java.nio.*;

public class encode{
	
	public static byte[] getBytes(String filename){ 		//return bytes extracted from file
		byte[] bytes = new byte[1];
		try{
			File f = new File(filename);
			FileInputStream file = new FileInputStream(filename);
			bytes = new byte[(int)f.length()];
			file.read(bytes);
		}catch(IOException e){
			System.out.println("File Not Found");
		}
	
	 // System.out.println(Arrays.toString(bytes));

		return bytes;
	}
	
	
	//A = 01000001
	
	public static byte[] encode(byte[] bytes, String message){
		byte[] msg = new byte[message.length()*8];
		for(int i = 0; i < message.length(); i++){
			byte character = (byte)message.charAt(i);
			for(int j = 8; j > 0; j--){
				msg[i*8 + j - 1] = (byte)((character >> ((j-1)))&1);
			}
		}
				
		for(int i = 0; i < msg.length; i++){
			bytes[i] = (byte)(bytes[i] | msg[i]);
		}
		for(int i = msg.length; i < bytes.length; i++){
			bytes[i] = (byte)(bytes[i] | 0);
		}
	//	System.out.println(Arrays.toString(bytes));
		return bytes;
	}
	
	
	public static void main(String[] args){
		//getBytes(args[0]);
		encode(getBytes(args[0]), "A");
	}
}