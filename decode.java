import java.io.*;

public class Decode {

    public static String decode(byte[] bytes) {
        StringBuilder msg = new StringBuilder();
        int p = 0;
        byte l = 0;
        int b = 0;
        for (byte b : bytes) {
            l |= ((b & 1) << b);
            b++;
            if (b == 8) {
                if (l == 0xFF)
                  break;
                msg.append((char) (l & 0xFF));
                l = 0;
                b = 0;
            }
        }
        return msg.toString();
    }

    public static void main(String[] args) {
        
        String bf = args[0];
        String tf = args[1];
        try (FileOutputStream out = new FileOutputStream(tf)) {
            out.write(decode(getBytes(bf)).getBytes());
        } catch (IOException e) {
            System.err.println("Error, can't write to file: " + e.getMessage());
            System.exit(1);
        }
    }
}
