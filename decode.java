public class Decode {
  public static String decodeMessage(int[][] arr) {
    StringBuilder newstr = new StringBuilder();
    
    if (arr != null) {
      for (int[] row : arr) {
        if (row != null) {
          for (int i : row) {
            newstr.append(i);
          }
        }
      }
    }
    
    String str = newstr.toString();
    StringBuilder message = new StringBuilder();
    
    for (int i = 0; i < str.length(); i += 8) {
      

      if (i + 8 > str.length()) {
        System.out.println((str.length() - i) + " incomplete bytes.");
        break;
      }
      
      String onebyte = str.substring(i, i + 8);
      
      int asc = Integer.parseInt(onebyte, 2);
      
      if (asc == 0) {
        break;
      }
      
      message.append((char) asc);
    }
    
    return message.toString();
  }
}
