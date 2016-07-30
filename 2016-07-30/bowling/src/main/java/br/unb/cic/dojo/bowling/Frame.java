package br.unb.cic.dojo.bowling;

import java.util.Arrays;

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
		return Arrays.toString(rolagem);
	}


}
