package br.com.softblue.tictactoe;

import java.io.IOException;

import br.com.softblue.tictactoe.core.Game;

public class Main {

	public static void main(String[] args) throws IOException {
		
		// Chamada para o jogo
		Game game = new Game();
		game.play();
	}

}
