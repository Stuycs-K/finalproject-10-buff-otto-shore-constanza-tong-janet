import java.io.*;

public class Decode {

    public static byte[] getBytes(String filename) {
        byte[] bytes = new byte[1];
        try (FileInputStream fis = new FileInputStream('wavFiles/encoded/' + filename)) {
            bytes = fis.readAllBytes();
        } catch (IOException e) {
            System.out.println("File Not Found");
        }
        return bytes;
    }

    public static String decode(byte[] bytes) {
        StringBuilder msg = new StringBuilder();
        int p = 0;
        byte l = 0;
        int b = 0;
        for (byte b_loop : bytes) {
            l |= ((b_loop & 1) << (7 - b));
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
        if (args.length != 2) {
            System.err.println("Usage: Decode <encoded_input_file> <decoded_output_file>");
            System.exit(1);
        }

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
