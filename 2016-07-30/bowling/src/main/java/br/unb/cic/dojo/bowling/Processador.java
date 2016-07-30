package br.unb.cic.dojo.bowling;

import java.util.ArrayList;
import java.util.List;

public class Processador {
	
	public int[] lista;

	public static List<Frame> processa(int[] jogadas) {
		List<Frame> lista = new ArrayList<Frame>();
		
		if(jogadas.length ==0)
			return lista;
			
			Frame f = new Frame();
			
			for (int i : jogadas) {
				if (f.isFull()) {
					lista.add(f);
					f = new Frame();
				}
				f.push(i);
			}
			
			lista.add(f);
		
		
		return lista;
	}

}

