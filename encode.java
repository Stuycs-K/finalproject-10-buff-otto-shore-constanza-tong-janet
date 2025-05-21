import java.util.*;
import java.io.*;
import java.nio.*;

public class encode{
	
	public static byte[] getBytes(String filename){
		byte[] bytes = new byte[1];
		try{
			File f = new File(filename);
			FileInputStream file = new FileInputStream(filename);
			bytes = new byte[(int)f.length()];
			file.read(bytes);
		}catch(IOException e){
			System.out.println("File Not Found");
		}
		
		
		return bytes;
		//return bytes extracted from file
	}
	
	public static byte[] encode(byte[] bytes, String message){
		return new byte[1];
		//return modified array of bytes
	}
	
	
	public static void main(String[] args){
		
	}
}