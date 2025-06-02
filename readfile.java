import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadFile {
  
  public int[][] readf(String filename){
    StringBuilder info = new Stringbuilder();
    try {
      File myObj = new File("test2.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    return data;
  }
  
  public static int countLines(File aFile) throws IOException {
      LineNumberReader reader = null;
      try {
          reader = new LineNumberReader(new FileReader(aFile));
          while ((reader.readLine()) != null);
          return reader.getLineNumber();
      } catch (Exception ex) {
          return -1;
      } finally {
          if(reader != null)
              reader.close();
      }
  }
  
      public static byte[] getBytes(String filename) {
          byte[] bytes = new byte[1];
          try (FileInputStream fis = new FileInputStream(filename)) {
              bytes = fis.readAllBytes();
          } catch (IOException e) {
              System.out.println("File Not Found");
          }
          return bytes;
      }

}

}
