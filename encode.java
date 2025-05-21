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
	
		//testing
		/* for(int i = 0; i < bytes.length; i++){
			System.out.println((Integer)Byte.toUnsignedInt(bytes[i])+" ");
		} */
	  //System.out.println(Arrays.toString(bytes));

		return bytes;
	}
	
	public static byte[] encode(byte[] bytes, String message){
		byte[] msg = new byte[message.length()*4];
		for(int i = 0; i < message.length(); i++){
			byte character = (byte)message.charAt(i);
			for(int j = 0; j < 4; j++){
				char[i*4 + j] = character >>
			}
		}
		return new byte[1];
		//return modified array of bytes
	}
	
	
	public static void main(String[] args){
		//getBytes(args[0]);
	}
}