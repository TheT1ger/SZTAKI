import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
	public static String home="..\\";

	public static void main(String[] args) {

		List<String> space = new ArrayList<String>();		

		Map<Character, Integer> apostrophe = new HashMap<Character, Integer>();
		Map<Character, Integer> doubled = new HashMap<Character, Integer>();
		Map<Character, Integer> initial = new HashMap<Character, Integer>();
		Map<Character, Integer> first = new HashMap<Character, Integer>();
		Map<Character, Integer> last = new HashMap<Character, Integer>();
		Map<Character, Integer> letters = new HashMap<Character, Integer>();
		Map<Integer, Map<String, Integer>> array = new HashMap<Integer, Map<String, Integer>>();
		for (int i = 0; i < 17; i++) {
			Map<String, Integer> temp = new HashMap<String, Integer>();
			array.put(i, temp);
		}

		boolean ap = false;
		boolean doub = false;
		boolean ws = false;
		boolean word = false;
		boolean endOfSentence = false;

		File folder = new File(home + "statistic\\english");
		File[] files = folder.listFiles();

		for (File f : files) {
			if(f.isDirectory())break;
			FileReader fr;
			try {
				fr = new FileReader(f);
			
			BufferedReader br = new BufferedReader(fr);

			String line;

			while ((line = br.readLine()) != null) {
				for (int i = 0; i < line.length(); i++) {
					if (line.charAt(i) == '\''
							&& (!Character.isJavaIdentifierPart(line
									.charAt(i + 1)) || i == line.length() - 1)) {

						line = line.substring(0, i) + "\""
								+ line.substring(i + 1, line.length());

					}
					if (line.charAt(i) == '\''
							&& (i == 0
									|| !Character.isJavaIdentifierPart(line
											.charAt(i - 1)) || line
									.charAt(i - 1) == '\"')) {
						line = line.substring(0, i) + "\""
								+ line.substring(i + 1, line.length());
					}
				}

				line = line.replace("\"", "");
				line = line.replace(",", "");
				line = line.replace("(", "");
				line = line.replace(")", "");
				line = line.replace("{", "");
				line = line.replace("}", "");
				line = line.replace("[", "");
				line = line.replace("]", "");
				line = line.replace("-", " ");
				line = line.replace("–", " ");
				line = line.replace("!", "");
				line = line.replace(";", "");
				line = line.replace("?", "");
				for(int i=0;i<10;i++){
					line = line.replace(i+"", "");
				}
				for (int i = 0; i < line.length(); i++) {
					char lower = Character.isUpperCase(line.charAt(i)) ? Character
							.toLowerCase(line.charAt(i)) : line.charAt(i);
					if (ap) {
						if (lower != 'a' && lower != 'u' && lower != 'e') {
							add(apostrophe, lower);
						}
						ap = false;
					}
					if (doub) {
						if (Character.isJavaIdentifierStart(lower)) {
							add(doubled, lower);
							doub = false;
						}
					}
					if (endOfSentence) {
						if (Character.isJavaIdentifierStart(lower)) {
							add(initial, lower);
							endOfSentence = false;
						}
					}
					if (ws) {
						if (Character.isJavaIdentifierStart(lower)) {
							add(first, lower);
							ws = false;
						}
					}
					if (word) {
						if (Character.isJavaIdentifierStart(lower)) {
							add(last, lower);
							word = false;
						}
					}
					if (Character.isJavaIdentifierStart(lower)) {
						add(letters, lower);
					}
					if (line.charAt(i) == '\'') {
						ap = true;
					}
					if (line.charAt(i) == '.') {
						endOfSentence = true;
					}
					if (line.charAt(i) == ' ' || line.charAt(i) == '.') {
						ws = true;
					}
					if (i < line.length() - 2
							&& (line.charAt(i + 2) == ' ' || line.charAt(i + 2) == '.')) {
						word = true;
					}
					if (i < line.length() - 1
							&& line.charAt(i) == line.charAt(i + 1)) {
						doub = true;
					}
				}
				line = line.replace(".", "");
				String[] wordsInLine = line.split(" ");
				for (String s : wordsInLine) {
					if (!s.isEmpty()) {
						Map<String, Integer> temp;
						if (s.length() < 16) {
							temp = array.get(s.length());
						}
						else{
							temp = array.get(16);
						}
						add(temp, s.toLowerCase());
					}
				}
			}

			br.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		save("Apostrophe", apostrophe);
		save("Double characters", doubled);
		save("Initial letter", initial);
		save("First letter", first);
		save("Last letter", last);
		save("Letters", letters);
		listWords(array);

		System.out.println();
		System.out.println();
		for (String s : space) {
			System.out.println(s);
		}
		System.out.println("ok");

	}

	public static int sum(Map m) {

		int count = 0;
		for (Object o : m.keySet()) {
			count += (int) m.get(o);
		}
		return count;
	}

	public static void save(String s,Map m){
		
		try {
			PrintWriter writer = new PrintWriter(home + "statistic\\english\\results\\"+ s +".txt");
			list(writer,m);
			writer.close();
		} catch (FileNotFoundException  e) {
			e.printStackTrace();
		}
	}
	
	public static void list(PrintWriter pw, Map m) {

		while (m.size() > 0) {
			Object o = m.keySet().iterator().next();
			int temp = (int) m.get(o);
			Object key = o;
			for (Object o2 : m.keySet()) {
				if ((int) m.get(o2) > temp) {
					temp = (int) m.get(o2);
					key = o2;
				}
			}
			pw.println(key + "," + temp);
			
			m.remove(key);
		}
	}
	
	public static void listWords(Map m){
		
		try {
			PrintWriter writer = new PrintWriter(home + "statistic\\english\\results\\Words.txt");
			for (int i = 0; i < 17; i++) {
				list(writer,(Map) m.get(i));
			}
			writer.close();
		} catch (FileNotFoundException  e) {
			e.printStackTrace();
		}	
	}

	@SuppressWarnings("unchecked")
	public static void add(Map m, Object o) {
		if (m.containsKey(o)) {
			int temp = (int) m.get(o);
			temp++;
			m.put(o, temp);
		} else {
			m.put(o, 1);
		}
	}

	public static int countWord(File f) {

		String line;
		FileReader fr;
		int count = 0;
		try {
			fr = new FileReader(f);
			BufferedReader br = new BufferedReader(fr);
			count = 0;
			try {
				while ((line = br.readLine()) != null) {
					for (int index = 0; index < line.length(); index++) {
						while (index < line.length()
								&& !Character.isJavaIdentifierStart(line
										.charAt(index))
								&& line.charAt(index) != ' ') {
							line = line.replace(
									Character.toString(line.charAt(index)), "");
						}
					}
					String[] lines = line.split(" ");
					for (String s : lines) {
						if (!s.isEmpty()) {
							count++;
						}
					}
				}
				br.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		return count;
	}

}
