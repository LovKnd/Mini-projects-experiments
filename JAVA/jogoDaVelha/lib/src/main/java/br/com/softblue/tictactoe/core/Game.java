package br.com.softblue.tictactoe.core;

import java.io.IOException;

import br.com.softblue.tictactoe.Constants;
import br.com.softblue.tictactoe.score.FileScoreManager;
import br.com.softblue.tictactoe.score.ScoreManager;
import br.com.softblue.tictactoe.ui.UI;

public class Game {

	private Board board = new Board();
	// Define a quantidade de jogadores
	private Player[] player = new Player[Constants.SYMBOL_PLAYERS.length];
	// O método nextPlayer() add 1 ao index
	private int currentPlayerIndex = -1;
	// Interface para o registro de pontuações
	private ScoreManager scoreManager;
	
	public void play() throws IOException {
		scoreManager = createScoreManager();
		
		UI.printTitle();
		
		// Cria os jogadores
		for (int index = 0; index < player.length; index++) {
			this.player[index] = createPlayer(index);
		}

		boolean gameEnded = false;
		Player winner = null;
		Player currentPlayer = nextPlayer();
		
		
		// Loop do Jogo
		while(!gameEnded) {
			board.print();
			
			boolean sequenceFound;
			try {
				sequenceFound = currentPlayer.play();
			} catch (InvalidMoveException e) {
				UI.printText("ERRO: " + e.getMessage());
				continue;
			}
			
			if (sequenceFound) {
				gameEnded = true;
				winner = currentPlayer;
				
			} else if (board.isFull()) {
				gameEnded = true;
			}
			
			currentPlayer = nextPlayer();
		}
		
		if (winner == null) {
			UI.printText("Empate");
		} else {
			UI.printText(winner.getName() + " ganhou");
			
			scoreManager.saveScore(winner);
		}
		
		board.print();
		UI.printText("Fim do jogo");
	}
	
	private Player createPlayer(int index) {
		String name = UI.readInput("Jogador " + (index + 1) + " =>");
		char symbol = Constants.SYMBOL_PLAYERS[index];
		Player player = new Player(name, symbol, this.board);
		
		Integer score = scoreManager.getScore(player);
		
		if (score != null) {
			UI.printText("O jogador " + player.getName() + " possui " + score + " vitória(s).");
		}
		
		UI.printText(name + " => " + symbol);
		
		return player;
	}
	
	private Player nextPlayer() {
		currentPlayerIndex = (currentPlayerIndex + 1) % player.length;
		return player[currentPlayerIndex];
	}
	
	private ScoreManager createScoreManager() throws IOException {
		return new FileScoreManager();
	}
}
