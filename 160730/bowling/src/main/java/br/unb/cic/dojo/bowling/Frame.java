package br.unb.cic.dojo.bowling;


public class Frame {
	
	private final int[] rolagem = new int[2];
	private int idx = 0;
	private boolean full = false;
	private int total = 0;
	
	public Frame() {
		for (int i=0; i < rolagem.length; i++) {
			rolagem[i] = -1;
		}
	}
	
	public void push(int value) {
		this.rolagem[idx++] = value;
		total += value;
		if (total > 10)
			throw new IllegalArgumentException("Frame nao pode ser maior que 10");
		if (idx == 2 || total == 10){
			full = true;
		}
	}
	
	public int get(int n)
	{
		return rolagem[n];
	}
	
	public boolean isFull() {
		return full;
	}
	
	@Override
	public String toString() {
		String resultado = "[";

		if (total == 10) {
			if (idx == 1) { // Strike
				resultado += "X";
			}
			else {
				if (rolagem[0] == 0)
					resultado += "-,/";
				else
					resultado += rolagem[0] +",/"; 
			}
		}
		else {
			for (int i = 0; i < 2; i++){
				switch (rolagem[i]){
				case -1:
					resultado += "_";
					break;
				case 0:
					resultado += "-";
					break;
				default:
					resultado += rolagem[i];
				}
				if (i == 0) resultado += ",";
			}
		}
		resultado += "]";
		return resultado;
	}

	public int getTotal() {
		if (isFull()){
			return total;
		}
		return 0;
	}


}
