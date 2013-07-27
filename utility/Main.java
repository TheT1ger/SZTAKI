import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;


public class Main {

	public static void main(String[] args) {
		//Input file
		String origDicPath = "..\\..\\veryverycleandic.txt";
		//Output file
		String newDicPath = "..\\..\\NewCleanDic.txt";
		
		try {		
			String currentLine1 = null;
			String currentLine2 = null;
			BufferedReader br1 = new BufferedReader(new FileReader(origDicPath));
			BufferedWriter bw = new BufferedWriter(new FileWriter(newDicPath));
			boolean isFirstOccurance = true;
			ArrayList<String> WordsToRemove = new ArrayList<String>();

			System.out.println("Words that'll be removed:");
			
			//Vegig megyunk egy kulso ciklussal a szotaron
			while ((currentLine1 = br1.readLine()) != null) {
				//Jelzi h elso elofordulas-e a szotarban
				isFirstOccurance = true;
				//Megnezzzuk, hogy valoban elso-e (a default true miatt kell)
				for(String st : WordsToRemove){
					if(currentLine1.equals(st)){
						isFirstOccurance = false;
					}
				}
				BufferedReader br2 = new BufferedReader(new FileReader(origDicPath));
				//Belso ciklus amivel megegyszer vegigmegyunk
				while ((currentLine2 = br2.readLine()) != null) {
					//Ha az elso elofordulas mehet az outputba
					if(currentLine1.equals(currentLine2) && isFirstOccurance){
						bw.write(currentLine2);
						bw.newLine();
						isFirstOccurance = false;
					//Ha tobbedszeri elofordulas beleirjuk a listaba
					}else if(currentLine1.equals(currentLine2)){
						//Az elejen ures a lista ezert akkor azonnal irunk
						if(WordsToRemove.isEmpty()){
							System.out.println(currentLine2);
							WordsToRemove.add(currentLine2);
						}else{
							//Egyebkent ellenorizzuk h ne irjuk ki ugyanazt tobbszor
							boolean isToBeAdded = true;
							for(String str : WordsToRemove){
								if(str.equals(currentLine2)){
									isToBeAdded = false;
								}
							}
							//Ha eloszor irjuk ki akkor mehet
							if(isToBeAdded){
								System.out.println(currentLine2);
								WordsToRemove.add(currentLine2);
							}
						}
					}
				}
				br2.close();
			}
			
			
			br1.close();
			bw.close();
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}
