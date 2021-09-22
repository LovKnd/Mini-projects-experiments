package dias.pedro.jogoDaForca.core;

import java.io.IOException;
import java.util.Properties;

public class Config {

	private static Properties props = new Properties();
	
	static {
		try {
			props.load(Config.class.getResourceAsStream("/conf.propriedades"));
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}
	
	public static String get(String name) {
		return props.getProperty(name);
	}
	
	public static void setMaxErrors(String maxErrors) {
		props.setProperty("MaxErrors", maxErrors);
	}
}
