package document;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.PrintWriter;

public class EfficientDocumentGrader {
    public static void main(String[] args) {
        try
        {
            System.out.println("NumberOfChars\tBasicTime\tEfficientTime");
            BufferedReader br = new BufferedReader(new FileReader("test_cases/mod2TestCases.txt"));
            String line;
            PrintWriter out = new PrintWriter("grader_output/module2.part1.out", "utf-8");
            while ((line = br.readLine()) != null)
            {
            	int charCount = line.length();
            	
            	BasicDocument bDoc = new BasicDocument(line);
            	bDoc.getFleschScore();
            	double bTime = bDoc.getTotalTime();
            	
                EfficientDocument efDoc = new EfficientDocument(line);
            	efDoc.getFleschScore();
                double efTime = efDoc.getTotalTime();
                
                String result = charCount + "\t\t" + bTime + "\t" + efTime;
                System.out.print(result);
                System.out.print("\n");
                out.print(result);
                out.print("\n");
                
            }
            out.print("\n");
            out.close();
            br.close();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}
