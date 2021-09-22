package br.com.softblue.tictactoe.core;

import br.com.softblue.tictactoe.ui.UI;

public class Player {

	private String name;
	private char symbol;
	private Board board = new Board();
	
	public Player(String name, char symbol, Board board) {
		this.name = name;
		this.symbol = symbol;
		this.board = board;
	}
	
	
	private Move inputMove() throws InvalidMoveException {
		String moveStr = UI.readInput("Jogador '" + name + "' =>");
		return new Move(moveStr);
	}

	public boolean play() throws InvalidMoveException {
		Move move = inputMove();
		return board.play(this, move);
	}
	
	
	public char getSymbol() {
		return symbol;
	}

	public String getName() {
		return name;
	}

	public Board getBoard() {
		return board;
	}
}
