package dias.pedro.jogoDaForca.game;

import java.util.HashSet;
import java.util.Set;

import dias.pedro.jogoDaForca.core.Config;
import dias.pedro.jogoDaForca.core.Dictionary;
import dias.pedro.jogoDaForca.core.InvalidCharacterException;
import dias.pedro.jogoDaForca.core.Word;
import dias.pedro.jogoDaForca.ui.UI;

public class Game {

	public void start(String[] args) {
		
		UI.print("Bem vindo ao jogo da forca!");
		
		Dictionary dictionary = Dictionary.getInstance();
		Word word = dictionary.nextWord();
		
		UI.print("A palavra tem " + word.size() + " letras.");
		
		Set<Character> usedChars = new HashSet<>();
		int errorCount = 0;
		
		if (args.length > 0) {
			Config.setMaxErrors(args[0]);
		}
		
		int maxErrors = Integer.parseInt(Config.get("MaxErrors"));
		UI.print("Tentaticas: " + maxErrors);
		
		// loop do jogo
		while (true) {
			UI.print(word);
			UI.newLine();
			
			char c;
			try {
				c = UI.readChar("Digite uma letra:");
				
				if (usedChars.contains(c)) {
					throw new InvalidCharacterException("Esta letra ja foi utilizada!");
				}
				
				usedChars.add(c);
				
				if (word.hasChar(c)) {
					UI.print("Você acertou!");
				} else {
					errorCount++;
				}
				
				if (errorCount < maxErrors) {
					UI.print("Você errou! Tente novamente.");
					UI.print("Chances restantes: " + (maxErrors - errorCount));
				}
					
				UI.newLine();
					
				if (word.discovered()) {
					UI.print("Parabéns!! Você ganhou!");
					UI.print("Palavra: " + word.getOriginalWord());
					UI.print("Fim do jogo!");
					break;
				}
					
				if (errorCount == maxErrors) {
					UI.print("Você perdeu!");
					UI.print("Palavra correta: " + word.getOriginalWord());
					UI.print("Fim do jogo!");
					break;
				}
				
			} catch (InvalidCharacterException e) {
				UI.print("ERRO: " + e.getMessage());
				UI.newLine();
			}
		}
	}
}
