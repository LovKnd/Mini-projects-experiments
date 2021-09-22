package br.com.softblue.tictactoe.ui;

import br.com.softblue.commons.io.Console;

public class UI {

	public static void printText(String text) {
		System.out.println(text);
	}
	
	public static void printTextWithNNL(String text) {
		System.out.print(text);
	}
	
	public static void printNewLine() {
		System.out.println();
	}
	
	public static void printTitle() {
		printText("=================");
		printText("| Jogo Da Velha |");
		printText("=================");
		printNewLine();
	}
	
	public static String readInput(String text) {
		printTextWithNNL(text + " ");
		return Console.readString();
	}
}
