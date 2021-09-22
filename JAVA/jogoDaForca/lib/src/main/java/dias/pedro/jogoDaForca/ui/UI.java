package dias.pedro.jogoDaForca.ui;

import java.util.Scanner;

import dias.pedro.jogoDaForca.core.InvalidCharacterException;

public class UI {

	public static void print(Object text) {
		System.out.println(text);
	}
	
	public static void newLine() {
		System.out.println();
	}
	
	@SuppressWarnings("resource")
	public static char readChar(String text) throws InvalidCharacterException {
		System.out.println(text + " ");
		
		Scanner scanner = new Scanner(System.in);
		String line = scanner.nextLine();
		
		if (line.trim().isEmpty()) {
			throw new InvalidCharacterException("Nenhuma letra digitada.");
		}
		
		if (line.length() > 1) {
			throw new InvalidCharacterException("Mais de um caracter digitado.");
		}
		
		char c = line.charAt(0);
		
		if (!Character.isLetter(c)) {
			throw new InvalidCharacterException("O Caracter digitado não é uma letra.");
		}
		
		return c;
	}
}
