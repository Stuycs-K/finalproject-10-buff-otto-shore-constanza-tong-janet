import java.util.*;
import java.io.*;
import java.nio.*;

public class Encode{
	
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
	
		for(int i = 0; i < 3*8; i++){
			System.out.print((Integer)Byte.toUnsignedInt(bytes[i])+" ");
		}
		System.out.println();
		return bytes;
	}
	
	
	//A = 01000001
	//B = 01000010
	
	public static byte[] encode(byte[] bytes, String message){
		byte[] msg = new byte[message.length()*8];
		for(int i = 0; i < message.length(); i++){
			byte character = (byte)message.charAt(i);
			for(int j = 0; j <8; j++){
				msg[(i+1)*8 - j -1] = (byte)((character >> ((j)))&1);
				//msg[(i+1)*8 - j ] = (byte)((character >> ((j-1)))&1);
				
			}
		}				
		for(int i = 0; i < msg.length; i++){
			bytes[i] = (byte)((bytes[i] &254)| (msg[i]));
	//		System.out.println(bytes[i] + " " + msg[i]);
		}
		System.out.println(Arrays.toString(msg));
		
		for(int i = msg.length; i < bytes.length; i++){
			bytes[i] = (byte)(bytes[i] | 255);
		}
		
		for(int i = 0; i < msg.length; i++){
			System.out.print((Integer)Byte.toUnsignedInt(bytes[i])+" ");
		}
		return bytes;
	}
	
	public static void updateBytes(byte[] bytes, String filename){
		try{
			FileOutputStream file = new FileOutputStream(filename);
			file.write(bytes);
		}catch(IOException e){
			System.out.println("exception");
		}
		
	}
	public static void main(String[] args){
		//getBytes(args[0]);
		//encode(getBytes(args[0]), args[1]);
		//updateBytes(encode(getBytes(args[0]), args[1]), "encoded.txt");
		updateBytes(encode(getBytes(args[0]), args[1]), args[2]);
	}
	
	
	
	/*
	public static void decode(byte[] bytes){
		String ans = "";
		int j = 0;
		for(int i = 0; i < bytes.length; i++){
			int b = bytes[i];
			b = (byte)(b & 1);
			bytes[i] = (byte)b;
		}
		for(int i = 0; i < bytes.length - 8; i+=8){
			byte result = bytes[i+7];
			result = (byte)(result | (bytes[i+6] << 1));
			result =(byte)( result | (bytes[i+5] << 2));
			result = (byte)(result | (bytes[i+4] << 3));
			result = (byte)(result | (bytes[i+3] << 4));
			result = (byte)(result | (bytes[i+2] << 5));
			result = (byte)(result | (bytes[i+1] << 6));
			result = (byte)(result | (bytes[i] << 7));
			ans += (char)result;
		//	ans += (char)((((bytes[i] << 6) | (bytes[i+1] << 4)) | (bytes[i+2] << 2)) | (bytes[i+3]));
		}
	
		//System.out.println(ans.substring(0, 5));
	}
		*/
	
	
}
