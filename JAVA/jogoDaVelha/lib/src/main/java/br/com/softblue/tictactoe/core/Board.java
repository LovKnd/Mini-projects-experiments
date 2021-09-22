package br.com.softblue.tictactoe.core;

import br.com.softblue.tictactoe.Constants;
import br.com.softblue.tictactoe.ui.UI;

public class Board {

	private char[][] matrix;
	
	public Board() {
		matrix = new char[Constants.BOARD_SIZE][Constants.BOARD_SIZE];
		clear();
	}
	
	public void clear() {
		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix[i].length; j++) {
				matrix [i][j] = ' ';
			}
		}
	}
	
	public void print() {
		UI.printNewLine();
		
		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix[i].length; j++) {
				UI.printTextWithNNL(String.valueOf(matrix[i][j]));
				
				if (j < matrix[i].length - 1) {
					UI.printTextWithNNL(" | ");
				} else if (i < matrix.length - 1) {
					UI.printNewLine();
					
					for (int n = 0; n < Constants.BOARD_SIZE; n++) {
						UI.printTextWithNNL("---");
					}
					UI.printNewLine();
				}
			}
			
			UI.printNewLine();
		}
	}
	
	public boolean isFull() {
		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix[i].length; j++) {
				if (matrix[i][j] == ' ') {
					return false;
				}
			}
		}
		
		return true;
	}
	
	public boolean play(Player player, Move move) throws InvalidMoveException {
		int i = move.getI();
		int j = move.getJ();
		int boardSize = Constants.BOARD_SIZE;
		
		if (i < 0 || j < 0 || i >= boardSize || j >= boardSize ) {
			throw new InvalidMoveException("Intervalo da jogada é inválido!");
		}
		
		if (matrix[i][j] != ' ') {
			throw new InvalidMoveException("Jogada Repetida!");
		}
		
		matrix[i][j] = player.getSymbol();
		
		return checkRows(player) || checkCols(player) || checkDiagonal1(player) || checkDiagonal2(player);
	}
	
	private boolean checkRows(Player player) {
		for (int i = 0; i < Constants.BOARD_SIZE; i++) {
			if (checkRow(player, i)) {
				return true;
			}
		}
		
		return false;
	}
	
	private boolean checkRow(Player player, int i) {
		char symbol = player.getSymbol();
		
		for (int j = 0; j < Constants.BOARD_SIZE; j++) {
			if (matrix[i][j] != symbol) {
				return false;
			}
		}
		
		return true;
	}
	
	private boolean checkCols(Player player) {
		for (int j = 0; j < Constants.BOARD_SIZE; j++) {
			if (checkCol(player, j)) {
				return true;
			}
		}
		
		return false;
	}
	
	private boolean checkCol(Player player, int j) {
		char symbol = player.getSymbol();
		
		for (int i = 0; i < Constants.BOARD_SIZE; i++) {
			if (matrix[i][j] != symbol) {
				return false;
			}
		}
		
		return true;
	}
	
	private boolean checkDiagonal1(Player player) {
		char symbol = player.getSymbol();
		
		for (int i = 0; i < Constants.BOARD_SIZE; i++) {
			if (matrix[i][i] != symbol) {
				return false;
			}
		}
		
		return true;
	}
	
	private boolean checkDiagonal2(Player player) {
		char symbol = player.getSymbol();
		int lastLine = Constants.BOARD_SIZE - 1;
		
		for (int i = lastLine, j = 0; i >= 0; i--, j++) {
			if (matrix[i][j] != symbol) {
				return false;
			}
		}
		
		return true;
	}
}
