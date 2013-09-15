import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;


public class Main {
	public static final int MAX_WORD_LENGTH = 7;
	public static final int MIN_WORD_LENGTH = 2;
	public static void main(String[] args) {
		//Input dic
		String origDicPath = "..\\..\\HunDic.txt";
		//Input text
		String text = "..\\..\\utility\\statistic\\hungarian\\linux.txt";
		//String text = "..\\..\\red hat.txt";
		
		//Output dic
		String newDicPath = "..\\..\\HunDic2.txt";
		
		try {		
			String currentLine = null;
			BufferedReader br = new BufferedReader(new FileReader(origDicPath));
			BufferedWriter bw = new BufferedWriter(new FileWriter(newDicPath));
			ArrayList<String[]> Dictionary = new ArrayList<String[]>();

			//Beolvassuk a szotarat
			while ((currentLine = br.readLine()) != null) {
				String word[] = new String[3];
				word = currentLine.split(",");
				Dictionary.add(word);
			}
			
			br.close();
			
			//Beolvassuk a szoveget
			br = new BufferedReader(new InputStreamReader(new FileInputStream(text),"UTF8"));
			while ((currentLine = br.readLine()) != null) {
				
				//Szavakra bontas
				for (int index = 0; index < currentLine.length(); index++) {
					while (index < currentLine.length()
						   && !Character.isLetter(currentLine.charAt(index))
						   && currentLine.charAt(index) != ' ') {
						currentLine = currentLine.replace(
						Character.toString(currentLine.charAt(index)), " ");
						currentLine = currentLine.replace("􀀢".charAt(0), ' ');

					}
				}
				//Megvannak a szavak
				String[] lines = currentLine.split(" ");
				
				boolean gotWord = false;
				for(String s : lines){
					s = s.toLowerCase();
					gotWord = false;
					//String[] currEntry;
					int index = 0;
					//Csak akkor van moka ha a max szohossznal nem hosszabb + 1 a /n miatt
					if(s.length() < MAX_WORD_LENGTH + 1 && s.length() > MIN_WORD_LENGTH - 1){
						
						//Megnezzuk hogy a szo benne van-e a szotarban
						for(int i = 0; i < Dictionary.size(); i++){
							if(s.equals(Dictionary.get(i)[0])){
								index = i;
								gotWord = true;
								break;
							}
						}
						//Ha nincs es nem ures string, beirjuk
						if(!gotWord && !s.equals("")){
							System.out.println("New word: " + s + "," + getPattern(s) + "," + "1");
							String[] addable = new String[3];
							addable[0] = s;
							addable[1] = getPattern(s);
							addable[2] = "1";
							Dictionary.add(addable);
							
						//Ha van freq-et modositunk
						}else if(gotWord){
							String [] currWord = Dictionary.get(index);
							int freq = Integer.parseInt(currWord[2]);
							freq++;
							currWord[2] = Integer.toString(freq);
							System.out.println("Frequency modified: " + currWord[0] + "," + currWord[2]);
							Dictionary.set(index, currWord);
						}
					}
				}
			}
		
		br.close();
		
		//Rendezes sajat rendezovel
		Collections.sort(Dictionary, new CustomArrayListComparator());
		//Iras file-ba
		for(String[] s : Dictionary){
			bw.write(s[0] + "," + s[1] + "," + s[2]);
			bw.newLine();
		}
		
		bw.close();
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	public static String getPattern(String inputWord){
	    ArrayList<String> tempPattern = new ArrayList<String>();
	    int sign = 1;
	    int used = 0;
	    int i;
	    // Előállít egy ugyanolyan hosszú listát, csupa kérdőjellel
	    for (i = 0; i < inputWord.length(); i++){
	        tempPattern.add("?");
	    }
	        
	    // Ha az input adott karaktere megismétlődik, akkor számmal jelzi minden előfordulásnál
	    for (i = 0; i < inputWord.length(); i++){
	        if (tempPattern.get(i) == "?"){
	            //for j in range(i+1,len(word)):
	        	for (int j = i + 1; j < inputWord.length(); j++){
	                if (inputWord.charAt(i) == inputWord.charAt(j)){
	                    if (used==0){
	                        // String indexelés
	                    	tempPattern.add(i, Integer.toString(sign));
	                    	tempPattern.remove(i+1);
	                    	
	                    }
	                    used=1;
	                    tempPattern.add(j, Integer.toString(sign));
                    	tempPattern.remove(j+1);
	                }
	        	}
	            if( used == 1){
	                if (sign<9){
	                    sign = sign + 1;
	                }	           
	                used=0;
	            }
	        }
	    }
	    // Listából string
	    String ret = "";
	    for(String s : tempPattern){
	    	ret += s;
	    }
	    return ret;
	}
}