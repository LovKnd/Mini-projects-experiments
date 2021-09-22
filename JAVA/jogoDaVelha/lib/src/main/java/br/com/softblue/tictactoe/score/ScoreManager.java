package br.com.softblue.tictactoe.score;

import java.io.IOException;

import br.com.softblue.tictactoe.core.Player;

public interface ScoreManager {

	Integer getScore(Player player);
	
	void saveScore(Player player) throws IOException;
}
