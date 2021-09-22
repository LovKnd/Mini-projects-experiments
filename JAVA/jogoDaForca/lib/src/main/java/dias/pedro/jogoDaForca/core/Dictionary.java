package dias.pedro.jogoDaForca.core;

import java.lang.reflect.Constructor;

public abstract class Dictionary {
	
	private static Dictionary instance;
	
	// Design Pattern|Singleton
	public static Dictionary getInstance() {
		if (instance == null) {
			try {
				String dictionaryClassName = Config.get("dictionaryClassName");
				Class<?> clazz = Class.forName(dictionaryClassName);
				Constructor<?> constructor = clazz.getConstructor();
				instance = (Dictionary) constructor.newInstance();
			} catch (Exception e) {
				throw new RuntimeException(e);
			}
		}
		return instance;
	}

	public abstract Word nextWord();
}
